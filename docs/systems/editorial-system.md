# Editorial System

## Overview

The **Editorial System** (`editorial.elsevier.com`) is the production tracking system for book and chapter workflows. It provides editorial contacts with visibility into manuscript progress and supports coordination with permissions workflows.

## System URL

```
https://editorial.elsevier.com/app/book?execution={id}
```

## Role in Permissions

| Function | Permissions Relevance |
|----------|----------------------|
| **Status Tracking** | Monitor manuscript progress relative to permissions deadlines |
| **Editorial Contact** | Find editors for escalations and queries |
| **Timeline Visibility** | Understand production deadlines |
| **Chapter Management** | Track chapter-level status |

## Interface Overview

### All Other Contributions Assigned To Me View

| Column | Description |
|--------|-------------|
| **MANUSCRIPT AUTHORS** | Author names |
| **CURRENT STATUS DUE DATE** | Status with deadline |
| **PREVIOUS WORKFLOW STEP** | Prior stage |
| **LAST SENT** | Date of last action |

### Status Indicators

| Color | Meaning |
|-------|---------|
| **Green squares** | On track |
| **Orange squares** | Attention needed |
| **Red flag** | Overdue/urgent |

### Workflow Steps

| Step | Description |
|------|-------------|
| **PM** | Project Manager review |
| **Creation** | Initial creation |
| **Production** | In production |

## Book/Chapter Structure

The system displays chapters in hierarchical order:

```
1. For internal Elsevier use only
2. Preface
3. Chapter 1: [Topic]
4. Chapter 2: [Topic]
5. Chapter 3: [Topic]
...
```

## Using Editorial System for Permissions

### Finding Editorial Contacts

1. Navigate to project in Editorial System
2. View assigned editors and project managers
3. Use contact information for escalations

### Timeline Coordination

| Permission Milestone | Editorial Reference |
|---------------------|---------------------|
| Permission deadline | Files to printer date |
| Follow-up urgency | Current production stage |
| Escalation priority | Status indicator color |

### Status Synchronization

| Editorial Status | Permission Impact |
|-----------------|-------------------|
| **PM Review** | Low urgency |
| **Creation** | Medium urgency |
| **Production** | High urgency - permissions critical |

## Best Practices

### Monitoring Projects

1. Check editorial status when assessing permission urgency
2. Note color indicators for deadline awareness
3. Coordinate with editorial on at-risk items

### Communication

- Use editorial contact for content questions
- Escalate timeline concerns through PM
- Document editorial decisions in RPC

## Integration Points

| System | Data Flow |
|--------|-----------|
| **EMSS** | Manuscript submission data |
| **ELSA** | Author platform integration |
| **RPC** | Permission status (manual sync) |

## Access Requirements

| Requirement | Details |
|-------------|---------|
| **Access Request** | IT ticket |
| **Approval** | Editorial lead |
| **Training** | System overview |
| **Permissions Level** | View-only for permissions staff |

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Can't find project | Check project ID, verify access |
| Status outdated | Refresh, contact editorial |
| Access denied | Submit IT ticket |
| Editor not listed | Check EMSS for contact |
