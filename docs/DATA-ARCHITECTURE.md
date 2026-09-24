# Data Architecture

## Design goal

Build a data model that can scale from one founder-operated machine to a distributed network.

---

# Core Entities

```text
Organization
User
Role
Venue
Machine
SKU
Product
Batch
COA
Supplier
Jurisdiction
Rule
ComplianceDecision
Transaction
InventoryEvent
MachineEvent
CustomerFeedback
Incident
AuditEvent
Campaign
Expense
```

---

# Identity Separation

Use separate domains:

```text
Identity
   │
   ├── Compliance identity
   ├── Payment identity
   └── Analytics identity
```

Do not combine these by default.

---

# Data Minimization

Store only what is needed for:

- transaction,
- safety,
- compliance,
- operations,
- analytics.

Delete or anonymize information when it is no longer necessary.

---

# Event Sourcing Concept

Important events become the system's history.

Example:

```text
SKU_CREATED
COA_ATTACHED
SKU_APPROVED
SKU_LOADED
INVENTORY_DECREMENTED
TRANSACTION_COMPLETED
CUSTOMER_RATED
SKU_BLOCKED
BATCH_RECALLED
```

---

# Analytics

Primary dimensions:

- time,
- location,
- machine,
- SKU,
- product objective,
- price,
- batch,
- transaction outcome.

---

# Privacy Principle

The less sensitive data collected, the less sensitive data can be breached.

The platform should be useful without building a medical profile of every customer.
