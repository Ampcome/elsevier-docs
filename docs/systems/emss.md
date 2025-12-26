# EMSS

## Overview

The **Electronic Manuscript Submission System (EMSS)** manages manuscript submissions and tracking throughout the editorial process. For permissions, it serves as the source for project and content information.

## Role in Permissions Workflow

| Function | How It Relates to Permissions |
|----------|-------------------------------|
| **Manuscript Tracking** | Source of book/journal content details |
| **Author Information** | Contact details for permissions |
| **Content Identification** | Identifies third-party content needs |
| **Timeline Management** | Publication deadlines affect permission urgency |

## Key Features for Permissions

### Project Information

EMSS provides:
- Project/book title and details
- Editorial contacts
- Publication timeline
- Chapter/article structure
- Author list with contacts

### Content Tracking

For each manuscript:
- Figures and tables list
- Source citations
- Third-party content flags
- Permission status indicators

## Interface Overview

### Dashboard

| Section | Content |
|---------|---------|
| **My Projects** | Assigned manuscripts |
| **Action Required** | Items needing attention |
| **Recent Activity** | Latest updates |
| **Quick Search** | Find projects |

### Project View

| Tab | Information |
|-----|-------------|
| **Overview** | Title, status, dates |
| **Manuscript** | Current version, history |
| **Contributors** | Authors, editors, reviewers |
| **Production** | Timeline, milestones |
| **Assets** | Figures, tables, supplements |

### Asset Management

For each figure/table:
- Asset ID and type
- Source information
- Permission status
- File attachments

## EMSS to RPC Workflow

### Creating Permission Items

1. **Identify** - Flag third-party content in EMSS
2. **Export** - Generate permission request list
3. **Import** - Create items in RPC
4. **Link** - Connect EMSS asset to RPC item

### Status Synchronization

| EMSS Status | RPC Action |
|-------------|------------|
| Content flagged | Create RPC item |
| Permission needed | Assign for processing |
| Permission received | Update EMSS status |
| Content removed | Close RPC item |

## Common Tasks

### Finding Project Information

1. Navigate to EMSS dashboard
2. Search by project name/ID
3. Open project details
4. Review assets requiring permissions

### Identifying Rights Holders

From EMSS asset records:
- Original publication citation
- Author names from source
- Publisher information
- DOI/PMID if available

### Updating Permission Status

1. Locate asset in EMSS
2. Update permission status field
3. Add notes if needed
4. Status syncs to production team

## Integration Points

### With RPC

| Data Flow | Direction |
|-----------|-----------|
| Project creation | EMSS → RPC |
| Asset details | EMSS → RPC |
| Permission status | RPC → EMSS |
| Completion confirmation | RPC → EMSS |

### With Editorial

| Communication | Channel |
|---------------|---------|
| Content questions | EMSS comments |
| Timeline changes | Email + EMSS |
| Alternative requests | Editorial workflow |

## Best Practices

### Data Quality

- Verify source citations are complete
- Ensure figure numbers match
- Confirm author information
- Check for duplicates before creating items

### Communication

- Use EMSS comments for project-specific notes
- Tag relevant parties in updates
- Link to RPC items when referencing permissions

### Timeline Management

- Note publication deadlines
- Flag items at risk
- Communicate delays early

## Troubleshooting

### Common Issues

| Issue | Resolution |
|-------|------------|
| Can't find project | Check permissions, search by ID |
| Asset missing | Contact editorial |
| Status not updating | Check integration settings |
| Duplicate assets | Merge/consolidate |

### Support Contacts

- **Technical Issues** - EMSS Support Team
- **Access Problems** - IT Help Desk
- **Process Questions** - Team Lead
- **Editorial Questions** - Project Editor
