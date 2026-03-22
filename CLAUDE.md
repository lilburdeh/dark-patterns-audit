# Dark Patterns Audit Tool

This project is a dark patterns audit tool built for the Behavioural Insights Team (Singapore). It uses the Gray et al. (2024) CHI Dark Patterns Ontology (65 patterns, 3 levels) to systematically analyze websites and interfaces for deceptive design.

## Usage

1. Drop a screenshot, paste a URL, or provide a code snippet
2. Type `/audit`
3. The audit report is saved to `reports/`

## Project Structure

- `.claude/skills/dark-pattern-audit/` — The audit skill
- `.claude/skills/dark-pattern-audit/references/gray-ontology.md` — Full 65-pattern framework reference
- `.claude/skills/dark-pattern-audit/references/report-template.md` — Report template
- `reports/` — Generated audit reports
