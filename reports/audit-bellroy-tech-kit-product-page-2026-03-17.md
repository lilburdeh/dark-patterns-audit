# Dark Patterns Audit Report

## Audit Metadata

| Field | Value |
|-------|-------|
| **Date** | 2026-03-17 |
| **Source** | Screenshot |
| **Source Description** | E-commerce product page for "Bellroy Tech Kit" (SGD$89.00) on an unidentified Singapore-based online retailer |
| **Framework** | Gray et al. (2024) Dark Patterns Ontology (CHI '24) |
| **Analyst** | Automated — Claude |

---

## Executive Summary

**Total findings:** 4

| Severity | Count |
|----------|-------|
| High | 1 |
| Medium | 2 |
| Low | 1 |

**Top concerns:**
- A low stock warning ("Hurry! Only 2 Left in Stock!") with a visual depletion bar creates artificial scarcity pressure — the claim is unverifiable and the visual bar amplifies the urgency beyond the text alone.
- A real-time viewer count ("11 people are looking at this product right now") fabricates social pressure to create fear of missing out.
- The word "Hurry!" and exclamation-heavy copy create urgency framing that pressures users to act before reflecting on their purchase decision.

---

## Findings Overview

| # | Pattern Name | Level | Parent Category | Severity | Brief Description |
|---|-------------|-------|-----------------|----------|-------------------|
| 1 | Low Stock | Low | Social Engineering > Social Proof | High | "Hurry! Only 2 Left in Stock!" with a visual depletion progress bar |
| 2 | High Demand | Low | Social Engineering > Scarcity and Popularity Claims | Medium | "11 people are looking at this product right now" |
| 3 | Positive or Negative Framing | Low | Interface Interference > Emotional or Sensory Manipulation | Medium | Urgency language ("Hurry!") and exclamation marks pressure the user emotionally |
| 4 | Information without Context | Low | Sneaking > (De)contextualizing Cues | Low | Viewer count and stock level presented as fact with no verifiable source or context |

---

## Detailed Findings

### Finding 1: Low Stock

| Field | Value |
|-------|-------|
| **Ontology Classification** | Social Engineering > Social Proof > Low Stock |
| **Severity** | **High** |

**Evidence:**
Below the colour selector, the page displays the text "Hurry! Only 2 Left in Stock!" in bold, with the number "2" highlighted in a distinct colour (red/orange). Directly beneath this text is a horizontal progress bar that is nearly fully depleted (approximately 90% empty), visually reinforcing that stock is almost gone. The bar uses a dark fill on the left and an empty grey track on the right.

**Why this is a dark pattern:**
This is a textbook Low Stock pattern. The combination of an explicit low-stock number with a visual depletion bar exploits loss aversion — the fear of missing out on a scarce resource. The progress bar is particularly manipulative because it adds a visceral, at-a-glance signal of scarcity that amplifies the text message. There is no way for the user to verify whether "2 left" is accurate, whether the bar reflects real inventory data, or whether these numbers reset. Notably, the page simultaneously displays "In stock" as a green badge at the top, which somewhat contradicts the urgency of "only 2 left." This is rated High severity because the visual depletion bar goes beyond a simple stock count — it is a designed artefact whose sole purpose is to pressure the purchase decision.

**Recommendation:**
If stock data is genuine, display it factually without urgency language or visual amplification (e.g., "2 units available" in neutral styling). Remove the depletion progress bar entirely — it serves no informational purpose beyond creating pressure. If stock data is not real-time or accurate, remove the claim altogether.

---

### Finding 2: High Demand

| Field | Value |
|-------|-------|
| **Ontology Classification** | Social Engineering > Scarcity and Popularity Claims > High Demand |
| **Severity** | **Medium** |

**Evidence:**
Below the stock warning, the page displays "11 people are looking at this product right now" with the number "11" displayed in a dark highlighted badge/box. This is presented as a real-time count of concurrent viewers.

**Why this is a dark pattern:**
This is a High Demand pattern that exploits social proof and competitive anxiety. By telling the user that 10 other people are viewing the same product — combined with the "only 2 left" message above — it creates a fear that someone else will purchase the item before them. The user has no way to verify whether this number is real, updated in real-time, or fabricated. Even if the number is technically accurate, presenting it in this context is designed to create competitive urgency rather than to inform. The combination with the Low Stock message above creates a compounding pressure effect: scarce supply + high demand = "buy now or lose it."

**Recommendation:**
Remove the real-time viewer count. It does not help the user make a better purchasing decision — it only creates social pressure. If the retailer wants to indicate product popularity, a less manipulative approach would be aggregate data like "popular item" or total units sold, which does not create the same real-time competitive pressure.

---

### Finding 3: Positive or Negative Framing

| Field | Value |
|-------|-------|
| **Ontology Classification** | Interface Interference > Emotional or Sensory Manipulation > Positive or Negative Framing |
| **Severity** | **Medium** |

**Evidence:**
The word "Hurry!" opens the low-stock message, using imperative, urgent language that directly commands the user to act quickly. The delivery and guarantee section also uses exclamation marks throughout ("Delivery within 7 working days!", "Free shipping on orders above $80."). While the delivery information is factual, the consistent use of exclamation marks across the page creates an overall tone of excitement and urgency.

**Why this is a dark pattern:**
The imperative "Hurry!" is a framing device — it reframes a purchase decision (which should be deliberate) as a time-critical action. This exploits the affect heuristic, where emotional arousal (anxiety about missing out) overrides rational evaluation. The word "Hurry" does not convey any factual information — it is purely an emotional nudge. Combined with the scarcity and demand indicators, it forms part of a coordinated pressure system.

**Recommendation:**
Remove the word "Hurry!" from the stock indicator. Present stock levels, if genuine, as neutral factual information. Reserve exclamation marks for genuinely exciting offers rather than using them to create a general tone of urgency.

---

### Finding 4: Information without Context

| Field | Value |
|-------|-------|
| **Ontology Classification** | Sneaking > (De)contextualizing Cues > Information without Context |
| **Severity** | **Low** |

**Evidence:**
Both the stock count ("Only 2 Left in Stock!") and the viewer count ("11 people are looking at this product right now") are presented as factual claims without any context about their source, accuracy, or methodology. There is no indication of whether the stock number reflects warehouse inventory, local availability, or a specific variant. The viewer count does not explain what "looking at" means (page views? active sessions? unique users?), how it is measured, or how frequently it updates.

**Why this is a dark pattern:**
Presenting unverifiable data points as facts exploits the user's trust in the interface. Users tend to take displayed numbers at face value, especially when presented with visual design treatments (badges, progress bars) that signal authority. Without context, the user cannot assess the reliability of these claims, which is the prerequisite for making an informed decision.

**Recommendation:**
If these metrics are displayed, provide context: specify what "in stock" refers to (e.g., "2 available at our warehouse"), and clarify what the viewer count measures. Ideally, link to a methodology note or simply remove unverifiable real-time claims.

---

## Patterns Not Detected

The following high-level categories were checked and no instances were found:

- [x] **Obstruction** — Checked. No evidence of Roach Motel, Creating Barriers, or Adding Steps patterns visible on this product page. (Note: account/cancellation flows could not be assessed from a single product page screenshot.)
- [x] **Sneaking** — Checked. No evidence of Bait and Switch, Sneak into Basket, Drip Pricing, or Disguised Ads. Price is displayed clearly as SGD$89.00. Free shipping threshold is stated upfront ("Free shipping on orders above $80"). One finding under (De)contextualizing Cues (Finding 4).
- [x] **Interface Interference** — Checked. The "ADD TO CART" button is large and black, which is prominent — but this is a standard e-commerce convention and not manipulative in isolation. No evidence of Bad Defaults, Trick Questions, Choice Overload, Hidden Information, Language Inaccessibility, or Feedforward Ambiguity. One finding under Emotional or Sensory Manipulation (Finding 3).
- [x] **Forced Action** — Checked. No evidence of Nagging, Forced Continuity, Forced Registration, Forced Communication, Gamification, or Attention Capture visible on this page.
- [x] **Social Engineering** — Three findings identified (Findings 1, 2, 4). No evidence of Urgency via Countdown Timers, Confirmshaming, or Personalization.

---

## Methodology

This audit was conducted using the Gray et al. (2024) Dark Patterns Ontology, a three-level taxonomy of 65 dark pattern types synthesized from 10 academic and regulatory sources. The ontology was published at ACM CHI 2024.

**Severity Rubric:**
- **High**: Actively deceptive or coercive. User is misled, financially harmed, or unable to exercise meaningful choice. Examples: hidden charges, impossible cancellation, fake urgency with fabricated timers.
- **Medium**: Manipulative but does not actively hide information. Steers user decisions through psychological pressure or interface design. Examples: confirmshaming, false hierarchy, pressured selling.
- **Low**: Nudge-like or borderline. May not cause direct harm but creates friction or mild pressure. Examples: nagging, bad defaults that are easy to change, mild framing effects.

**Scope:** Static screenshot analysis of a single product page.

**Limitations:**
- Only one page was analyzed — multi-step flows (checkout, account creation, cancellation) were not tested and may contain additional dark patterns.
- The screenshot does not show the full page; patterns above or below the visible area may exist.
- It is not possible to verify from a static screenshot whether the stock count or viewer count is accurate, dynamic, or fabricated.
- Cookie consent, privacy settings, and account-related flows could not be assessed.
- No interaction was performed, so patterns that only appear on hover, click, or scroll could not be detected.
