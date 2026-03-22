# CLAUDE.md

## Project Overview

**Logistic Disparity Sensor (LDS)** is a symbolic-cognitive framework for validating "Mandela Effect" memories by examining supply chain disparities. Rather than dismissing divergent memories as errors, it traces them to documented causes: uneven product distribution, media desynchronization, surplus stock routing, and rural/urban access inequality.

Core thesis: many "false memories" are regionally valid experiences caused by logistics — not mass delusion.

## Repository Structure

```
Logistics-Disparity-Sensor/
├── lds-scanner.py              # Core scoring algorithm (calculate_lds_score)
├── README.md                   # Project overview
├── memory.md                   # Research analysis document (626 lines)
├── LICENSE                     # MIT License
│
├── artifact-tracker/           # Upload & validate physical artifacts with SHA256 hashing
│   ├── readme.md
│   └── test.txt                # Setup instructions + sample JSON
│
├── drift-map/                  # Document regionally valid alternate realities
│   ├── drift-entry-form.py     # CLI-based memory entry wizard
│   ├── sample-entry.json       # Example drift memory entry
│   ├── drift-map-index-sample.json  # Index of known divergence clusters
│   └── schema.md               # Data entry schema definition
│
├── drift-monitor/              # Archive silent edits to public sources
│   ├── readme.md
│   └── sample-targets.txt      # URLs to monitor for changes
│
├── field-manual-export/        # Create printable/offline memory records
│   ├── exporter-sample.py      # Export utility
│   ├── readme.md
│   └── templates/
│       └── artifact-card-templates.md  # Jinja2 card template
│
├── mandela-proof/              # Memory submission & cross-validation web app
│   ├── memory-bank.json        # Stored memory entries
│   ├── memory-search.html      # Search interface
│   ├── memory-submit.html      # Submission form
│   ├── requirements.txt        # Python deps (Flask, Jinja2)
│   ├── readme.md
│   └── memory_bank/
│       └── memory-app.py       # Flask app (placeholder)
│
└── rural-artifact-network/     # Map divergence zones by supply chain
    ├── readme.md
    ├── product-lifecycle-table.csv  # Product variant reference data
    ├── heatmap-design.md        # Heatmap design doc
    └── tagging-interface.md     # Tagging interface design doc
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
| `lds-scanner.py` | Core LDS scoring algorithm — weighted calculation using geography, media exposure, era, access mode, evidence, and community validation |
| `drift-map/drift-entry-form.py` | CLI wizard for submitting drift memory entries |
| `field-manual-export/exporter-sample.py` | Generates printable artifact cards from JSON data |

## LDS Scoring Algorithm

The core algorithm in `lds-scanner.py` calculates a disparity score using weighted factors:

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
pip install -r mandela-proof/requirements.txt
```

### Running the Core Scanner

```bash
python lds-scanner.py
```

### No Build Step Required

The project runs directly as Python scripts — no compilation, bundling, or build process.

## Conventions

- **File naming**: kebab-case for all files and directories
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
- Maintain the weighted scoring approach in `lds-scanner.py`
- Follow existing snake_case naming conventions for Python code
- Use kebab-case for file and directory names
- Do not introduce heavy dependencies — the project values simplicity and accessibility
