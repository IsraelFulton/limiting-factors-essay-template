#!/usr/bin/env python3
"""Transform raw data into analysis-ready tables.
Write results to ./data/processed.
"""
from pathlib import Path
proc = Path("data/processed")
proc.mkdir(parents=True, exist_ok=True)
(proc / "table.parquet").write_bytes(b"")  # placeholder
print("01_clean.py: wrote placeholder data/processed/table.parquet")
