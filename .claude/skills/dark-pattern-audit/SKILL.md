---
name: audit
description: This skill should be used when the user asks to "audit", "review for dark patterns", "check for deceptive design", "analyze this for dark patterns", drops a screenshot for dark pattern analysis, or pastes a URL or code snippet and asks for a dark pattern review. Performs a structured dark patterns audit using the Gray et al. CHI 2024 ontology.
version: 0.1.0
---

# Dark Patterns Audit

Perform a systematic dark patterns audit on the provided input using the Gray et al. (2024) Dark Patterns Ontology.

## Step 1: Identify the Input Type

Determine what the user has provided:

- **Screenshot/Image**: The user has dropped or pasted an image file. Analyze visually.
- **URL**: The user has provided a web link. Navigate to it using browser tools, take a screenshot, then analyze.
- **Code snippet**: The user has pasted HTML, CSS, or JavaScript. Analyze the code for dark pattern implementations.

If no input is provided alongside `/audit`, ask the user: "Please provide a screenshot, URL, or code snippet to audit."

## Step 2: Load the Framework

Read the full ontology reference at `references/gray-ontology.md` in this skill's directory. This contains all 65 dark pattern types across 3 levels with definitions and detection indicators.

## Step 3: Systematic Analysis

Work through each of the 5 high-level categories methodically. For each category, check every meso-level and low-level pattern against the input. Do not skip categories.

### 3a. OBSTRUCTION
Check for: Roach Motel patterns (immortal accounts, dead ends), Creating Barriers (price comparison prevention, intermediate currency), Adding Steps (privacy maze).

### 3b. SNEAKING
Check for: Bait and Switch (disguised ads), Hiding Information (sneak into basket, drip pricing/hidden costs, reference pricing), (De)contextualizing Cues (conflicting information, information without context).

### 3c. INTERFACE INTERFERENCE
Check for: Manipulating Choice Architecture (false hierarchy, visual prominence, bundling, pressured selling), Bad Defaults, Emotional or Sensory Manipulation (cuteness, positive/negative framing), Trick Questions, Choice Overload, Hidden Information, Language Inaccessibility (wrong language, complex language), Feedforward Ambiguity.

### 3d. FORCED ACTION
Check for: Nagging, Forced Continuity, Forced Registration, Forced Communication or Disclosure (privacy zuckering, friend spam, address book leeching, social pyramid), Gamification (pay-to-play, grinding), Attention Capture (auto-play).

### 3e. SOCIAL ENGINEERING
Check for: Scarcity and Popularity Claims (high demand), Social Proof (low stock, endorsements and testimonials, parasocial pressure), Urgency (activity messages, countdown timer, limited time message), Shaming (confirmshaming), Personalization.

## Step 4: Assign Severity

For each finding, assign a severity level:

- **High**: Actively deceptive or coercive. The user is misled, financially harmed, or unable to exercise meaningful choice. The pattern exploits a cognitive vulnerability in a way that most users would not detect. Examples: hidden charges added silently, impossible account deletion, fabricated countdown timers, auto-opted-in paid services.

- **Medium**: Manipulative but does not actively deceive. Steers user decisions through psychological pressure, visual design, or friction. An attentive user could recognize and overcome it. Examples: confirmshaming, false hierarchy between buttons, pressured selling during checkout, bad defaults on marketing consent.

- **Low**: Nudge-like or borderline. Creates mild friction or pressure but does not cause direct financial or privacy harm. May be a common industry practice that is still worth flagging. Examples: nagging notifications, mild positive framing, choice overload in settings.

## Step 5: Generate the Report

Read the report template at `references/report-template.md` in this skill's directory.

Generate a complete audit report following that template structure. Fill in all sections:

1. **Audit Metadata** — date, source type, source description, framework, analyst
2. **Executive Summary** — total findings, severity breakdown, top concerns
3. **Findings Overview** — summary table of all findings
4. **Detailed Findings** — one section per finding with evidence, explanation, and recommendation
5. **Patterns Not Detected** — confirm which categories were checked and found clean
6. **Methodology** — framework citation, severity rubric, scope, limitations

Save the report to the `reports/` directory in the project root with the filename format:
`reports/audit-[source-description]-[YYYY-MM-DD].md`

For example: `reports/audit-booking-com-hotel-page-2026-03-17.md`

## Important Guidelines

- **Be specific with evidence.** Describe exactly what you see — text content, button labels, colors, sizes, placement. Vague descriptions like "the page uses dark patterns" are not useful.
- **Quote UI text exactly.** When referencing button labels, messages, or copy, quote them verbatim.
- **Don't over-flag.** Not every design choice is a dark pattern. Only flag patterns where there is clear evidence of manipulation, deception, or coercion. Common UX conventions (e.g., a prominent CTA button) are not inherently dark patterns unless combined with other manipulative elements.
- **Note uncertainty.** If a pattern might be present but you cannot confirm from the available input (e.g., you can see a "sale" price but cannot verify if the original price is genuine), note it as "Possible" and explain what additional information would be needed.
- **Consider context.** A countdown timer on a live auction is legitimate; a countdown timer on an always-available product is deceptive. Context matters.
