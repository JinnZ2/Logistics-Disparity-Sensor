#  Reality Drift Monitor

Track silent changes to public "truth" sources over time.

---

##  Purpose

Detect, archive, and compare silent edits made to:

-  Wikipedia articles
-  News outlets
-  Brand/product pages
-  Publishing records
-  Google Knowledge Panels

---

##  Core Features

###  1. Target List
- Add URLs or keyword-triggered queries to `targets.txt`

###  2. Auto Scraper
- Fetches and stores target pages at regular intervals (daily/weekly)

###  3. Difference Engine
- Compares last 2 versions of a page
- Highlights insertions, deletions, or edits

###  4. Archive + Log
- Saves:
  - timestamped `.html` pages
  - `.txt` diffs
  - optional screenshots (future)

###  5. Optional GUI Dashboard
- Search history by domain or term
- See what changed and when
- Flag stealth edits (no visible change tags)

---

##  File Overview

```bash
drift_monitor.py      # Main runner script
targets.txt           # List of URLs or queries
diffs/                # Text change diffs
archive/              # Raw HTML snapshots
logs/                 # Optional logs or timestamps
utils/diff_engine.py  # Basic diff generator
dashboard.py          # Optional: GUI view
