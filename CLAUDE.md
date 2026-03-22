# CLAUDE.md

## Project Overview

**Logistic Disparity Sensor (LDS)** is a symbolic-cognitive framework for validating "Mandela Effect" memories by examining supply chain disparities. Rather than dismissing divergent memories as errors, it traces them to documented causes: uneven product distribution, media desynchronization, surplus stock routing, and rural/urban access inequality.

Core thesis: many "false memories" are regionally valid experiences caused by logistics — not mass delusion.

## Repository Structure

```
Logistics-Disparity-Sensor/
├── lds_scanner.py              # Core scoring algorithm (calculate_lds_score)
├── README.md                   # Project overview
├── Memory.md                   # Research analysis document (626 lines)
├── LICENSE                     # MIT License
│
├── artifact_tracker/           # Upload & validate physical artifacts with SHA256 hashing
│   ├── Readme.md
│   └── Test.txt                # Setup instructions + sample JSON
│
├── drift_map/                  # Document regionally valid alternate realities
│   ├── drift_entry_form.py     # Flask-based memory entry form
│   ├── sample_entry.json       # Example drift memory entry
│   ├── drift_map_index.json    # Index of known divergence clusters
│   └── schema.md               # Data entry schema definition
│
├── drift_monitor/              # Archive silent edits to public sources
│   ├── Readme.md
│   └── sample_targets.txt      # URLs to monitor for changes
│
├── field_manual_export/        # Create printable/offline memory records
│   ├── exporter_sample.py      # Export utility
│   ├── Readme.md
│   └── templates/
│       └── artifact_card_templates.md  # Jinja2 card template
│
├── mandela_proof/              # Memory submission & cross-validation web app
│   ├── memory_app.py           # Flask app for memory submission
│   ├── memory_bank.json        # Stored memory entries
│   ├── requirements.txt        # Python deps (Flask, Jinja2)
│   ├── Readme.md
│   └── templates/
│       ├── memory_form.html    # Submission form
│       └── memory_search.html  # Search interface
│
└── rural_artifact_network/     # Map divergence zones by supply chain
    ├── Readme.md
    └── product_lifecycle_table.csv  # Product variant reference data
```

## Tech Stack

- **Language**: Python 3
- **Web Framework**: Flask + Jinja2
- **Database**: SQLite (lightweight, local)
- **Data Format**: JSON for artifact/memory storage
- **Frontend**: HTML/CSS (basic forms)
- **License**: MIT

## Key Files

| File | Purpose |
|------|---------|
| `lds_scanner.py` | Core LDS scoring algorithm — weighted calculation using geography, media exposure, era, access mode, evidence, and community validation |
| `drift_map/drift_entry_form.py` | Flask route for submitting drift memory entries |
| `mandela_proof/memory_app.py` | Flask web app for anonymous memory submission and search |
| `field_manual_export/exporter_sample.py` | Generates printable artifact cards from JSON data |

## LDS Scoring Algorithm

The core algorithm in `lds_scanner.py` calculates a disparity score using weighted factors:

- **Geographic weight**: rural (1.2), tribal (1.3), urban (0.9), suburban (0.8)
- **Media sync**: no_exposure (1.5), radio_only (1.2), mainstream (0.7)
- **Era bias**: pre_digital (1.4), catalog_era (1.3), smartphone_era (0.7)
- **Binary flags**: access_mode, variant_evidence, community_validation, suppression_pressure

**Score classifications**:
- `> 2.0` — Relief Zone
- `> 1.5` — Catalog/Variant Zone
- `> 1.1` — Localized Divergence Zone
- `<= 1.1` — Mainstream Zone

## Development Workflow

### Dependencies

```bash
pip install -r mandela_proof/requirements.txt
```

### Running the Core Scanner

```bash
python lds_scanner.py
```

### Running the Web App

```bash
cd mandela_proof
python memory_app.py
```

### No Build Step Required

The project runs directly as Python scripts — no compilation, bundling, or build process.

## Conventions

- **Python style**: snake_case for variables and functions
- **Data IDs**: `M####` for memories, `A####` for artifacts
- **JSON schema**: entries include geographic tags (region, state, ZIP), timeline data, and community validation counts
- **Offline-first**: all modules designed to work without internet; local JSON/SQLite storage
- **Modular architecture**: each subdirectory is an independent module that can function standalone
- **No formal test suite**: validation is done via sample data files and manual testing

## Architecture Notes

- Modules are loosely coupled — each can operate independently
- Data flows through JSON files, not shared databases
- Community validation is baked into the data model (confirmation counts, witness lists)
- The project emphasizes grassroots documentation without institutional gatekeeping
- Physical artifact preservation uses SHA256 hashing for integrity verification

## When Making Changes

- Preserve the offline-first, community-focused design philosophy
- Keep modules independent — avoid tight coupling between subdirectories
- Use JSON for data interchange between modules
- Maintain the weighted scoring approach in `lds_scanner.py`
- Follow existing snake_case naming conventions
- Do not introduce heavy dependencies — the project values simplicity and accessibility
