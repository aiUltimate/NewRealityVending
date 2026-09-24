# Adaptive Intelligence

## Principle

AI is the optimization layer, not the authority layer.

---

# AI Stack

## Layer 1 — Retrieval

Official laws, regulations, product documents, COAs, SOPs.

## Layer 2 — Extraction

Turn documents into structured data.

## Layer 3 — Classification

Classify:

- product,
- objective,
- risk,
- documentation completeness,
- maintenance event.

## Layer 4 — Prediction

Forecast:

- demand,
- inventory depletion,
- maintenance,
- venue performance.

## Layer 5 — Optimization

Recommend:

- SKU allocation,
- restocking,
- venue candidates,
- pricing experiments,
- campaign priorities.

## Layer 6 — Human Control

Human approves high-risk decisions.

---

# AI Decision Classes

### Low risk
Summarize a product document.

### Medium risk
Recommend restocking.

### High risk
Suggest a legal classification.

### Critical
Allow regulated dispensing.

Critical actions require deterministic rules + required authorization.

---

# AI Evidence Rule

Every compliance-related answer should be traceable to:

```text
Source
Document
Section
Date
Rule version
Confidence
Human reviewer
```

---

# Hallucination Defense

Never accept an AI statement merely because it sounds authoritative.

Use:

```text
AI output
 ↓
source retrieval
 ↓
evidence match
 ↓
rule engine
 ↓
human review if required
```
