#!/usr/bin/env python3
"""
Logistic Disparity Sensor — Simulation

Generates a population of memory reports across different regions,
eras, and access patterns, scores each one through the LDS algorithm,
then prints a full breakdown: per-zone stats, regional comparisons,
and detailed case studies showing how logistics — not delusion —
explain divergent memories.

Run:
    python lds-simulation.py
"""

import random
import json
import sys

# ---------------------------------------------------------------------------
# LDS scoring engine (imported inline so the sim is self-contained)
# ---------------------------------------------------------------------------

GEO_WEIGHT = {
    "rural": 1.2, "inner_city": 1.1, "tribal": 1.3,
    "suburban": 0.8, "urban": 0.9,
}
MEDIA_WEIGHT = {
    "no_exposure": 1.5, "radio_only": 1.2, "TV_only": 1.0,
    "ad_lagged": 1.3, "mainstream": 0.7,
}
ERA_BIAS = {
    "pre_digital": 1.4, "catalog_era": 1.3,
    "digital_camera": 1.0, "smartphone_era": 0.7,
}

ZONE_THRESHOLDS = [
    (2.0, "Relief Zone"),
    (1.5, "Catalog/Variant Zone"),
    (1.1, "Localized Divergence Zone"),
]
DEFAULT_ZONE = "Mainstream Zone"


def calculate_lds_score(data):
    g = GEO_WEIGHT.get(data.get("geolocation_type", ""), 1.0)
    m = MEDIA_WEIGHT.get(data.get("media_sync", ""), 1.0)
    e = ERA_BIAS.get(data.get("capture_era", ""), 1.0)

    access_obscure = 1.2 if data.get("access_mode", "") in ["catalog", "discount", "surplus"] else 1.0
    has_variant = 1.3 if data.get("product_variant_evidence") else 1.0
    confirmed = 1.2 if data.get("community_validation") else 1.0
    suppression = 1.4 if data.get("memory_suppression_pressure") else 1.0
    ad_match = 0.9 if data.get("ad_match_consistency") else 1.0
    central = 0.8 if data.get("central_record_match") else 1.0

    numerator = g * m * e * access_obscure * has_variant * confirmed * suppression
    denominator = ad_match * central
    score = numerator / max(denominator, 0.1)

    zone = DEFAULT_ZONE
    for threshold, label in ZONE_THRESHOLDS:
        if score > threshold:
            zone = label
            break

    return {"lds_score": round(score, 2), "zone": zone}


# ---------------------------------------------------------------------------
# Region profiles — each encodes realistic demographic/logistics biases
# ---------------------------------------------------------------------------

REGIONS = [
    {
        "name": "Pine Ridge Reservation, SD",
        "geo_pool": ["tribal"],
        "media_pool": ["no_exposure", "radio_only"],
        "era_pool": ["pre_digital", "catalog_era"],
        "access_pool": ["surplus", "catalog"],
        "variant_prob": 0.75,
        "community_prob": 0.80,
        "suppression_prob": 0.70,
        "ad_match_prob": 0.05,
        "central_prob": 0.05,
    },
    {
        "name": "Rural Appalachia, WV",
        "geo_pool": ["rural"],
        "media_pool": ["radio_only", "TV_only", "no_exposure"],
        "era_pool": ["pre_digital", "catalog_era"],
        "access_pool": ["catalog", "discount"],
        "variant_prob": 0.65,
        "community_prob": 0.70,
        "suppression_prob": 0.55,
        "ad_match_prob": 0.10,
        "central_prob": 0.10,
    },
    {
        "name": "South Philadelphia, PA",
        "geo_pool": ["inner_city"],
        "media_pool": ["ad_lagged", "TV_only", "mainstream"],
        "era_pool": ["catalog_era", "digital_camera"],
        "access_pool": ["discount", "catalog"],
        "variant_prob": 0.50,
        "community_prob": 0.55,
        "suppression_prob": 0.35,
        "ad_match_prob": 0.30,
        "central_prob": 0.25,
    },
    {
        "name": "Northern Wisconsin (surplus zone)",
        "geo_pool": ["rural"],
        "media_pool": ["radio_only", "no_exposure", "ad_lagged"],
        "era_pool": ["catalog_era", "pre_digital"],
        "access_pool": ["surplus", "discount"],
        "variant_prob": 0.70,
        "community_prob": 0.65,
        "suppression_prob": 0.60,
        "ad_match_prob": 0.10,
        "central_prob": 0.08,
    },
    {
        "name": "Suburban Denver, CO",
        "geo_pool": ["suburban"],
        "media_pool": ["mainstream", "TV_only"],
        "era_pool": ["digital_camera", "smartphone_era"],
        "access_pool": ["mainstream"],
        "variant_prob": 0.10,
        "community_prob": 0.15,
        "suppression_prob": 0.05,
        "ad_match_prob": 0.80,
        "central_prob": 0.85,
    },
    {
        "name": "Downtown Chicago, IL",
        "geo_pool": ["urban"],
        "media_pool": ["mainstream", "TV_only"],
        "era_pool": ["digital_camera", "smartphone_era"],
        "access_pool": ["mainstream"],
        "variant_prob": 0.12,
        "community_prob": 0.10,
        "suppression_prob": 0.05,
        "ad_match_prob": 0.85,
        "central_prob": 0.90,
    },
    {
        "name": "Border Town, TX",
        "geo_pool": ["rural", "inner_city"],
        "media_pool": ["ad_lagged", "radio_only", "no_exposure"],
        "era_pool": ["catalog_era", "digital_camera"],
        "access_pool": ["surplus", "discount"],
        "variant_prob": 0.60,
        "community_prob": 0.60,
        "suppression_prob": 0.50,
        "ad_match_prob": 0.15,
        "central_prob": 0.12,
    },
    {
        "name": "Post-Katrina New Orleans, LA",
        "geo_pool": ["inner_city", "rural"],
        "media_pool": ["no_exposure", "radio_only"],
        "era_pool": ["digital_camera"],
        "access_pool": ["surplus"],
        "variant_prob": 0.70,
        "community_prob": 0.75,
        "suppression_prob": 0.65,
        "ad_match_prob": 0.08,
        "central_prob": 0.10,
    },
]

# Products that can exhibit variant drift
PRODUCTS = [
    {"name": "Froot Loops / Fruit Loops", "variant": "Fruit Loops", "window": "1985-1999"},
    {"name": "Febreze / Febreeze", "variant": "Febreeze", "window": "1996-1997"},
    {"name": "Looney Tunes / Looney Toons", "variant": "Looney Toons", "window": "1970s-2000s"},
    {"name": "Berenstain / Berenstein Bears", "variant": "Berenstein Bears", "window": "1980-2002"},
    {"name": "Jiffy / Jif Peanut Butter", "variant": "Jiffy", "window": "1975-1995"},
    {"name": "Oscar Mayer / Oscar Meyer", "variant": "Oscar Meyer", "window": "1980-2000"},
    {"name": "Sketchers / Skechers", "variant": "Sketchers", "window": "1998-2010"},
    {"name": "Chic-fil-A / Chick-fil-A", "variant": "Chic-fil-A", "window": "1990-2005"},
]


# ---------------------------------------------------------------------------
# Simulation engine
# ---------------------------------------------------------------------------

def generate_memory(region, rng):
    """Synthesize one memory report from a region profile."""
    product = rng.choice(PRODUCTS)
    return {
        "region": region["name"],
        "product": product["name"],
        "variant_seen": product["variant"],
        "distribution_window": product["window"],
        "geolocation_type": rng.choice(region["geo_pool"]),
        "media_sync": rng.choice(region["media_pool"]),
        "capture_era": rng.choice(region["era_pool"]),
        "access_mode": rng.choice(region["access_pool"]),
        "product_variant_evidence": rng.random() < region["variant_prob"],
        "community_validation": rng.random() < region["community_prob"],
        "memory_suppression_pressure": rng.random() < region["suppression_prob"],
        "ad_match_consistency": rng.random() < region["ad_match_prob"],
        "central_record_match": rng.random() < region["central_prob"],
    }


def run_simulation(n_per_region=50, seed=42):
    rng = random.Random(seed)
    results = []

    for region in REGIONS:
        for _ in range(n_per_region):
            memory = generate_memory(region, rng)
            score_result = calculate_lds_score(memory)
            memory["lds_score"] = score_result["lds_score"]
            memory["zone"] = score_result["zone"]
            results.append(memory)

    return results


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def print_header(title):
    width = 70
    print()
    print("=" * width)
    print(f"  {title}")
    print("=" * width)


def print_zone_summary(results):
    print_header("ZONE DISTRIBUTION")
    zones = {}
    for r in results:
        zones.setdefault(r["zone"], []).append(r["lds_score"])

    zone_order = ["Relief Zone", "Catalog/Variant Zone",
                  "Localized Divergence Zone", "Mainstream Zone"]

    total = len(results)
    for zone in zone_order:
        scores = zones.get(zone, [])
        count = len(scores)
        pct = (count / total) * 100
        avg = sum(scores) / count if scores else 0
        lo = min(scores) if scores else 0
        hi = max(scores) if scores else 0
        bar = "#" * int(pct / 2)
        print(f"\n  {zone}")
        print(f"    Count : {count}/{total} ({pct:.1f}%)")
        print(f"    Scores: avg {avg:.2f}  |  range [{lo:.2f} - {hi:.2f}]")
        print(f"    {bar}")


def print_regional_breakdown(results):
    print_header("REGIONAL BREAKDOWN")

    by_region = {}
    for r in results:
        by_region.setdefault(r["region"], []).append(r)

    # Sort by average score descending
    region_avgs = []
    for region, entries in by_region.items():
        avg = sum(e["lds_score"] for e in entries) / len(entries)
        region_avgs.append((region, entries, avg))
    region_avgs.sort(key=lambda x: -x[2])

    for region, entries, avg in region_avgs:
        zones = {}
        for e in entries:
            zones[e["zone"]] = zones.get(e["zone"], 0) + 1

        dominant_zone = max(zones, key=zones.get)
        hi = max(e["lds_score"] for e in entries)
        lo = min(e["lds_score"] for e in entries)

        print(f"\n  {region}")
        print(f"    Avg Score: {avg:.2f}  |  Range: [{lo:.2f} - {hi:.2f}]")
        print(f"    Dominant Zone: {dominant_zone}")
        print(f"    Zone split: ", end="")
        parts = []
        for z in ["Relief Zone", "Catalog/Variant Zone",
                   "Localized Divergence Zone", "Mainstream Zone"]:
            if z in zones:
                parts.append(f"{z}: {zones[z]}")
        print(" | ".join(parts))


def print_product_analysis(results):
    print_header("PRODUCT DRIFT ANALYSIS")

    by_product = {}
    for r in results:
        by_product.setdefault(r["product"], []).append(r)

    for product, entries in sorted(by_product.items()):
        avg = sum(e["lds_score"] for e in entries) / len(entries)
        variant_confirmed = sum(1 for e in entries if e["product_variant_evidence"])
        high_disparity = sum(1 for e in entries if e["lds_score"] > 2.0)

        print(f"\n  {product}")
        print(f"    Reports: {len(entries)}  |  Avg Score: {avg:.2f}")
        print(f"    Variant evidence: {variant_confirmed}/{len(entries)} "
              f"({variant_confirmed/len(entries)*100:.0f}%)")
        print(f"    Relief Zone hits: {high_disparity}")


def print_case_studies(results):
    print_header("CASE STUDIES — HIGHEST DISPARITY MEMORIES")

    sorted_results = sorted(results, key=lambda r: -r["lds_score"])

    for i, case in enumerate(sorted_results[:5], 1):
        print(f"\n  --- Case #{i} ---")
        print(f"  Region   : {case['region']}")
        print(f"  Product  : {case['product']}")
        print(f"  Variant  : \"{case['variant_seen']}\"")
        print(f"  Window   : {case['distribution_window']}")
        print(f"  Score    : {case['lds_score']}")
        print(f"  Zone     : {case['zone']}")
        print(f"  Factors  :")
        print(f"    Geography   : {case['geolocation_type']}")
        print(f"    Media       : {case['media_sync']}")
        print(f"    Era         : {case['capture_era']}")
        print(f"    Access      : {case['access_mode']}")
        print(f"    Evidence    : {'yes' if case['product_variant_evidence'] else 'no'}")
        print(f"    Community   : {'confirmed' if case['community_validation'] else 'unconfirmed'}")
        print(f"    Suppression : {'yes' if case['memory_suppression_pressure'] else 'no'}")
        print(f"    Ad match    : {'yes' if case['ad_match_consistency'] else 'no'}")
        print(f"    Central rec : {'yes' if case['central_record_match'] else 'no'}")


def print_key_insight(results):
    print_header("KEY INSIGHT")

    rural_tribal = [r for r in results
                    if r["geolocation_type"] in ("rural", "tribal")]
    urban_suburban = [r for r in results
                      if r["geolocation_type"] in ("urban", "suburban")]

    avg_rt = sum(r["lds_score"] for r in rural_tribal) / len(rural_tribal) if rural_tribal else 0
    avg_us = sum(r["lds_score"] for r in urban_suburban) / len(urban_suburban) if urban_suburban else 0

    relief_rt = sum(1 for r in rural_tribal if r["zone"] == "Relief Zone")
    relief_us = sum(1 for r in urban_suburban if r["zone"] == "Relief Zone")

    pct_rt = (relief_rt / len(rural_tribal) * 100) if rural_tribal else 0
    pct_us = (relief_us / len(urban_suburban) * 100) if urban_suburban else 0

    print(f"""
  Rural/Tribal populations (n={len(rural_tribal)}):
    Avg disparity score : {avg_rt:.2f}
    Relief Zone rate    : {relief_rt}/{len(rural_tribal)} ({pct_rt:.1f}%)

  Urban/Suburban populations (n={len(urban_suburban)}):
    Avg disparity score : {avg_us:.2f}
    Relief Zone rate    : {relief_us}/{len(urban_suburban)} ({pct_us:.1f}%)

  Disparity gap: {avg_rt - avg_us:.2f}x higher score in rural/tribal regions

  Conclusion: Divergent memories cluster where supply chains fragment.
  These aren't false memories — they're regionally valid experiences
  shaped by logistics, access inequality, and media desync.""")


def export_json(results, path="simulation-results.json"):
    with open(path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n  Full results exported to {path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    n = 50
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
        except ValueError:
            print(f"Usage: python {sys.argv[0]} [memories_per_region]")
            sys.exit(1)

    total = n * len(REGIONS)
    print(f"\nSimulating {total} memory reports across {len(REGIONS)} regions "
          f"({n} per region)...")

    results = run_simulation(n_per_region=n)

    print_zone_summary(results)
    print_regional_breakdown(results)
    print_product_analysis(results)
    print_case_studies(results)
    print_key_insight(results)
    export_json(results)

    print("\n" + "=" * 70)
    print("  Simulation complete.")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
