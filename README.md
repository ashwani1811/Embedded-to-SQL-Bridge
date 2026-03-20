# 🚀 The Hardware-to-Data Bridge: IoT Telemetry System

In IoT, "Garbage In = Garbage Out." High-level analytics fail if the firmware doesn't provide clean, structured data. Drawing on **20 years of Embedded C expertise**, I built this bridge to demonstrate data integrity at the point of ingestion.

---

## 🛠 Project Workflow
To ensure a clean data environment, follow this execution order:
1. **Initialize:** Run `python db_setup.py` (This clears old data and creates fresh tables).
2. **Generate:** Choose **Method A** or **Method B** (see below) to populate data.
3. **Analyze:** Open `analysis_queries.sql` in VS Code to run SQL joins and filters.

---

## 📡 Methods of Operation

### Method A: Quick Start (Python Only)
*Best for testing SQL logic quickly.*
* **Command:** `python generate_data.py`
* **Result:** Inserts 100 simulated sensor rows directly into the database.

### Method B: Edge-to-Cloud Bridge (C + Python)
*Best for demonstrating real-world IoT architecture.*
* **Requirement:** GCC Compiler installed.
* **Command 1 (Compile):** `gcc sensor_emulator.c -o sensor_emulator`
* **Command 2 (Run):** `python bridge_ingestor.py`
* **Result:** A C-program emulates a live sensor node, piping real-time data into the SQL database via a Python gateway.

---

## 📋 Technical Highlights
- **Data Integrity:** Schema includes constraints to prevent "ghost" device entries.
- **Relational Mapping:** Demonstrates `INNER JOIN` and `LEFT JOIN` for predictive maintenance reporting.
- **Efficiency:** C-emulator uses minimal memory footprint, simulating resource-constrained environments.
