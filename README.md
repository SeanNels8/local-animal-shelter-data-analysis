# Relational Data Pipeline Optimization: Database Archiving Engine

## Business Case & Objective
Non-profit organizations frequently face scaling costs associated with CRM and email marketing platforms (such as Mailchimp), where maintaining inactive records unnecessarily drives up monthly overhead. 

The goal of this project was to build a fail-safe data pipeline to isolate **archivable subscribers** based on complex operational parameters. This automated process prevents the accidental deletion or archiving of recent donors, active campaign targets, or crucial crisis supporters.

## Data Strategy & Architecture
Rather than relying on manual spreadsheet filtering, I engineered a rule-based decision engine in **Python (Pandas)** that dynamically cross-references relational tables:
1. **Subscriber Interaction Logs:** Aggregated metrics tracking user click/open historical behaviors.
2. **Dynamic Campaign Tag Matrix:** Mapping internal non-profit organizational tags (e.g., event attendees, fosters) to strict retention protocols.

### Pipeline Logic Flow
- **Cross-Reference Isolation (`HowManyLEIDsInBothCSVs.py`):** Leverages Python `set` intersections to identify and isolate unique user IDs (`LEID`) with conflicting status logs across system extractions.
- **Nested Tag Parsing & Prioritization (`ArchiveDB.py`):** Automatically splits and sanitizes irregular, double-quoted, comma-separated string vectors within database entries to identify high-value operational flags (safeguarding profiles with specific codes like emergency disaster or capital appeal tags).
- **Targeted Output Segmentation (`No-Yes-ArchiveCSVs.py`):** Automatically processes the transformed dataframes to export clean, execution-ready delivery buckets (`Safe_To_Archive_LEIDs.csv` and `Do_Not_Archive_LEIDs.csv`) for zero-risk system maintenance.

## Tech Stack
- **Languages:** Python 3.11
- **Libraries:** Pandas (Vectorized string filtering, tabular transformations)
- **Concepts:** Data Integrity Verification, Rule-Based Decision Architecture, Relational Mapping
