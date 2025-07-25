# Logistic Disparity Sensor (LDS) Core Scanner
# Built by Jinn | Human-Friendly Format by Monday 🦝

def calculate_lds_score(data):
    # Convert category inputs to weights (simple example)
    geo_weight = {
        "rural": 1.2,
        "inner_city": 1.1,
        "tribal": 1.3,
        "suburban": 0.8,
        "urban": 0.9
    }

    media_weight = {
        "no_exposure": 1.5,
        "radio_only": 1.2,
        "TV_only": 1.0,
        "ad_lagged": 1.3,
        "mainstream": 0.7
    }

    era_bias = {
        "pre_digital": 1.4,
        "catalog_era": 1.3,
        "digital_camera": 1.0,
        "smartphone_era": 0.7
    }

    # Pull weighted values (with fallback)
    g = geo_weight.get(data.get("geolocation_type", ""), 1.0)
    m = media_weight.get(data.get("media_sync", ""), 1.0)
    e = era_bias.get(data.get("capture_era", ""), 1.0)

    # Binary flags
    access_obscure = 1.2 if data.get("access_mode", "") in ["catalog", "discount", "surplus"] else 1.0
    has_variant_evidence = 1.3 if data.get("product_variant_evidence") else 1.0
    confirmed_by_others = 1.2 if data.get("community_validation") else 1.0
    suppression_pressure = 1.4 if data.get("memory_suppression_pressure") else 1.0
    ad_match_consistent = 0.9 if data.get("ad_match_consistency") else 1.0
    found_in_central_records = 0.8 if data.get("central_record_match") else 1.0

    # Core score
    numerator = g * m * e * access_obscure * has_variant_evidence * confirmed_by_others * suppression_pressure
    denominator = ad_match_consistent * found_in_central_records

    lds_score = numerator / max(denominator, 0.1)

    # Classification
    if lds_score > 2.0:
        zone = "Relief Zone"
    elif lds_score > 1.5:
        zone = "Catalog/Variant Zone"
    elif lds_score > 1.1:
        zone = "Localized Divergence Zone"
    else:
        zone = "Mainstream Zone"

    return {
        "lds_score": round(lds_score, 2),
        "zone": zone,
        "message": f"🧠 Memory context likely shaped by access disparity. ({zone})"
    }

# === EXAMPLE USAGE ===
if __name__ == "__main__":
    # Paste or modify this with real input
    memory_data = {
        "geolocation_type": "rural",
        "media_sync": "radio_only",
        "capture_era": "catalog_era",
        "access_mode": "catalog",
        "product_variant_evidence": True,
        "community_validation": True,
        "memory_suppression_pressure": True,
        "ad_match_consistency": False,
        "central_record_match": False
    }

    result = calculate_lds_score(memory_data)
    print("\n🛰 Logistic Disparity Sensor Result:")
    print(f"Score: {result['lds_score']}")
    print(f"Zone: {result['zone']}")
    print(f"Message: {result['message']}\n)

  What It Does:
	•	Takes inputs about where/when/how someone might’ve seen a weird version of reality
	•	Calculates how likely that memory is due to access/supply disparity
	•	Classifies it into a “zone” (like “Catalog/Variant” or “Relief Zone”)
