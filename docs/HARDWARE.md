# Adaptive Pod Hardware Specification

## MVP Objective

Build the smallest machine that can prove the business model.

---

# Hardware Requirements

## Customer interface

- touchscreen,
- clear product display,
- QR/NFC,
- accessibility considerations.

## Payment

- cashless,
- secure payment terminal,
- transaction reconciliation.

## Security

- electronic locks,
- tamper detection,
- enclosure monitoring,
- controlled access.

## Inventory

- compartment tracking,
- dispense confirmation,
- low-stock alert.

## Connectivity

- Wi-Fi,
- cellular fallback where justified,
- secure device identity.

## Telemetry

- power,
- network,
- door,
- temperature where relevant,
- inventory,
- dispense events,
- errors.

---

# Device State Machine

```text
BOOT
 ↓
SELF_TEST
 ↓
ONLINE
 ↓
READY
 ↓
AUTHORIZING
 ↓
DISPENSING
 ↓
CONFIRMING
 ↓
COMPLETE
```

Error states:

```text
OFFLINE
TAMPER
PAYMENT_FAILED
INVENTORY_UNKNOWN
DISPENSE_FAILED
COMPLIANCE_BLOCKED
MAINTENANCE_REQUIRED
```

---

# Fail-Safe

If the controller loses:

- compliance status,
- inventory confidence,
- payment confirmation,
- required network state,
- authorization,

the device must not complete a regulated dispense.

---

# Hardware MVP Rule

Do not build custom electronics before proving:

1. the workflow,
2. the economics,
3. the legal architecture.

Use commercially available components where possible for the first prototype.
