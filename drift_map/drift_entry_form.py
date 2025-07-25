import json
import os

def get_input(prompt, default=None, options=None):
    """Helper function for user input with default and optional values."""
    if options:
        print(f"{prompt} ({'/'.join(options)})")
    else:
        print(prompt)
    response = input("> ").strip()
    if not response and default is not None:
        return default
    if options and response not in options:
        print("⚠️ Invalid choice. Using default.")
        return default
    return response or default

def yes_no(prompt):
    return get_input(f"{prompt} (y/n)", default="n", options=["y", "n"]) == "y"

def collect_entry():
    print("\n🧠 Drift Memory Entry Wizard\n")
    
    entry = {
        "region_label": input("Region Label (e.g. Pine Ridge Reservation): ").strip(),
        "state_or_country": input("State or Country: ").strip(),
        "timeline": input("Memory or Product Time Range (e.g. 1992–2001): ").strip(),
        "zone_type": get_input("Zone Type", options=[
            "Rural", "Inner City", "Tribal Land", "Border Zone",
            "Post-Disaster", "Migrant", "Other"
        ]),
        "access_pattern": get_input("Access Pattern", options=[
            "Catalog", "Discount Chain", "Relief Supply", "Church Sale",
            "Flea Market", "Donation Bin", "Local Reseller", "Other"
        ]),
        "product_examples": input("Product Examples (comma separated): ").split(","),
        "distribution_anomaly_type": get_input("Distribution Anomaly Type", options=[
            "Misprint", "Branding Lag", "Mislabel", "Early Packaging", "Recalled Item", "Unknown"
        ]),
        "media_ad_match": get_input("Media Ad Match", options=[
            "Never saw ads", "Didn’t match TV", "Matched ads", "Not applicable"
        ]),
        "community_confirmation": get_input("Community Confirmation", options=[
            "Confirmed", "Mixed", "Contradicted", "Unknown"
        ]),
        "imperfect_normalization_zone": yes_no("Was this an imperfect normalization zone?"),
        "notes": input("Notes (freeform – observed drift, feelings, context): ").strip()
    }

    return entry

def save_entry(entry, directory="drift_map"):
    # Make sure the directory exists
    os.makedirs(directory, exist_ok=True)

    # Generate filename
    safe_label = entry['region_label'].lower().replace(" ", "_")
    safe_time = entry['timeline'].replace("–", "-").replace(" ", "")
    filename = f"{safe_label}_{safe_time}.json"

    filepath = os.path.join(directory, filename)

    with open(filepath, "w") as f:
        json.dump(entry, f, indent=2)
    
    print(f"\n✅ Drift memory entry saved to {filepath}")

def main():
    entry = collect_entry()
    save_entry(entry)

if __name__ == "__main__":
    main()
