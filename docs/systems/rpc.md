# RPC System

## Overview

The **Rights & Permissions Collector (RPC)** is the system of record for all permission-related activities. Every permission request, communication, and outcome is documented here.

## Key Functions

| Function | Description |
|----------|-------------|
| **Project Management** | Track book/journal projects requiring permissions |
| **Item Tracking** | Monitor individual permission requests |
| **Status Management** | Update and report on permission status |
| **Communication Log** | Record all correspondence |
| **Reporting** | Generate status and metrics reports |

## RPC Interface

### Main Dashboard

The dashboard provides:
- Active projects summary
- Items requiring attention
- Overdue items alerts
- Recent activity feed
- Quick search

### Project Screen

Each project displays:

| Section | Information |
|---------|-------------|
| **Header** | Project ID, title, type, status |
| **Details** | Editor, publication date, priority |
| **Items** | List of all permission items |
| **Timeline** | Key dates and deadlines |
| **Notes** | Project-level comments |

### Item Screen

Each permission item shows:

| Field | Purpose |
|-------|---------|
| **Item ID** | Unique identifier |
| **Source** | Original publication details |
| **Rights Holder** | Identified owner |
| **Contact** | Email/portal used |
| **Status** | Current stage |
| **History** | All updates and communications |
| **Documents** | Attached files |

## Status Workflow

### Status State Machine

This diagram shows all valid status transitions for permission items:

![RPC Status State Machine](/diagrams/10_RPC_Status_State_Machine.svg)

### Item Statuses (Text Reference)

```
┌─────────────┐
│    NEW      │  Item created, not started
└──────┬──────┘
       ▼
┌─────────────┐
│ IN PROGRESS │  Actively being worked
└──────┬──────┘
       │
       ├───────────────────┐
       ▼                   ▼
┌─────────────┐     ┌─────────────┐
│   PENDING   │     │  ESCALATED  │
│  RESPONSE   │     │             │
└──────┬──────┘     └──────┬──────┘
       │                   │
       ├───────────────────┘
       ▼
┌─────────────┐
│  RESOLVED   │
└──────┬──────┘
       │
       ├─────────────┬─────────────┐
       ▼             ▼             ▼
┌───────────┐ ┌───────────┐ ┌───────────┐
│  GRANTED  │ │  DENIED   │ │ NOT NEEDED│
└───────────┘ └───────────┘ └───────────┘
```

### Status Definitions

| Status | Definition | Next Actions |
|--------|------------|--------------|
| **New** | Just created | Assign, research |
| **In Progress** | Being actively worked | Contact, research |
| **Pending Response** | Awaiting reply | Monitor, follow-up |
| **Escalated** | Needs higher review | Team lead action |
| **Granted** | Permission received | Document terms |
| **Denied** | Permission refused | Find alternative |
| **Not Needed** | Tier 0 or removed | Document reason |

## Core Features

### Search Functionality

| Search Type | Use Case |
|-------------|----------|
| **Quick Search** | Item ID, project name |
| **Advanced Search** | Multiple criteria |
| **Saved Searches** | Frequent queries |
| **Export** | Download results |

### Filtering Options

- By status
- By tier
- By date range
- By assignee
- By project type
- By publisher

### Bulk Operations

| Operation | When to Use |
|-----------|-------------|
| **Bulk Status Update** | Same-source items resolved |
| **Bulk Assign** | Rebalancing workload |
| **Bulk Export** | Reporting |

## Data Entry Guidelines

### Creating New Items

Required fields:
1. **Project** - Which project this belongs to
2. **Source Reference** - Complete citation
3. **Content Type** - Figure, table, text, etc.
4. **Usage Description** - How content will be used
5. **Rights Holder** - If known

### Updating Items

Always record:
- Date and time of update
- Action taken
- Response received (if any)
- Next steps planned
- Relevant attachments

### Documentation Standards

| Do | Don't |
|----|-------|
| Complete all required fields | Leave fields blank |
| Use consistent formatting | Use abbreviations without explanation |
| Attach correspondence | Summarize without evidence |
| Note all contact attempts | Skip logging failed attempts |
| Record exact terms | Paraphrase license terms |

## Reporting

### Standard Reports

| Report | Purpose | Frequency |
|--------|---------|-----------|
| **Status Summary** | Current state overview | Daily |
| **Aging Report** | Identify overdue items | Weekly |
| **Productivity Report** | Items closed per person | Weekly |
| **Project Status** | By-project summary | As needed |
| **Publisher Analysis** | Response rates by publisher | Monthly |

### Custom Reports

Build reports by selecting:
- Date range
- Grouping (project, person, publisher)
- Status filters
- Output format (screen, Excel, PDF)

## Best Practices

### Daily Workflow

1. **Morning** - Check dashboard for urgent items
2. **Process** - Work assigned queue
3. **Document** - Update RPC after each action
4. **End of Day** - Review pending items

### Quality Checks

- Verify source information accuracy
- Confirm rights holder identification
- Check for duplicate items
- Ensure complete documentation
- Validate status transitions

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Can't find project | Check search filters, try project ID |
| Duplicate item | Merge with original, document |
| Wrong status | Update with correction note |
| Missing history | Contact IT for audit log |
| Export fails | Reduce date range, try again |

### Getting Help

- **System Issues** - IT Help Desk
- **Process Questions** - Team Lead
- **Access Problems** - Manager + IT

## System URL

```
https://app-services.cwsrpc.elsevier.net/rp-collector-web/
```

## Detailed Screen Reference

### Project Details Screen

#### Service Details Section

| Field | Description | Example |
|-------|-------------|---------|
| **Received Date** | Project receipt date | 30-Sep-2025 |
| **Division** | Business division | HS |
| **Sub Division** | Sub-division | Clinical Solutions |
| **Project Reference No** | Internal reference | DEL_Kim_4_murugans |
| **ISBN/Manifestation Id** | Publication ID | 9780443124976 |
| **Location** | Processing location | New Delhi |

#### Editorial Contact Details

| Field | Description |
|-------|-------------|
| **Name** | Editorial contact name |
| **Email** | Contact email address |
| **Invited Editorial Users** | Additional editors with access |
| **Freelancer Name/Email** | External contractor details |

#### Project Details

| Field | Description |
|-------|-------------|
| **Author(s)** | Primary author(s) |
| **Title** | Publication title |
| **Edition** | Edition number |
| **Author/Editor email** | Author contact |
| **Projected publication date** | Target pub date |
| **Permission deadline date** | Permissions due |
| **Files to printer date** | FTP deadline |
| **Transmittal date** | Handoff date |
| **Ownership** | Rights owner (Elsevier Inc., etc.) |
| **Service Type** | Tier classification |
| **Platform** | EMSS, ELSA, etc. |
| **Language** | Publication language |
| **Free to translate** | Translation rights |
| **High priority title** | Priority flag |

#### Other Details

| Field | Description |
|-------|-------------|
| **Brief description** | Project summary |
| **Batch delivery** | Yes/No, with schedule |
| **Total Budget** | Budget for permissions |
| **Max Cost per Item** | Per-item limit |
| **Invoice payment by** | Cost center |
| **Number of Chapters** | Chapter count |
| **Book Price** | Retail price |
| **Print run** | Print quantity |
| **Page count** | Total pages |
| **Distribution** | Worldwide, regional |
| **Format** | Print, electronic, both |

### Rights Item Assignments Tab

#### Table Columns

| Column | Description |
|--------|-------------|
| **Item ID** | Unique identifier |
| **Creator Type** | Author Created, Courtesy, etc. |
| **Chapter No.** | Chapter number |
| **Rightsholders** | Rights holder name |
| **Permission Status** | Resolved, Pending, Deleted |
| **Restrictions** | Usage restrictions |
| **Invoice Amount** | Cost if applicable |
| **Resolved Time** | Days to resolve |
| **Send Email** | Email action button |

#### Status Badges

| Badge | Description |
|-------|-------------|
| **Total Items** | All items in project |
| **Total items pending** | Awaiting resolution |
| **Total items in query** | In editorial query |
| **Total items yet to apply** | Not yet requested |
| **Total fee spent** | Cumulative cost |

### Chapter Tracker Tab

For projects where authors provide permissions:

| Column | Description |
|--------|-------------|
| **Chapter No.** | Chapter number |
| **Chapter Title** | Full chapter title |
| **Authors** | Chapter author(s) |
| **Editor Email** | Editor contact |
| **Chapter Submitted** | Submission status |
| **Permission Received** | Yes/No |
| **Permission Status** | Pending, Resolved |
| **Comments** | Notes |

#### Reminder Date Columns

| Column | Purpose |
|--------|---------|
| **Intro Email Due Date** | Initial outreach |
| **Intro Email Sent Date** | Confirmation |
| **MS Due Date** | Manuscript deadline |
| **First Reminder Due/Sent** | First follow-up |
| **Second Reminder Due/Sent** | Second follow-up |
| **First Chaser Due/Sent** | First chaser |
| **Second Chaser Due/Sent** | Second chaser |

#### Chapter Permission Status Options

| Status | Description |
|--------|-------------|
| **Pending** | Awaiting resolution |
| **Resolved** | Permission obtained |
| **Permission log and licenses yet to be received** | Waiting for author |
| **Permission log received, licenses yet to be received** | Partial |

#### Chapter Statistics

- Total Chapters: Count
- Chapters Completed: Count
- Chapters Pending: Count
- Completion Rate: Percentage

### Documents Tab

| Feature | Description |
|---------|-------------|
| **Upload new Document** | Add files |
| **Download document(s)** | Export selected |
| **Document Title** | Display name |
| **File Name** | System filename |
| **Uploaded Date** | Upload timestamp |

Common document types:
- Permission Logs (`.xlsx`)
- Chapter Zip Files (`.zip`)
- AWP Files (`.pdf`, `.zip`)
- Permission grants

## Permissions Tracker Screen

**URL**: `https://app-services.cwsrpc.elsevier.net/rp-collector-web/permissions-tracker`

### Project Level View

| Column | Description |
|--------|-------------|
| **Division** | Business unit |
| **Title** | Project title |
| **Project ID** | Unique identifier |
| **Assignee** | Team member |
| **Editorial Contact** | Editor |
| **Additional Contact** | Secondary contact |
| **Total RightsItems** | All items |
| **Resolved RightsItems** | Completed |
| **To be worked RightsItems** | Remaining |

### Available Actions

- Save
- Refresh
- Send WSR (Weekly Status Report)
- Send WSR With Attachment
- Send Analysis Report
- Columns (customize)
- Export Data

## Analysis Report Screen

**URL**: `https://app-services.cwsrpc.elsevier.net/rp-collector-web/analysis-report/{id}`

### Report Header Actions

- Send Report With Attachment
- Send Report

### Report Fields

| Field | Description | Example |
|-------|-------------|---------|
| **Total no of Permission items** | All items | 404 |
| **Permissions to be cleared** | Requiring action | 404 |
| **Elsevier permissions** | Internal reuse | 0 |
| **Third Party permissions Split** | Breakdown | Publishers/Companies/Courtesy/First time |
| **High Fee permission items** | Above threshold | 0 |
| **High TAT copyright holders** | Slow responders | 0 |
| **Restriction list** | Dropdown | Available/Not Available/Not Applicable |
| **Chapter author information** | Dropdown | Available/Not Available |
| **Approximate project completion date** | Estimate | Jan 14, 2026 |

### Additional Notes

Free text area for detailed analysis, such as:
- High fee items requiring editorial decision
- Items needing replacement or deletion
- Special considerations or risks

## Email Integration

### Automated Emails from RPC

| Email Type | Trigger | From Address |
|------------|---------|--------------|
| **New Project Assignment** | Project created | rpcapplication@elsevier.com |
| **Weekly Status Report** | Manual/scheduled | permissionseeking@elsevier.com |
| **Analysis Report** | Manual send | permissionseeking@elsevier.com |

### Key Email Addresses

| Purpose | Email |
|---------|-------|
| RPC Application | rpcapplication@elsevier.com |
| Permissions Seeking | permissionseeking@elsevier.com |
| Permissions Helpdesk | permissionshelpdesk@elsevier.com |
