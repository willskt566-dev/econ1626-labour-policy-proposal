# ECON1626 Assessment 2: AI and the Australian Labour Market

A policy brief advising the **Department of Employment and Workplace Relations (DEWR)** on how to manage generative AI's effects on Australian workers. It recommends a staged, trigger-based package costing about $440 million over four years.

**Author:** William Sia | RMIT University | ECON1626 Economics of AI | Semester 2, 2026

## Repository structure

```text
econ1626-labour-policy-proposal/
├── README.md                      project overview (this file)
├── proposal.md                    the policy brief
├── reflection.md                  AI use reflection
└── figures/
    ├── figure-1-exposure-gap.png  Figure 1 used in the brief
    └── make_figure_1.py           script that builds Figure 1
```

## Read the brief

| Section | What it covers |
|---|---|
| [Executive Summary](proposal.md#executive-summary) | The recommendation in one paragraph |
| [1. Problem Definition and Context](proposal.md#1-problem-definition-and-context) | How AI changes work: displacement, augmentation and reinstatement |
| [2. Analysis of Impacts](proposal.md#2-analysis-of-impacts) | Employment, tasks, wages, industry, and who bears the cost |
| [3. Policy Options and Evaluation](proposal.md#3-policy-options-and-evaluation) | Four options and the status quo, scored on five weighted criteria |
| [4. Recommended Package and Implementation Plan](proposal.md#4-recommended-package-and-implementation-plan) | Timeline, responsibilities, costs and KPIs |
| [5. Risks and Mitigations](proposal.md#5-risks-and-mitigations) | What could go wrong and how to manage it |
| [References](proposal.md#references) | RMIT Harvard style |

## Word count

| File | Words | Counting rule |
|---|---:|---|
| `proposal.md` | 1,309 | Includes headings, tables and in-text citations; excludes references |
| `reflection.md` | 202 | Reflection text only; excludes the AI acknowledgement and reference |
| **Total** | **1,511** | Brief: 1,200-word proposal plus 200-word reflection, 1,400 words ± 10% |

## Reproducing Figure 1

Run `python figures/make_figure_1.py` from the repository root (requires `matplotlib`). The data come from DEWR (2026), cited in the brief.

## Version history

The brief was built and committed section by section. Select **Commits** on the repository home page to see how it developed.

## AI use

Claude (Anthropic) was used to prepare this repository. [`reflection.md`](reflection.md) explains how, what was checked, and the limits of that use.
