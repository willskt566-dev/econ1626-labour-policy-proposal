"""Builds Figure 1 for proposal.md from DEWR (2026) published figures."""
import matplotlib.pyplot as plt

labels = ["Employment growth,\nNov 2022 to Feb 2026", "Share of workers\nwith tertiary qualifications"]
most_exposed = [5.6, 43.7]
least_exposed = [9.5, 14.9]

fig, ax = plt.subplots(figsize=(8, 4.5), dpi=150)
x = range(len(labels))
w = 0.36
b1 = ax.bar([i - w / 2 for i in x], most_exposed, w, label="Most-exposed fifth of occupations", color="#1f4e79")
b2 = ax.bar([i + w / 2 for i in x], least_exposed, w, label="Least-exposed fifth of occupations", color="#9dc3e6")
ax.bar_label(b1, fmt="%.1f%%", padding=3, fontsize=10)
ax.bar_label(b2, fmt="%.1f%%", padding=3, fontsize=10)
ax.set_xticks(list(x))
ax.set_xticklabels(labels, fontsize=10)
ax.set_ylabel("Per cent")
ax.set_ylim(0, 52)
ax.spines[["top", "right"]].set_visible(False)
ax.legend(frameon=False, fontsize=9, loc="upper left")
ax.set_title("AI-exposed jobs are growing more slowly and employ more graduates", fontsize=12, loc="left")
fig.text(0.01, 0.01, "Source: DEWR (2026), using JSA exposure scores and ABS Labour Force data.", fontsize=8, color="#555555")
fig.tight_layout(rect=(0, 0.04, 1, 1))
fig.savefig("figures/figure-1-exposure-gap.png")
