#  Module 1: Artifact Tracker

Part of the **MandelaProof Toolkit**, this module preserves physical memory artifacts and ties them to metadata — creating a trustworthy archive of divergent memories.

---

##  Purpose

Capture and validate artifacts like:
- 📸 Polaroids of packaging
- 📚 Books with unusual spellings
- 🧾 Labels, VHS tapes, scans
- 🔊 Audio/video clips

Attach:
- Memory description
- Witnesses
- Timestamps
- Integrity hash (SHA256)

---

##  Features

- Upload scanned artifact image
- Auto-generate SHA256 hash for integrity
- Input structured memory metadata
- Store in local SQLite DB
- Search and filter by memory, witness, year
- Export or print artifact records

---

##  File Structure

```bash
artifact_tracker/
├── app.py                 # Main Flask app
├── templates/
│   ├── index.html         # Upload form
│   └── search.html        # Artifact viewer
├── static/
│   └── style.css          # Stylesheet
├── db/
│   └── artifact_data.db   # SQLite data store
├── utils/
│   └── image_hasher.py    # Optional: externalize hash logic
├── requirements.txt
