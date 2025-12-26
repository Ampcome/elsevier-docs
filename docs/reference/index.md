# Data Dictionary

## Overview

This reference provides definitions for all key data fields used across permissions systems, particularly RPC.

## Project Fields

### Core Project Information

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| **Project ID** | String | Unique project identifier | PRJ-2024-12345 |
| **Project Title** | String | Book/journal title | "Clinical Cardiology, 5th Ed" |
| **Project Type** | Enum | Type of publication | Book, Journal, Chapter |
| **Status** | Enum | Current project status | Active, Complete, On Hold |
| **Priority** | Enum | Urgency level | High, Medium, Low |
| **Publication Date** | Date | Target publication date | 2024-06-15 |
| **Created Date** | DateTime | When project was created | 2024-01-10 14:30:00 |

### Project Relationships

| Field | Type | Description |
|-------|------|-------------|
| **Editor** | Reference | Assigned editor(s) |
| **Publisher** | Reference | Elsevier imprint |
| **Department** | Reference | HS or S&T |
| **Parent Project** | Reference | For multi-volume works |

## Permission Item Fields

### Item Identification

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| **Item ID** | String | Unique item identifier | ITM-2024-67890 |
| **Source Citation** | Text | Full citation of source | "Smith J. Nature. 2023;500:123-128" |
| **DOI** | String | Digital Object Identifier | 10.1038/nature12345 |
| **PMID** | String | PubMed ID | 12345678 |
| **ISBN** | String | Book identifier | 978-0-123-45678-9 |

### Content Details

| Field | Type | Description | Values |
|-------|------|-------------|--------|
| **Content Type** | Enum | Type of content | Figure, Table, Text, Image, Multimedia |
| **Figure Number** | String | Source figure ID | "Figure 3A" |
| **Page Range** | String | Source pages | "pp. 123-125" |
| **Word Count** | Integer | For text excerpts | 250 |
| **Description** | Text | Content description | "ECG tracing showing..." |

### Rights Information

| Field | Type | Description |
|-------|------|-------------|
| **Rights Holder** | String | Identified owner |
| **Rights Holder Type** | Enum | Author, Publisher, Institution, Other |
| **Contact Email** | String | Primary contact |
| **Contact Name** | String | Contact person name |
| **Contact Method** | Enum | Email, Portal, CCC, Phone |

### Workflow Fields

| Field | Type | Description | Values |
|-------|------|-------------|--------|
| **Tier** | Enum | Tier classification | 0, 1, 2, 3, 4, Rule of 10 |
| **Status** | Enum | Current status | New, In Progress, Pending, Granted, Denied |
| **Assigned To** | Reference | Responsible person | |
| **Last Action Date** | DateTime | Most recent activity | |
| **Due Date** | Date | Target completion | |

### Financial Fields

| Field | Type | Description |
|-------|------|-------------|
| **Fee Amount** | Decimal | Permission cost |
| **Currency** | Enum | Fee currency |
| **Fee Status** | Enum | Pending, Approved, Paid |
| **Invoice Number** | String | For tracking |
| **PO Number** | String | Purchase order |

## Status Values

### Project Statuses

| Status | Definition | Next Actions |
|--------|------------|--------------|
| **Draft** | Being set up | Complete details |
| **Active** | In progress | Process items |
| **On Hold** | Paused | Awaiting input |
| **Complete** | All items resolved | Archive |
| **Cancelled** | Project cancelled | Close items |

### Item Statuses

| Status | Definition | Auto-triggers |
|--------|------------|---------------|
| **New** | Just created | Assignment needed |
| **Assigned** | Has owner | Research/contact |
| **In Progress** | Being worked | None |
| **Pending Response** | Awaiting reply | Follow-up reminders |
| **Escalated** | Needs review | Manager alert |
| **Granted** | Permission received | Documentation |
| **Denied** | Permission refused | Editorial notification |
| **Not Needed** | No permission required | Closure |

## Tier Definitions

### Health Sciences Tiers

| Tier | Code | Criteria |
|------|------|----------|
| **Tier 0** | HS-T0 | No permission needed (PD, CC, owned) |
| **Tier 4** | HS-T4 | Standard author permission |
| **Rule of 10** | HS-R10 | Publisher contact (10+ items or publisher rights) |

### S&T Tiers

| Tier | Code | Criteria |
|------|------|----------|
| **Tier 1** | ST-T1 | Simple author contact |
| **Tier 2** | ST-T2 | Complex/escalated cases |
| **Tier 3** | ST-T3 | Publisher negotiations |

## Content Type Values

| Value | Description | Typical Sources |
|-------|-------------|-----------------|
| **Figure** | Graphs, charts, diagrams | Journal articles |
| **Table** | Data tables | Research papers |
| **Image** | Photos, illustrations | Various |
| **Text** | Quoted passages | Books, articles |
| **Multimedia** | Video, audio, interactive | Online sources |
| **Map** | Geographic content | Atlases, articles |
| **Algorithm** | Clinical algorithms | Guidelines |

## Contact Method Values

| Value | When Used | Documentation |
|-------|-----------|---------------|
| **Email** | Direct author/publisher | Store correspondence |
| **Portal** | Publisher permission site | Screenshot/reference |
| **CCC** | RightsLink purchase | License document |
| **Phone** | Urgent/escalated | Call notes in RPC |
| **Mail** | Legacy/required | Scan documents |

## Date/Time Fields

### Standard Formats

| Format | Example | Used For |
|--------|---------|----------|
| **Date** | 2024-06-15 | Deadlines, publication |
| **DateTime** | 2024-06-15 14:30:00 | Activity logging |
| **Year** | 2024 | Copyright year |

### Calculated Fields

| Field | Calculation |
|-------|-------------|
| **Days Open** | Today - Created Date |
| **Days Since Action** | Today - Last Action Date |
| **Days to Deadline** | Due Date - Today |

## Lookup Tables

### Publisher Codes

Common publisher abbreviations used in system:

| Code | Publisher |
|------|-----------|
| **SPR** | Springer Nature |
| **WIL** | Wiley |
| **ELS** | Elsevier |
| **TAF** | Taylor & Francis |
| **OUP** | Oxford University Press |
| **CUP** | Cambridge University Press |
| **ACS** | American Chemical Society |

### Department Codes

| Code | Department |
|------|------------|
| **HS** | Health Sciences |
| **ST** | Science & Technology |
| **EDU** | Education |
