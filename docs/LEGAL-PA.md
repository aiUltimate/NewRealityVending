# Pennsylvania Legal Architecture — Research Baseline

**Last reviewed:** 2026-09-24  
**Status:** Research baseline — not legal advice

## 1. Core conclusion

A generic unattended machine that independently dispenses psychoactive THC products in a Pennsylvania bar should **not** be treated as the default legal architecture.

The current planning model should instead prioritize:

1. Licensed Medical Marijuana Organization partnership.
2. Approved/controlled facility architecture.
3. Smart kiosk/order interface where final regulated dispensing remains with an authorized operator.
4. Regulator-approved automated architecture only if specifically permitted.
5. Separately analyzed hemp/wellness products where the exact product and distribution route are lawful.

---

## 2. Pennsylvania Medical Marijuana

Pennsylvania's Medical Marijuana Program is a licensed framework.

The PA Department of Health states that dispensaries must obtain a permit before dispensing medical marijuana and describes permit, security, zoning, and capital requirements.

Source:
https://www.pa.gov/agencies/health/programs/medical-marijuana/dispensaries

---

## 3. Act 63

Act 63 of 2023 permits qualified independent MMOs to apply for an additional permit: an independent grower/processor can apply for one dispensary permit and an independent dispensary can apply for one grower/processor permit.

The PA Department of Health identifies Phase 3 as Fall 2025 and closed.

Source:
https://www.pa.gov/agencies/health/programs/medical-marijuana/act-63

---

## 4. API / Seed-to-Sale Integration

PA DOH states that, as of June 9, 2026, it uses a new API request form for access to Seed-to-Sale System data.

The request is submitted by the requesting MMO; if approved, the Bureau's seed-to-sale vendor works with the MMO and API vendor to implement the API.

This is highly relevant to Adaptive because the software architecture should be capable of integrating with an MMO's approved data pathway rather than attempting to bypass it.

Source:
https://www.pa.gov/agencies/health/programs/medical-marijuana/growers-processors

---

## 5. Dispensary Architecture

PA's program is not equivalent to ordinary vending retail.

The implementation must be reviewed against current:

- Chapter 1161A dispensary rules.
- Patient/caregiver identification requirements.
- Facility requirements.
- Security requirements.
- Product approval requirements.
- Seed-to-sale tracking.
- Advertising/marketing restrictions.
- Device/product requirements.

Official regulations:
https://www.pa.gov/agencies/health/programs/medical-marijuana/medical-marijuana-regulations

---

## 6. Pennsylvania Hemp

Pennsylvania maintains a separate USDA-approved hemp program.

The PA Department of Agriculture reports 2026 permits and states that hemp growing and processing are regulated under the PA Hemp Program.

Source:
https://www.pa.gov/agencies/pda/plants-land-water/hemp

---

## 7. Hemp Retailing

PA's Hemp Program FAQ states there is not a state-level permit/license specifically for wholesaling, retailing, or brokering hemp and hemp products, while also warning that specific product categories can have additional requirements and that all products must comply with applicable state and federal law.

This must NOT be interpreted as a blanket authorization to retail psychoactive cannabinoid products.

Source:
https://www.pa.gov/agencies/pda/plants-land-water/hemp/hemp-program-faqs

---

## 8. Product-by-Product Classification

For every proposed cannabinoid SKU, record:

- cannabinoid identity,
- source,
- concentration,
- total amount per container,
- product format,
- ingredients,
- intended use,
- claims,
- federal classification,
- Pennsylvania classification,
- age requirements,
- testing,
- packaging,
- licensing,
- distribution route,
- current date,
- evidence.

---

## 9. Federal Change Risk

Federal hemp rules are changing in November 2026. The project should therefore not build its long-term economics around an assumption that any particular intoxicating hemp cannabinoid will remain outside controlled-substance regulation.

Official federal research source to monitor:
https://www.congress.gov/crs-product/IF13136

---

## 10. Legal Engine Requirement

Every SKU should have a machine-readable status:

```text
APPROVED
APPROVED_WITH_RESTRICTIONS
HUMAN_REVIEW
BLOCKED
UNKNOWN
```

No automated dispensing should occur when status is:

```text
HUMAN_REVIEW
BLOCKED
UNKNOWN
```

---

## 11. Legal Workstream

The founder should maintain a table:

| Question | Answer | Authority | Date checked | Evidence | Owner |
|---|---|---|---|---|---|
| Can SKU be sold? | | | | | |
| Can SKU be dispensed from Pod? | | | | | |
| Does venue qualify? | | | | | |
| Is age verification required? | | | | | |
| Is patient verification required? | | | | | |
| Is employee involvement required? | | | | | |
| Is product approval required? | | | | | |
| Is API integration required? | | | | | |

---

## 12. Legal Stop Conditions

Stop deployment if:

- classification is unresolved,
- required license is missing,
- required approval is missing,
- product documentation is incomplete,
- age/patient verification fails,
- venue is not authorized,
- machine cannot enforce required controls,
- a regulator or qualified counsel identifies a blocking issue.

---

## 13. Research Principle

The legal engine should be **date-aware**.

A product can be:

```text
Legal on Day A
→ Restricted on Day B
→ Blocked on Day C
```

Therefore compliance decisions must be versioned.
