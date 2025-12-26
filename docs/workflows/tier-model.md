# Tier-Based Delivery Model

## Overview

The tier-based model categorizes permission requests by complexity and required action, enabling efficient resource allocation and workflow routing.

![Tier-Based Overview](/diagrams/02_Tier_Based_Overview.svg)

## Health Sciences (HS) Tiers

### Tier 0 - Author/CDS Obtains Permissions

**Definition**: CDS/Author obtains all permissions. CS validates and uploads the logs and files into RPC.

| Responsibility | Owner |
|----------------|-------|
| **Obtain Permissions** | Author or CDS |
| **Validate Logs** | Copyrights Specialist (CS) |
| **Upload to RPC** | Copyrights Specialist (CS) |

**Workflow**:
1. Author/CDS obtains all necessary permissions
2. Author/CDS provides completed permission log
3. CS validates log completeness and accuracy
4. CS uploads logs and permission files to RPC

---

### Tier 4 - Full Service (HS)

**Definition**: CDS provides permission log. CS obtains permissions and uploads the logs and files into RPC.

| Responsibility | Owner |
|----------------|-------|
| **Provide Permission Log** | Content Development Specialist (CDS) |
| **Obtain Permissions** | Copyrights Specialist (CS) |
| **Upload to RPC** | Copyrights Specialist (CS) |

**Workflow**:
1. CDS provides permission log identifying items needing permission
2. CS reviews and validates the log
3. CS contacts rightsholders to obtain permissions
4. CS tracks responses and sends follow-up chasers
5. CS uploads completed logs and files to RPC

**Service Type in RPC**: Tier 4(HS - Full service)

---

### Rule of 10 - Assessment Only

**Definition**: No permission seeking is performed. CS only performs the Rule of 10 assessment.

| Responsibility | Owner |
|----------------|-------|
| **Rule of 10 Assessment** | Copyrights Specialist (CS) |
| **Permission Seeking** | Not performed |

**Workflow**:
1. CS receives project information
2. CS performs Rule of 10 assessment
3. CS documents assessment in RPC
4. No external permission requests are sent

---

## Science & Technology (S&T) Tiers

*Note: Tiers 1-3 apply to RREF, Hot Topics, and MRW divisions*

### Tier 1 - Author Obtains and Provides

**Definition**: Author obtains all permissions and provides permissions log. CS validates and uploads the logs and files into RPC.

| Responsibility | Owner |
|----------------|-------|
| **Obtain Permissions** | Author |
| **Provide Permission Log** | Author |
| **Validate Logs** | Copyrights Specialist (CS) |
| **Upload to RPC** | Copyrights Specialist (CS) |

**Workflow**:
1. Author obtains all permissions
2. Author provides completed permission log
3. CS validates log completeness
4. CS uploads logs and files to RPC

---

### Tier 2 - Author Provides Log, CS Obtains

**Definition**: Author provides permission log. CS obtains permissions and uploads the logs and files into RPC.

| Responsibility | Owner |
|----------------|-------|
| **Provide Permission Log** | Author |
| **Obtain Permissions** | Copyrights Specialist (CS) |
| **Upload to RPC** | Copyrights Specialist (CS) |

**Workflow**:
1. Author provides permission log identifying items needing permission
2. CS reviews and validates log
3. CS contacts rightsholders to obtain permissions
4. CS tracks responses and chasers
5. CS uploads completed logs and files to RPC

---

### Tier 3 - Full Service (S&T)

**Definition**: Author submits manuscript. CS creates permission log and obtains permissions. CS uploads the logs and files into RPC.

| Responsibility | Owner |
|----------------|-------|
| **Submit Manuscript** | Author |
| **Create Permission Log** | Copyrights Specialist (CS) |
| **Obtain Permissions** | Copyrights Specialist (CS) |
| **Upload to RPC** | Copyrights Specialist (CS) |

**Workflow**:
1. Author submits manuscript only
2. CS reviews manuscript for third-party content
3. CS creates permission log from scratch
4. CS identifies all items requiring permissions
5. CS contacts all rightsholders
6. CS tracks all responses
7. CS uploads completed logs and files to RPC

---

## Tier Classification Decision Tree

Use this decision tree to determine the correct tier for any permission request:

![Tier Classification Decision Tree](/diagrams/09_Tier_Classification_Decision_Tree.svg)

## Tier Classification Decision Matrix

| Factor | Points to Tier 0 | Points to Higher Tier |
|--------|------------------|----------------------|
| **Copyright Status** | Public domain, CC license | Active copyright |
| **Rights Holder** | Clear author ownership | Publisher or unclear |
| **Usage Scope** | STM compliant | Extended usage |
| **Volume** | Single item | Multiple items |
| **Terms** | Standard | Custom required |

## Tier Migration

Items may move between tiers based on:

- **Initial research findings** - Re-classify after investigation
- **Response received** - Author declines, escalate to publisher
- **Terms requested** - Non-standard terms require escalation
- **Volume changes** - Additional items trigger Rule of 10

## Applications Used

| Application | Purpose |
|-------------|---------|
| **RPC** | Rights & Permissions Collector - System of record |
| **ELSA** | Elsevier Author Platform |
| **EMSS** | Electronic Manuscript Submission System |
