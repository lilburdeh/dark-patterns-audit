# Dark Patterns Audit Tool — Product Requirements Document

**Owner:** Sai Ming, Senior Advisor, Behavioural Insights Team (BIT)
**Status:** Draft v0.4
**Last updated:** 19 March 2026
**Target ship date:** 30 April 2026

---

# Part A: Business Requirements

---

## 1. What is it?

A web application that systematically analyses websites and digital interfaces for deceptive design ("dark patterns"). Users upload a screenshot or provide a URL, and the tool produces a structured audit report classifying every detected pattern against the **Gray et al. (2024) CHI Ontology** — the most comprehensive academically validated framework of deceptive design patterns, covering 65 patterns organised across 3 hierarchical levels:

- **5 high-level strategies** (e.g., Obstruction, Sneaking)
- **25 meso-level angles** (e.g., Price Comparison Prevention, Hidden Costs)
- **35 low-level patterns** (e.g., Drip Pricing, Bait and Switch)

Built for the Behavioural Insights Team (BIT) to support evidence-based policy work on consumer protection in digital services. Designed to be the first tool that operationalises the full Gray et al. ontology into regulator-ready audit reports — combining BIT's behavioural science expertise with AI-assisted analysis.

---

## 2. Problem

Dark patterns are pervasive across e-commerce, SaaS, and consumer apps — hidden fees, fake urgency timers, manipulative opt-out flows, confirmshaming. These patterns exploit cognitive biases to extract money, data, or attention from users who don't realise they're being manipulated.

While awareness of dark patterns has grown and some detection tools now exist (see Section 4: Competitive Landscape), significant gaps remain:

- **No tool uses the most comprehensive taxonomy.** Existing tools use proprietary or older frameworks. The Gray et al. (2024) CHI Ontology — the most complete academic taxonomy of deceptive design (65 patterns) — has not been operationalised into any tool.
- **Existing tools are built for compliance buyers, not regulators.** Commercial offerings like Fair Patterns target businesses wanting to self-audit. Regulators and policymakers need different outputs: methodology-transparent reports that can support enforcement actions, evidence citations, and cross-case comparison.
- **No standardised severity framework tied to behavioural harm.** Existing tools flag patterns but don't consistently link severity to the behavioural mechanisms being exploited — the cognitive biases, friction costs, and welfare harms that matter for policy decisions.
- **Reports vary wildly in structure and depth**, making cross-audit comparison difficult across cases, jurisdictions, and time.
- **Time cost remains high.** A thorough manual audit of a single page against the full ontology takes 30–60 minutes of expert time. AI-assisted tools can reduce this to under 3 minutes.

---

## 3. Why now?

- **Regulatory momentum is accelerating.** The EU Digital Services Act, FTC enforcement actions, Italy's €98.6M penalty against Apple over ATT dark patterns, South Korea's new self-regulatory dark pattern code, and consumer protection reviews globally are increasing scrutiny. Regulators need rigorous, repeatable methodology — not just awareness.
- **The academic grounding has matured.** Gray et al.'s 2024 CHI paper provides the most comprehensive dark pattern taxonomy to date, but no tool applies it systematically. The window to be first is open.
- **Existing tools leave the public sector underserved.** Current commercial offerings (Fair Patterns, various browser extensions) are designed for B2B compliance. There is no tool purpose-built for the regulator and policymaker workflow: enforcement evidence, educational demonstrations, and cross-jurisdiction benchmarking.
- **BIT is uniquely positioned.** BIT has the behavioural science credibility, the government relationships, and the policy expertise to bridge the gap between academic taxonomy and regulator-ready tooling. No pure technology company or academic lab has this combination.

---

## 4. Competitive landscape

### 4.1 Existing tools

| Tool | Type | Coverage | Target user | Key limitation for our use case |
|---|---|---|---|---|
| **Fair Patterns / FairAudit Pro** | Commercial SaaS | Proprietary framework, 70+ checks per screen | Businesses, compliance teams | Proprietary taxonomy (not academically cited). B2B positioning. Reports designed for corporate compliance, not regulatory enforcement. |
| **UIGuard** | Academic research tool (UIST 2023) | 14 dark pattern types, mobile only | Researchers | Limited to mobile UIs. Covers only 14 of 65 known pattern types. Not a usable product — a research prototype. |
| **AppRay** | Academic research tool (2024) | Extends UIGuard with LLM-powered app exploration | Researchers | Mobile-only. Academic prototype, not deployed for end-user use. |
| **Dapde** | Academic project + browser extension | Text-based detection via browser extension | Consumers, researchers | Real-time consumer tool, not an audit/reporting tool. Limited pattern coverage. |
| **Dark Pattern Detector** (Chrome) | Browser extension | Text scanning via TinyBERT | Consumers | Lightweight consumer tool. No structured reporting. No comprehensive taxonomy. |

### 4.2 Our differentiation

1. **First tool to operationalise the Gray et al. (2024) CHI Ontology.** The most comprehensive academic taxonomy of deceptive design — 65 patterns across 3 hierarchical levels. No existing tool uses it. This gives every audit report an academically citable methodology, which matters for regulatory credibility.

2. **Built for the public sector.** Reports are designed for enforcement workflows: methodology transparency, full-coverage documentation (including what was checked and found clean), severity justifications linked to behavioural harm, and exportable formats ready for policy briefs and evidence packs.

3. **Behavioural science depth.** BIT's expertise means the tool doesn't just flag patterns — it explains *why* each pattern is deceptive in terms of the cognitive biases and behavioural mechanisms being exploited. This connects technical detection to the welfare harm arguments that regulators need to make.

4. **Consultancy-integrated.** The tool is not a standalone SaaS product — it's the entry point for BIT's broader advisory services on digital consumer protection (see Section 12: Strategic Vision). This is a fundamentally different go-to-market from Fair Patterns or browser extensions.

5. **Transparency and reproducibility.** Open methodology, versioned ontology, and deterministic analysis settings mean audits can be reproduced, compared across time, and scrutinised — essential for any tool whose outputs may feature in enforcement proceedings.

---

## 5. Audience

### Primary: Regulators and policymakers

- Use audit reports as evidence in enforcement actions and guidance documents
- Need consistent methodology citations and severity classifications
- Need an accessible tool that doesn't require technical expertise
- May use for both targeted investigations and educational demonstrations

### Secondary: UX designers and product teams

- Self-audit products before launch
- Need actionable recommendations, not just pattern identification

### Tertiary: BIT consultants (internal)

- Use as a standardised starting point for client-facing dark patterns work
- Reduce manual audit time on engagements

---

## 6. Success metrics

| Metric | Target |
|---|---|
| **Coverage** | Tool checks all 5 high-level categories and documents which were audited (even if clean) in every report |
| **Precision** | <10% false positive rate — flagged patterns are genuine dark patterns, not standard UX conventions |
| **Consistency** | Two runs on the same input produce substantially the same findings |
| **Time to audit** | Single-page audit completes in under 3 minutes end-to-end |
| **Report usability** | Reports are structured, exportable (PDF/markdown), and ready for stakeholder consumption without reformatting |
| **Regulator showcase** | Demonstrate to at least one regulator or relevant organisation and receive positive feedback on utility |
| **Pipeline generation** | Tool demo leads to at least one consultancy engagement enquiry within 3 months of launch |

---

## 7. User experience

### 7.1 Input

Users provide one of:

- **Screenshot upload** — drag-and-drop or file picker
- **URL** — pasted into a text input; the app captures and analyses the page

### 7.2 Output

A web-rendered audit report containing:

- **Executive summary** — finding count, severity breakdown, overall risk assessment
- **Findings table** — sortable/filterable, with pattern name, ontology path, severity, and evidence summary
- **Detailed findings** — expandable cards per finding with ontology classification, evidence, behavioural harm analysis, severity justification, and recommended fix
- **Patterns not detected** — confirms full-coverage audit, listing categories checked and confirmed clean
- **Methodology** — framework citation, severity rubric, model details, limitations disclaimer
- **Export** — PDF and markdown download

### 7.3 Severity rubric

| Level | Definition | Examples |
|---|---|---|
| **High** | Actively deceptive or coercive. User is misled, financially harmed, or unable to exercise free choice. | Hidden charges, fabricated countdown timers, forced continuity with no clear cancellation path |
| **Medium** | Manipulative but visible to attentive users. Creates friction or biases decisions without outright deception. | Confirmshaming copy, visual hierarchy that de-emphasises the "decline" option, pre-selected add-ons |
| **Low** | Nudge-like. Mild friction or framing effects without direct harm. | Nagging notifications, mild scarcity language ("only a few left"), aesthetic manipulation |

---

## 8. Experiment plan

### Phase 1: Calibration testing (Week 2)

- Run audits on 10 known-deceptive pages (e-commerce checkouts, subscription services, cookie consent banners, app permission screens) and 5 "clean" pages (government services, well-designed SaaS).
- Validate: Are findings accurate? Are clean pages reported clean? Is severity calibration reasonable?
- Log false positive and false negative rates.
- Refine prompt, ontology indicators, and severity rubric based on results.

### Phase 2: Expert benchmarking (Week 3)

- 2–3 BIT analysts independently audit 5 pages manually using the same ontology.
- Compare human audits against tool output for agreement on: patterns detected, severity assigned, evidence cited.
- Measure inter-rater reliability between tool and humans.
- Identify systematic biases (e.g., model over-flags visual hierarchy issues).

### Phase 3: Regulator showcase (Week 5–6)

- Demonstrate the tool to a target regulator or organisation (e.g., UK CMA, ICO, Forbrukerrådet, PDPC, European Commission DG Justice).
- Collect feedback on: report usefulness, credibility, fit for enforcement/education workflows.
- Iterate on report format and analysis depth based on feedback.

---

## 9. Timeline

**Deadline: 30 April 2026**

| Week | Dates | Build | Test |
|---|---|---|---|
| **1** | 23–29 Mar | Streamlit app scaffold. File upload + URL input. Report display with markdown rendering. Wire analysis to Claude API. Basic severity badges and findings layout. Construct `ontology.json` from Gray et al. paper. | Manually test 3 known-deceptive pages end-to-end. Verify screenshot upload and URL input both produce structured reports. Confirm report matches ontology template. |
| **2** | 30 Mar – 5 Apr | Report polish and export. PDF/markdown download buttons. Findings table with sortable dataframes. Severity breakdown chart. Annotated evidence display. | Run calibration suite: 10 deceptive + 5 clean pages. Log false positive/negative rates. Tune prompt and severity rubric. |
| **3** | 6–12 Apr | Audit history (session-based or file-backed). Side-by-side comparison for re-audits. Shareable link via Streamlit Cloud. | Expert benchmarking: 2–3 BIT analysts audit 5 pages manually, compare against tool. Measure agreement. |
| **4** | 13–19 Apr | UX refinement and edge cases. Multi-page flow handling. Error handling for failed URL captures. Polish for regulator laptop/tablet use. Deploy to Streamlit Cloud. | Internal BIT dogfooding — consultants use the tool for 1 week on real work. Collect structured feedback. |
| **5** | 20–26 Apr | Address dogfooding feedback. Performance optimisation. Onboarding sidebar and help docs. Prepare demo materials. | Regulator pilot: share Streamlit Cloud link with 2–3 target contacts. Collect feedback. |
| **6** | 27–30 Apr | Fix pilot feedback. Final QA. Polish. | End-to-end regression on calibration suite. Confirm exports. Final sign-off. |

---

## 10. Risks and mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **Model hallucinations** — Claude flags patterns that aren't there | Medium | High (credibility) | Calibration testing in Phase 1. Explicit prompt instructions to distinguish standard UX from dark patterns. Confidence notes field for uncertain findings. |
| **Ontology extraction errors** — patterns mis-transcribed from paper | Low | High | Cross-check against paper during construction. Version the ontology so errors can be corrected. |
| **URL screenshot capture fails** — Playwright blocked by site or JS-heavy rendering | Medium | Low (fallback exists) | Users can always upload a manual screenshot. Error message explains the fallback. |
| **API cost overruns during demos** | Low | Low | Sonnet pricing is minimal (~$0.02/audit). Set a soft cap in settings. |
| **Regulator data sensitivity** — regulators may not want to send screenshots through an external API | Medium | Medium | Document data handling: screenshots are sent to Anthropic API, processed, not stored. Offer localhost deployment option for sensitive use cases. |
| **Scope creep into multi-page flows** | Medium | Medium | V1 scope is single-page audit. Multi-page is a stretch goal for Week 4 only if core is solid. |
| **Competitive response** — Fair Patterns or others adopt Gray et al. ontology | Low (short-term) | Medium | First-mover advantage on this specific ontology. BIT's differentiation is the consultancy wrapper and public-sector positioning, not just the tool. |

---

## 11. Out of scope (v1)

- Automated crawling of entire sites
- Real-time monitoring or alerting
- User accounts or persistent storage beyond session
- Integration with regulatory case management systems
- Comparison against competitor sites
- Automated re-testing over time (regression tracking)
- Paid SaaS offering or commercial licensing

---

## 12. Strategic vision: the tool as a consultancy platform

### 12.1 The bigger picture

The audit tool is not the product — it's the entry point. The tool demonstrates BIT's capability and creates demand for deeper advisory work that only a behavioural science consultancy can deliver. The tool generates the leads; the consultancy services generate the revenue.

Think of it as: **the tool does the "what" (detection); BIT's consultants do the "so what" and "now what."**

### 12.2 Consultancy services enabled by the tool

**Tier 1: Diagnostic services (tool-led, consultant-light)**

- **Rapid dark pattern audits.** Use the tool to conduct structured audits for clients, with a BIT consultant reviewing and contextualising the output. Deliverable: audit report + 1-hour debrief. Low cost, high volume, good for initial engagements.
- **Sector benchmarking studies.** Audit multiple services within a sector (e.g., all major ride-hailing apps, or all telco sign-up flows in a given market) and produce a comparative report. Useful for regulators conducting market studies or for trade associations.
- **Pre-launch compliance checks.** Product teams send screenshots of forthcoming designs for a quick dark pattern review before go-live.

**Tier 2: Advisory services (consultant-led, tool-supported)**

- **Regulatory guidance development.** Help regulators draft dark pattern guidelines, codes of practice, or enforcement frameworks. The tool provides the empirical base; BIT provides the policy expertise. Example: supporting a national consumer protection agency to develop its own dark pattern assessment methodology.
- **Remediation design.** After an audit identifies problems, BIT designs the behavioural interventions to fix them — redesigning choice architectures, consent flows, cancellation processes. This is where BIT's core expertise in behavioural design comes in.
- **Training and capability building.** Run workshops for regulator staff or industry teams on identifying dark patterns, using the tool, and applying behavioural science to digital consumer protection. Can be delivered as a standalone programme or embedded within a broader capacity-building engagement.

**Tier 3: Strategic engagements (high-touch, high-value)**

- **National dark pattern assessments.** Comprehensive review of a country's digital services landscape — auditing the most-used consumer platforms and producing a state-of-play report with policy recommendations. This is a signature BIT offering: combining tool-generated evidence with expert analysis.
- **Policy design and legislation support.** Advising governments on drafting dark pattern regulations, drawing on the ontology framework and BIT's cross-country experience. Example: helping a government define which patterns should be prohibited vs. disclosed vs. permitted.
- **Longitudinal monitoring programmes.** Establishing ongoing audit programmes where regulators periodically re-audit key services to track improvement or regression. The tool provides the standardised methodology; BIT provides the analytical framework and reporting.

### 12.3 Revenue model logic

| Service tier | Tool role | BIT consultant role | Indicative pricing | Sales cycle |
|---|---|---|---|---|
| **Tier 1: Diagnostic** | Primary — generates the report | Reviews, contextualises, presents | £5K–£15K per engagement | Short (weeks) |
| **Tier 2: Advisory** | Supporting — provides evidence base | Leads the engagement | £20K–£80K per engagement | Medium (1–3 months) |
| **Tier 3: Strategic** | Foundation — underpins the methodology | Leads strategy and policy work | £50K–£200K+ per engagement | Long (3–6 months) |

### 12.4 Go-to-market sequence

1. **Demo the tool** to generate interest and establish credibility. The tool is the conversation starter — it shows capability concretely rather than abstractly.
2. **Offer a Tier 1 diagnostic** as a low-commitment first engagement. This gets BIT's foot in the door and builds the relationship.
3. **Upsell to Tier 2/3** based on findings. If the diagnostic reveals significant issues or the client has broader regulatory questions, propose deeper advisory work.
4. **Publish benchmarking research** using the tool to build BIT's public profile in this space. Sector reports, blog posts, and conference presentations create inbound demand.

### 12.5 Longer-term product evolution

If the consultancy services gain traction, the tool itself may evolve:

- **Multi-page journey audits** — analysing full checkout funnels, onboarding flows, and cancellation paths rather than single pages.
- **Longitudinal tracking** — re-auditing the same services over time and producing trend reports for regulators.
- **Jurisdiction-specific regulatory mapping** — linking detected patterns to specific legal provisions (e.g., EU DSA Article 25, FTC Section 5) to produce enforcement-ready outputs.
- **Client self-service portal** — a licensed version of the tool that regulators or industry bodies can run independently, with BIT providing the methodology and updates.
- **Training mode** — an educational version where users try to identify dark patterns before the tool reveals its findings, useful for regulator capacity-building programmes.

---

## 13. Open questions

1. **Ontology licensing:** Can we reference and embed the Gray et al. ontology in a tool? Need to confirm academic use terms.
2. **BIT branding:** What level of BIT branding is appropriate for an external-facing demo tool? Need sign-off from comms.
3. **Data handling for regulator users:** Should we offer a fully local deployment option (no API calls) for sensitive use cases? This would require a local model or cached analysis.
4. **Multi-page flows:** How important is checkout funnel analysis for the regulator demo? If critical, prioritise in Week 4.
5. **Pricing and commercial model:** Does BIT want to position this as a free demo tool that drives consultancy, or explore licensing/subscription revenue for the tool itself?
6. **Competitive positioning:** Should we reference or acknowledge existing tools (e.g., Fair Patterns) in client-facing materials, or let the ontology and methodology speak for themselves?

---
---

# Part B: Technical Requirements

---

## 14. Tech stack

| Layer | Choice | Rationale |
|---|---|---|
| **Frontend/UI** | Streamlit (Python) | Fast to build, zero frontend code, built-in components for file upload, dataframes, charts, download buttons. Free hosting on Streamlit Community Cloud. |
| **Analysis engine** | Claude API (Anthropic) | Vision capability for screenshot analysis. Structured output for consistent report generation. |
| **Development/prototyping** | Claude Code | Used for iterating on prompts, ontology, and analysis logic locally before wiring into the Streamlit app. |
| **Screenshot capture** | Playwright (Python) | Headless browser for URL → screenshot. Handles JS-rendered pages. |
| **Export** | `markdown` + `fpdf2` or `weasyprint` | Markdown for structured text export; PDF generation for formal reports. |
| **Deployment** | Streamlit Community Cloud | Free, shareable URL, no infrastructure management. Localhost for development. |

---

## 15. App architecture

### 15.1 Folder structure

```
dark-patterns-audit-tool/
├── app.py                     # Main Streamlit entrypoint
├── requirements.txt           # Python dependencies
├── .streamlit/
│   └── config.toml            # Streamlit theme and settings
├── config/
│   ├── settings.py            # App configuration (model, temperature, etc.)
│   └── ontology.json          # Gray et al. ontology (structured)
├── core/
│   ├── analyser.py            # Orchestrates the analysis pipeline
│   ├── prompt_builder.py      # Constructs analysis prompts from ontology + input
│   ├── report_generator.py    # Structures raw analysis into report format
│   └── screenshot.py          # URL → screenshot capture (Playwright)
├── ui/
│   ├── input_page.py          # Upload/URL input interface
│   ├── report_page.py         # Report display, filtering, export
│   └── components.py          # Reusable UI elements (severity badges, cards, etc.)
├── export/
│   ├── pdf_export.py          # PDF report generation
│   └── markdown_export.py     # Markdown report generation
├── data/
│   └── audit_history.json     # Session-based audit log (file-backed)
└── tests/
    ├── calibration/           # Known-deceptive and clean page test cases
    └── test_analyser.py       # Unit tests for analysis pipeline
```

### 15.2 Data flow

```
User input (screenshot or URL)
        │
        ▼
┌─────────────────────┐
│  If URL: capture     │
│  screenshot via      │
│  Playwright          │
│  (screenshot.py)     │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  prompt_builder.py   │
│  Loads ontology.json │
│  Constructs analysis │
│  prompt with image   │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  analyser.py         │
│  Sends to Claude API │
│  (vision + text)     │
│  Receives structured │
│  JSON response       │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  report_generator.py │
│  Parses response     │
│  Applies severity    │
│  rubric, structures  │
│  into report schema  │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  report_page.py      │
│  Renders in Streamlit│
│  + export options    │
│  (PDF / Markdown)    │
└─────────────────────┘
```

### 15.3 Page structure (Streamlit)

The app uses a single-page layout with clear sections, not Streamlit's multi-page navigation. This keeps the flow linear and intuitive for non-technical users.

**Sidebar:**
- BIT branding/logo
- About the tool (collapsible)
- Methodology summary (collapsible)
- Audit history (list of past audits in session, clickable)

**Main area — sequential flow:**
1. **Input section** — File uploader + URL text input. Clear CTAs. Brief guidance text.
2. **Analysis status** — Progress indicator while the audit runs. Shows which category is being checked.
3. **Executive summary** — Finding count, severity breakdown (bar chart or metric cards), overall risk assessment.
4. **Findings table** — Sortable/filterable Streamlit dataframe. Columns: Pattern name, Ontology path, Severity, Evidence summary.
5. **Detailed findings** — Expandable cards per finding. Each contains: ontology classification (3-level path), evidence description, behavioural harm analysis, severity justification, recommended fix.
6. **Patterns not detected** — Collapsible section confirming full-coverage audit. Lists categories checked and confirmed clean.
7. **Methodology** — Framework citation, severity rubric, model details, limitations disclaimer.
8. **Export** — Download buttons for PDF and Markdown.

---

## 16. Ontology specification

### 16.1 Source

Gray, C. M., Santos, C., Bielova, N., Toth, C., & Clifford, D. (2024). "An Ontology of Dark Patterns Knowledge." CHI 2024.

### 16.2 JSON schema

The ontology is stored as `config/ontology.json`:

```json
{
  "version": "1.0",
  "source": "Gray et al. (2024) CHI Ontology",
  "strategies": [
    {
      "id": "S1",
      "name": "Obstruction",
      "description": "Making a process more difficult than it needs to be...",
      "angles": [
        {
          "id": "S1.A1",
          "name": "Price Comparison Prevention",
          "description": "...",
          "patterns": [
            {
              "id": "S1.A1.P1",
              "name": "...",
              "description": "...",
              "indicators": ["...", "..."],
              "examples": ["..."],
              "severity_default": "Medium"
            }
          ]
        }
      ]
    }
  ]
}
```

### 16.3 Design decisions

- **Indicators field:** Each pattern includes observable signals (visual, textual, interactive) that the analysis prompt uses to detect presence. These are what make the ontology actionable rather than just descriptive.
- **Default severity:** Each pattern has a default severity level, which the analyser can override based on context (e.g., hidden fees in a checkout flow are always High regardless of the pattern's default).
- **Versioning:** The ontology is versioned so reports always reference which version was used. If Gray et al. update their framework, we can update without breaking historical reports.

### 16.4 Prerequisite task

The ontology JSON needs to be manually constructed from the Gray et al. paper. This is a prerequisite before the build begins. Estimated effort: 2–3 hours to extract and structure all 65 patterns with IDs, descriptions, indicators, and default severities.

---

## 17. Prompt strategy

### 17.1 Approach: Structured single-pass with ontology injection

The analysis uses a single API call with the full ontology loaded into the system prompt. This is preferred over multi-pass (one call per strategy) because:

- Reduces latency (one call vs. five)
- Allows the model to reason across categories (some patterns overlap)
- Claude's context window comfortably fits the ontology + image + instructions

If context limits become an issue (unlikely with current models), fall back to a two-pass approach: first pass for detection, second pass for detailed analysis of detected patterns only.

### 17.2 Prompt structure

```
[System prompt]
├── Role and task framing
├── Full ontology (from ontology.json)
├── Severity rubric with definitions and examples
├── Output schema (JSON) with required fields
└── Analysis instructions:
    ├── Check ALL 5 strategies systematically
    ├── For each detected pattern:
    │   ├── Cite specific visual/textual evidence
    │   ├── Map to ontology path (Strategy → Angle → Pattern)
    │   ├── Assign and justify severity
    │   ├── Explain the behavioural mechanism being exploited
    │   └── Recommend a fix
    ├── For strategies with no findings: explicitly confirm checked
    └── Flag uncertainty (possible but not certain patterns)

[User message]
├── Image (screenshot — sent as base64 via vision API)
└── Context (if URL provided: domain, page type if known)
```

### 17.3 Output schema

The prompt instructs the model to return structured JSON:

```json
{
  "audit_metadata": {
    "url": "...",
    "page_type": "checkout | landing | settings | cookie_banner | ...",
    "audit_timestamp": "...",
    "ontology_version": "1.0"
  },
  "summary": {
    "total_findings": 0,
    "high": 0,
    "medium": 0,
    "low": 0,
    "risk_level": "High | Medium | Low | Clean"
  },
  "findings": [
    {
      "pattern_id": "S1.A1.P1",
      "pattern_name": "...",
      "strategy": "Obstruction",
      "angle": "Price Comparison Prevention",
      "severity": "High",
      "evidence": "Specific description of what was observed...",
      "behavioural_mechanism": "Which cognitive bias or behavioural principle is being exploited...",
      "harm_analysis": "Why this is deceptive and how it affects the user...",
      "severity_justification": "Why this severity level...",
      "recommendation": "What the interface should do instead..."
    }
  ],
  "strategies_checked": {
    "Obstruction": { "checked": true, "findings_count": 0 },
    "Sneaking": { "checked": true, "findings_count": 2 },
    "Interface Interference": { "checked": true, "findings_count": 1 },
    "Forced Action": { "checked": true, "findings_count": 0 },
    "Social Engineering": { "checked": true, "findings_count": 0 }
  },
  "confidence_notes": "Any patterns the model was uncertain about..."
}
```

### 17.4 Prompt calibration

The prompt will be iteratively refined during Phase 1 (calibration testing). Key tuning dimensions:

- **False positive control:** The prompt should explicitly instruct the model to distinguish standard UX conventions from dark patterns. For example, a "Recommended" badge is not inherently a dark pattern; a "Recommended" badge on a more expensive option with suppressed alternatives is.
- **Evidence specificity:** The model should cite exact text, colours, button labels, and spatial relationships — not vague descriptions.
- **Severity calibration:** Test cases with known severity levels will calibrate whether the model's assignments match expert judgement.

---

## 18. API integration

### 18.1 Development → Production path

| Phase | Analysis backend | How it works |
|---|---|---|
| **Local dev** | Claude Code (local) | Prompt iteration and testing via Claude Code. No API costs. |
| **Streamlit prototype** | Claude API (direct) | `anthropic` Python SDK. API key stored in Streamlit secrets or `.env`. |
| **Streamlit Cloud deploy** | Claude API (direct) | API key stored in Streamlit Cloud secrets management. |

### 18.2 Analyser interface

```python
# core/analyser.py — simplified interface

import anthropic
from config.settings import MODEL, MAX_TOKENS, TEMPERATURE

client = anthropic.Anthropic()  # Reads ANTHROPIC_API_KEY from env

def analyse_screenshot(image_base64: str, url: str = None) -> dict:
    """
    Sends screenshot to Claude API with ontology-based analysis prompt.
    Returns structured audit results as dict.
    """
    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
        system=build_system_prompt(),   # Ontology + rubric + instructions
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/png",
                            "data": image_base64
                        }
                    },
                    {
                        "type": "text",
                        "text": f"Audit this interface for dark patterns. URL: {url or 'Not provided'}"
                    }
                ]
            }
        ]
    )
    return parse_response(response)
```

### 18.3 Abstraction layer

The analyser module exposes a single function interface (`analyse_screenshot`) so the backend can be swapped without touching UI code. During local development with Claude Code, this function can be stubbed with saved responses for faster UI iteration.

### 18.4 Cost estimate

- Model: `claude-sonnet-4-20250514` (vision-capable, good balance of quality and cost)
- Estimated tokens per audit: ~2,000 input (ontology + image) + ~2,000 output (structured report)
- Cost per audit: approximately $0.01–0.02 USD
- At 100 demo audits: ~$1–2 total

---

## 19. Configuration

All tuneable parameters are centralised in `config/settings.py`:

```python
# Model
MODEL = "claude-sonnet-4-20250514"
TEMPERATURE = 0.1          # Low for consistency; near-deterministic
MAX_TOKENS = 4096

# Ontology
ONTOLOGY_PATH = "config/ontology.json"
ONTOLOGY_VERSION = "1.0"

# App
APP_TITLE = "Dark Patterns Audit Tool"
APP_SUBTITLE = "Powered by the Gray et al. (2024) CHI Dark Pattern Ontology"
MAX_FILE_SIZE_MB = 10
ALLOWED_IMAGE_TYPES = ["png", "jpg", "jpeg", "webp"]

# Export
PDF_TEMPLATE = "export/templates/report.html"
REPORT_FOOTER = "Generated by BIT Dark Patterns Audit Tool v1.0"
```

---

## 20. Dependencies and environment

### 20.1 Python dependencies (requirements.txt)

```
streamlit>=1.30.0
anthropic>=0.40.0
playwright>=1.40.0
fpdf2>=2.7.0
Pillow>=10.0.0
pandas>=2.0.0
plotly>=5.18.0
```

### 20.2 Environment variables

```
ANTHROPIC_API_KEY=sk-ant-...
```

Stored in `.env` for local development, Streamlit Cloud secrets for deployment.

### 20.3 Playwright setup

Playwright requires a one-time browser install after `pip install`:

```bash
playwright install chromium
```

Note: Streamlit Community Cloud may not support Playwright. If URL capture is blocked in deployment, the feature degrades gracefully — users upload screenshots manually. Evaluate alternatives (e.g., a lightweight screenshot API) if this becomes a blocker.
