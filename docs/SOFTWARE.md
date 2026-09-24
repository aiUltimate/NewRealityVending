# Adaptive OS Software

## Core services

```text
Auth
Catalog
Orders
Payments
Inventory
Machine
Compliance
Audit
Analytics
AI
Notifications
Support
```

---

# Core API Objects

### Machine

```json
{
  "machine_id": "POD-001",
  "venue_id": "VENUE-001",
  "status": "online",
  "firmware_version": "0.1.0"
}
```

### SKU

```json
{
  "sku_id": "SKU-001",
  "status": "human_review",
  "jurisdiction": "PA"
}
```

### Compliance decision

```json
{
  "sku_id": "SKU-001",
  "jurisdiction": "PA",
  "status": "human_review",
  "rule_version": "2026-09-24",
  "evidence_ids": ["LAW-001"]
}
```

---

# Event Bus

Important events:

```text
machine_online
machine_offline
inventory_low
inventory_unknown
payment_started
payment_failed
transaction_completed
sku_blocked
compliance_review_created
coa_uploaded
batch_recalled
tamper_detected
maintenance_required
```

---

# Audit Requirement

Important actions must be immutable or append-only.

Example:

```text
WHO
WHAT
WHEN
WHY
OBJECT
PREVIOUS STATE
NEW STATE
EVIDENCE
```

---

# Dashboard

Founder dashboard:

- live machines,
- inventory,
- sales,
- incidents,
- compliance queue,
- maintenance,
- campaign funds,
- product documentation status.

The first dashboard should optimize for one founder managing the whole network.
