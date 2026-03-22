# Dark Patterns Audit Report Template

Use this template structure when generating audit reports.

---

```markdown
# Dark Patterns Audit Report

## Audit Metadata

| Field | Value |
|-------|-------|
| **Date** | [YYYY-MM-DD] |
| **Source** | [Screenshot / URL / Code snippet] |
| **Source Description** | [Brief description of what was analyzed, e.g., "Booking.com hotel listing page"] |
| **Framework** | Gray et al. (2024) Dark Patterns Ontology (CHI '24) |
| **Analyst** | [Analyst name or "Automated — Claude"] |

---

## Executive Summary

**Total findings:** [N]
| Severity | Count |
|----------|-------|
| High | [n] |
| Medium | [n] |
| Low | [n] |

**Top concerns:**
- [One-sentence summary of the most significant finding]
- [One-sentence summary of the second most significant finding]
- [One-sentence summary of the third most significant finding, if applicable]

---

## Findings Overview

| # | Pattern Name | Level | Parent Category | Severity | Brief Description |
|---|-------------|-------|-----------------|----------|-------------------|
| 1 | [e.g., Countdown Timer] | Low | Social Engineering > Urgency | High | [One-line evidence summary] |
| 2 | [e.g., False Hierarchy] | Low | Interface Interference > Manipulating Choice Architecture | Medium | [One-line evidence summary] |
| ... | ... | ... | ... | ... | ... |

---

## Detailed Findings

### Finding 1: [Pattern Name]

| Field | Value |
|-------|-------|
| **Ontology Classification** | [High-Level] > [Meso-Level] > [Low-Level] |
| **Severity** | [High / Medium / Low] |

**Evidence:**
[Describe exactly what was observed in the screenshot, code, or page. Be specific — reference visual elements, text content, placement, colors, sizes. If from a screenshot, describe the location in the image.]

**Why this is a dark pattern:**
[Explain how this meets the pattern definition. What user harm does it cause? What cognitive bias or vulnerability does it exploit?]

**Recommendation:**
[Specific, actionable suggestion for how to fix or mitigate this pattern.]

---

[Repeat "### Finding N" for each finding]

---

## Patterns Not Detected

The following high-level categories were checked and no instances were found:

- [ ] **Obstruction** — [Checked / Not applicable]
- [ ] **Sneaking** — [Checked / Not applicable]
- [ ] **Interface Interference** — [Checked / Not applicable]
- [ ] **Forced Action** — [Checked / Not applicable]
- [ ] **Social Engineering** — [Checked / Not applicable]

---

## Methodology

This audit was conducted using the Gray et al. (2024) Dark Patterns Ontology, a three-level taxonomy of 65 dark pattern types synthesized from 10 academic and regulatory sources. The ontology was published at ACM CHI 2024.

**Severity Rubric:**
- **High**: Actively deceptive or coercive. User is misled, financially harmed, or unable to exercise meaningful choice. Examples: hidden charges, impossible cancellation, fake urgency with fabricated timers.
- **Medium**: Manipulative but does not actively hide information. Steers user decisions through psychological pressure or interface design. Examples: confirmshaming, false hierarchy, pressured selling.
- **Low**: Nudge-like or borderline. May not cause direct harm but creates friction or mild pressure. Examples: nagging, bad defaults that are easy to change, mild framing effects.

**Scope:** [Static screenshot analysis / Interactive flow analysis / Code review]

**Limitations:** [Note any limitations, e.g., "Only one page was analyzed; multi-step flows were not tested" or "Screenshot quality limited analysis of small text"]
```
