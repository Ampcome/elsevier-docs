# Systems Overview

## Core Systems Architecture

The permissions seeking workflow relies on several interconnected systems:

![System Integration Architecture](/diagrams/12_System_Integration_Architecture.svg)

### Text Reference

```
┌─────────────────────────────────────────────────────────────────┐
│                    PERMISSIONS ECOSYSTEM                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────────┐  │
│  │     RPC      │◄──►│     EMSS     │◄──►│       ELSA       │  │
│  │  (System of  │    │  (Manuscript │    │    (Author       │  │
│  │   Record)    │    │  Submission) │    │    Platform)     │  │
│  └──────┬───────┘    └──────────────┘    └──────────────────┘  │
│         │                                                        │
│         ▼                                                        │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────────┐  │
│  │    Email     │    │     CCC      │    │    Publisher     │  │
│  │   (Outlook)  │    │  RightsLink  │    │     Portals      │  │
│  └──────────────┘    └──────────────┘    └──────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## System Comparison

| System | Purpose | Primary Users | Key Function |
|--------|---------|---------------|--------------|
| **RPC** | System of record | All permissions staff | Track all permission items |
| **EMSS** | Manuscript management | Editors, Authors | Submit/track manuscripts |
| **ELSA** | Author platform | Authors | Self-service access |
| **CCC RightsLink** | License purchasing | Permissions staff | Buy permissions online |
| **Email (Outlook)** | Communication | All staff | Request/respond |

## System Interconnections

### Data Flow

```
EMSS (Manuscripts)
      │
      ▼
   Project Created
      │
      ▼
RPC (Permission Items)
      │
      ├──► Email (Requests)
      │
      ├──► CCC (Purchases)
      │
      └──► Manual Entry (Results)
```

### Integration Points

| From | To | Data Exchanged |
|------|-----|----------------|
| EMSS → RPC | Project info, content items | Manual/API |
| RPC → Email | Request templates | Manual copy |
| CCC → RPC | License confirmations | Manual entry |
| ELSA → Authors | Submission status | Automatic |

## System Access

### Access Requirements

| System | Access Request | Approval |
|--------|---------------|----------|
| **RPC** | IT ticket | Manager |
| **EMSS** | IT ticket | Editorial lead |
| **ELSA** | Author self-registration | Automatic |
| **CCC** | Create account | Automatic |
| **Outlook** | Standard employee | IT automatic |

### User Roles

| Role | RPC | EMSS | CCC | Outlook |
|------|-----|------|-----|---------|
| Permissions Specialist | Full | View | Full | Full |
| Team Lead | Full + Reports | View | Full | Full |
| Manager | Admin | Full | Admin | Full |
| Editorial | View | Full | - | Full |

## System Selection Guide

### When to Use Which System

| Task | Primary System | Secondary |
|------|---------------|-----------|
| Create new project | EMSS | → RPC |
| Track permission status | RPC | - |
| Contact rights holder | Outlook | CCC |
| Purchase license | CCC RightsLink | - |
| Document permission | RPC | - |
| Research author | External tools | - |
| Generate reports | RPC | Excel |

## Quick Links

- [RPC System Guide](/systems/rpc) - Rights & Permissions Collector
- [EMSS Guide](/systems/emss) - Electronic Manuscript Submission System
- [ELSA Guide](/systems/elsa) - Elsevier Author Platform
- [CCC RightsLink](/systems/ccc-rightslink) - License purchasing
- [External Resources](/systems/external-resources) - Research tools
