# ELSA

## Overview

**ELSA (Elsevier Author Platform)** is the self-service platform for authors interacting with Elsevier. For permissions, it can facilitate direct author communication and permission workflows.

## Role in Permissions

| Function | Permissions Relevance |
|----------|----------------------|
| **Author Portal** | Authors can respond to permission requests |
| **Contact Verification** | Validated author contact information |
| **Self-Service** | Potential for author-initiated permissions |
| **Communication Hub** | Alternative contact channel |

## Key Features

### Author Profile

Each author profile includes:
- Verified email address
- Institution affiliation
- Publication history
- ORCID connection (if linked)

### Communication Tools

| Feature | Use |
|---------|-----|
| **Direct Messages** | Contact authors through platform |
| **Notifications** | Alert authors to requests |
| **Document Sharing** | Exchange permission forms |

## Using ELSA for Permissions

### Finding Author Contacts

1. Search by author name
2. Filter by publication
3. View verified contact info
4. Note last activity date

### Contacting Authors

When email fails, ELSA can:
- Send notification to author
- Provide alternate contact path
- Show if author is active on platform

### Verification Benefits

| Advantage | Description |
|-----------|-------------|
| **Email Validation** | Confirmed working addresses |
| **Activity Status** | See if author is active |
| **Affiliation Currency** | Updated institution info |
| **Publication Linking** | Connect to their works |

## Integration with Workflow

### When to Use ELSA

| Scenario | ELSA Action |
|----------|-------------|
| Email bounced | Find alternate contact |
| No response | Check activity status |
| Verify identity | Confirm author details |
| Multiple authors | Find co-author contacts |

### Author Self-Service Potential

Future capabilities may include:
- Authors viewing permission requests
- Online permission granting
- Terms selection interface
- Direct document exchange

## Best Practices

### Contact Verification

1. Cross-reference with paper correspondence
2. Check last login date
3. Verify institution is current
4. Confirm publication matches

### Communication Etiquette

- Keep messages professional
- Reference specific content clearly
- Provide easy response options
- Respect platform guidelines

## Limitations

| Limitation | Workaround |
|------------|------------|
| Not all authors registered | Use traditional email |
| Activity varies | Check last login |
| Limited messaging features | Follow up via email |
| Author may miss notification | Multiple channels |

## System Access

### For Permissions Staff

- Read-only access to author profiles
- Contact information visibility
- Activity status viewing
- Publication history access

### Requesting Access

1. Submit IT ticket
2. Manager approval
3. Training completion
4. Access provisioned

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Author not found | May not be registered |
| Old contact info | Check last updated date |
| Author unresponsive | Try alternative channels |
| Access denied | Contact IT for permissions |

## System URL

```
https://app.elsa.elsevier.com/
```

## Detailed Screen Reference

### Chapter View Screen

**URL Pattern**: `https://app.elsa.elsevier.com/document/{id}/write`

#### Navigation Tabs

| Tab | Purpose |
|-----|---------|
| **Write** | Main editing interface |
| **Activity & Versions** | Change history |
| **Permissions Files** | Upload granted permissions |
| **Figures** | Figure management |
| **Tables** | Table management |
| **Permission Log** | Permission tracking |
| **Art Log** | Artwork tracking |
| **LaTeX files** | LaTeX support files |

#### Chapter Information Display

| Field | Description |
|-------|-------------|
| **Chapter Number** | Chapter position |
| **Title** | Chapter title |
| **View Mode** | Toggle view options |
| **Staff Review** | Progress indicator (stages) |
| **Word Count** | Total words |
| **Publishing Assistant** | Alert count |

### Permissions Files Tab

**URL Pattern**: `https://app.elsa.elsevier.com/document/{id}/resources/{resource-id}/edit?projectId={project-id}`

| Feature | Description |
|---------|-------------|
| **Upload** | Add granted permissions files |
| **Table Columns** | Name, Size, Uploaded By, Date, Placed in Document |
| **Purpose** | Share permission files with co-contributors |
| **Save Button** | Save uploaded files |

### Permission Log Tab

**URL Pattern**: `https://app.elsa.elsevier.com/document/{id}/permissionlogreport?projectId={project-id}`

| Column | Description |
|--------|-------------|
| **#** | Row number |
| **Owner** | Report creator |
| **Report** | Report type |
| **Created** | Date/time |
| **Status** | Waiting, Complete |

- **Run Button**: Generates permission log report
- Reports queue and update when complete

### Publishing Assistant Tab

Provides overview of all chapters:

| Column | Description |
|--------|-------------|
| **Name** | Chapter name |
| **Location** | Section/Part |
| **Current Workflow Stage** | Production, Draft, etc. |
| **Word Count** | Total words |
| **Figures** | Figure count |
| **References** | Reference count |
| **Tables** | Table count |
| **Boxes** | Box count |
| **Callouts** | Callout count |
| **Permissions** | Permission item count |

**Download project reports** button available at top.

### Project List View

**URL**: `https://app.elsa.elsevier.com/project/list`

| Feature | Description |
|---------|-------------|
| **Search** | Search by project name |
| **Filter** | Filter by Editor/Author |
| **View Options** | All projects, Due dates |
| **Table Columns** | Project Name, Editors/Authors, Publication Date |

### Project Settings Screen

| Section | Purpose |
|---------|---------|
| **General Information** | Project name, details |
| **Project Settings** | Configuration options |
| **Import Previous Edition** | Import from prior edition |
| **Publishing Assistant** | Assistant settings |

### Dates & Milestones Tab

| Column | Description |
|--------|-------------|
| **Name** | Chapter name |
| **Location** | Part number |
| **Currently Editing** | Active editor |
| **Responsible Editor** | Assigned editor |
| **Chapter Notes** | Notes |
| **Status columns** | Not Started, Draft, Staff Review, etc. |

### Reports & Jobs Tab

| Column | Description |
|--------|-------------|
| **#** | Row number |
| **Report** | Report type |
| **Owner** | Creator |
| **Created** | Date/time |
| **Status** | complete/pending |

#### Available Report Types

- Project Status Report
- Contributor Agreement Report
- Contributor Payments by Project Report
- Permission Logs Report

## Chapter Status Indicators

| Icon | Status | Description |
|------|--------|-------------|
| Red circle | Not Started | Chapter not begun |
| Orange circle | Draft | In draft stage |
| Yellow circle | Staff Review | Under editorial review |
| Green circle | Production | In production |
| Blue checkmark | Complete | Chapter finished |

## Permission Logs Report (ELSA Export)

### Report Format

```
Selected Parameters:
Project Id: [Project GUID]

Permission Logs Report for a Project
```

### Report Columns

| Column | Description |
|--------|-------------|
| **Project ID / Publication Name** | Full project name |
| **Permission Status (Mandatory)** | Status |
| **Chapter Number** | Chapter number |
| **Chapter Title** | Full chapter title |
| **Elsevier Author Name** | Chapter author |

### Status Values in Report

| Status | Meaning |
|--------|---------|
| **No Permission Needed** | Original content |
| **Resolved** | Permission obtained |
| **Pending** | Awaiting response |

## ELSA Support Resources

| Resource | URL |
|----------|-----|
| **ELSA FAQ** | https://service.elsevier.com/app/answers/detail/a_id/17532/ |
| **ELSA Support Hub** | https://service.elsevier.com/app/home/supporthub/elsa/ |
| **ELSA Support Email** | elsasupport@elsevier.com |
