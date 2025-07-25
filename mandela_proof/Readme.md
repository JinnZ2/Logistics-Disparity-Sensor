#  Memory Bank + Cross-Validation

**Purpose:**  
Allow users to log subjective memories (even without physical proof) and cross-validate them anonymously. Detect mass drift vs isolated memory events, and provide classification context for pattern research.

---

##  Core Features

###  1. Memory Submission
- Freeform memory entry
- Optional: region, timeframe, source
- Tag with memory category (spelling, quote, logo, etc)

###  2. Cross-Validation
- Search memory logs
- Confirm matches anonymously
- Contribute new versions or regions
- Auto-calculates "shared memory confidence"

###  3. Drift Origin Tagging
Tag possible origin:
-  Misprint
-  Legal rename
-  Online overwrite
-  Schema bias
-  Unknown anomaly

---

## Example Record (JSON)

```json
{
  "id": "M0034",
  "memory_text": "Oscar Mayer was spelled 'Meyer' in the commercials I saw.",
  "category": "Brand spelling",
  "date_range": "1985–1992",
  "region": "Northern Wisconsin",
  "source": "TV ad, sandwich packaging",
  "confirmation_count": 11,
  "origin_suspect": "Misprint or jingle auditory bias",
  "last_confirmed": "2025-07-19"
}
