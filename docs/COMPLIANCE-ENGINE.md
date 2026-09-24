# Compliance Engine

## Purpose

Convert changing legal/product requirements into machine-readable gates.

---

# Decision Pipeline

```text
SKU
 ↓
Jurisdiction
 ↓
Current rule set
 ↓
Product attributes
 ↓
Evidence validation
 ↓
Decision
 ↓
Machine permissions
```

---

# Decision Status

```text
APPROVED
APPROVED_WITH_RESTRICTIONS
HUMAN_REVIEW
BLOCKED
UNKNOWN
```

---

# Example Rule

```yaml
rule_id: PA-EXAMPLE-001
jurisdiction: PA
effective_date: 2026-09-24
product_category: regulated
required:
  - valid_operator
  - approved_product
  - required_customer_verification
  - secure_location
fail_action: BLOCK
```

This is an architectural example, not a legal determination.

---

# Rule Versioning

Every decision references:

```text
rule_id
rule_version
effective_date
source
source_location
reviewer
```

---

# Change Detection

The system should periodically check authoritative sources for:

- new rules,
- amendments,
- guidance,
- forms,
- court orders,
- enforcement notices.

A detected change creates:

```text
COMPLIANCE_REVIEW_REQUIRED
```

---

# Human Review Queue

Priority:

```text
CRITICAL
HIGH
MEDIUM
LOW
```

Critical examples:

- product classification change,
- license change,
- court order,
- regulator notice,
- product recall.

---

# Compliance Fail-Closed

No evidence:

```text
UNKNOWN
```

Unknown is not approval.
