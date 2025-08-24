#!/usr/bin/env python3
"""Run analysis and save figures to ./figures."""
from pathlib import Path
import matplotlib.pyplot as plt

fig_dir = Path("figures")
fig_dir.mkdir(parents=True, exist_ok=True)

plt.plot([2015, 2020, 2025], [10, 35, 60])
plt.xlabel("Year"); plt.ylabel("USD (bn)")
plt.title("Placeholder: Pledges over time")
plt.tight_layout()
plt.savefig(fig_dir / "placeholder_gap.png", dpi=150)
print("02_analyze.py: wrote figures/placeholder_gap.png")
