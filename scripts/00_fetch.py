#!/usr/bin/env python3
"""Download or load source data.

Replace this placeholder with real downloads. Keep raw files in ./data/raw.
"""
from pathlib import Path
raw = Path("data/raw")
raw.mkdir(parents=True, exist_ok=True)
print("00_fetch.py: (placeholder) ensured data/raw exists.")
