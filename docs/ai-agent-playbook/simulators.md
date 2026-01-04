# Simulators and Scenario Matrix

## Purpose
This page defines the external system simulators required for end-to-end testing when RPC, ELSA, EMSS, and other systems are not available. The core multi-agent system should not change. Simulators implement the same contracts as real integrations and emit the same triggers.

## Architecture
- Core system uses integration plugins to call external systems.
- Simulators run as separate flows or agents outside the core system.
- Simulators emit trigger events that start or advance core flows.
- A scenario orchestrator sets up simulator state and controls time-based triggers.

## Standard Event Envelope
All simulators emit events in a consistent envelope so the core system can route them.

```json
{
  "event_id": "evt_123",
  "event_type": "rpc.project.created",
  "occurred_at": "2025-01-20T10:15:00Z",
  "schema_version": "1.0",
  "source": "RPC",
  "correlation_id": "rpc:PRJ-2024-12345",
  "payload": {}
}
```

## Simulator Contracts
Each simulator exposes actions (called by the core system) and emits events (triggers used by flows).

### RPC Simulator (rpc-sync)
Actions used by core:
- Get project by ID
- List rights items for a project
- Download permission log document
- Upload documents (permission log, cost sheet, analysis report, WSR, credit line change)
- Update project status and deadlines
- Update rights item status, fees, and credit lines

Events emitted:
- ProjectCreatedOrUpdated
- PermissionLogUploaded
- RightsItemCreatedOrUpdated
- ProjectStatusChanged
- SyncFailure

Minimum project payload:
- rpc_project_id, project_title, division, tier, isbn
- permission_deadline, publication_date, submission_route
- cs_name, cs_email, cds_name, cds_email
- permission_log_available, rpc_project_url

### ELSA Simulator (elsa-export)
Actions used by core:
- Export permission log report
- List chapters and authors
- Download permission files

Events emitted:
- ProjectCreatedOrUpdated
- PermissionLogUploaded
- ELSAPermissionFilesUploaded
- SyncFailure

### EMSS Simulator (emss-ingest)
Actions used by core:
- Fetch manuscript and art file metadata
- Download manuscript and art files

Events emitted:
- ManuscriptReceived
- ProjectCreatedOrUpdated

### Email Simulator (outlook-mail)
Actions used by core:
- Send email (permission request, chaser, escalation, completion, WSR)
- Query by message_id or thread_id

Events emitted:
- InboundEmailReceived
- EmailFailure

### RightsLink/CCC Simulator (rightslink-automation)
Actions used by core:
- Request quote
- Submit order
- Retrieve license document

Events emitted:
- RightsLinkEvent (quote_ready, order_confirmed, license_issued)
- RightsLinkFailure

### Author and CDS Simulator
Actions used by core:
- Request permission log
- Request missing fields or files
- Request editorial decisions

Events emitted:
- PermissionLogUploaded
- ELSAPermissionFilesUploaded
- EditorialDecision
- InboundEmailReceived

### Publisher Portal Simulator (publisher-portal-form)
Actions used by core:
- Submit request form
- Fetch confirmation receipt

Events emitted:
- InboundEmailReceived (confirmation or denial)
- EditorialDecision (if portal returns a direct decision)

### Metadata Enrichment Simulators
Actions used by core:
- crossref-lookup: DOI lookup
- pubmed-lookup: PMID/DOI lookup
- image-finder: asset lookup

Events emitted:
- None required (synchronous responses)

### File Storage Simulator (file-storage)
Actions used by core:
- Store documents and attachments
- Retrieve stored documents

Events emitted:
- None required

### Scheduler and Time Simulator
Actions used by core:
- Schedule tasks
- Advance time or run scheduled queue

Events emitted:
- ScheduledChaser
- DeadlineRisk
- WeeklyStatusReport
- SyncRetry

## Scenario Matrix
Each scenario is a deterministic script of events and responses.

Minimum coverage set:
- ST-T1-AuthorLog-Email-Resolved
- ST-T2-AuthorLog-RightsLink-FeeWithinBudget
- ST-T3-Manuscript-GeneratedLog-NoResponse-Chasers
- HS-T4-LogProvided-Email-FeeOverLimit
- HS-T0-ValidationOnly
- HS-RuleOf10-GroupedRequest
- Portal-Form-Delayed-Approval
- CreditLineChange-EditorialDecision
- SyncFailure-Retry-Recovery
- EmailBounce-Recovery

Scenario matrix (sample):

| Scenario ID | Division/Tier | Intake Source | Rights Items Source | Contact Mode | Fee Path | Expected Outcome | Primary Triggers |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ST-T1-AuthorLog-Email-Resolved | S&T Tier1 | RPC | RPC log | Email | No fee | All items resolved, close project | ProjectCreatedOrUpdated, PermissionLogUploaded, InboundEmailReceived |
| ST-T2-AuthorLog-RightsLink-FeeWithinBudget | S&T Tier2 | RPC | ELSA export | RightsLink | Fee within limits | Auto-approve fee, license issued | ProjectCreatedOrUpdated, PermissionLogUploaded, RightsLinkEvent |
| ST-T3-Manuscript-GeneratedLog-NoResponse-Chasers | S&T Tier3 | EMSS | Manuscript extraction | Email | No fee | Escalate to editorial query after chasers | ManuscriptReceived, ScheduledChaser, PendingChaserDue |
| HS-T4-LogProvided-Email-FeeOverLimit | HS Tier4 | RPC | RPC log | Email | Fee over limit | Editorial decision required | PermissionLogUploaded, FeeApprovalPending, EditorialDecision |
| HS-T0-ValidationOnly | HS Tier0 | RPC | Author/CDS log | Email | No fee | Validate evidence, close project | PermissionLogUploaded, ProjectReadyToClose |
| HS-RuleOf10-GroupedRequest | HS RuleOf10 | RPC | RPC log | Email | No fee | Single grouped request, resolved | PermissionLogUploaded, InboundEmailReceived |
| Portal-Form-Delayed-Approval | Any | RPC | RPC log | WebForm | Fee within limits | Portal confirmation after delay | PermissionLogUploaded, ScheduledChaser, InboundEmailReceived |
| CreditLineChange-EditorialDecision | Any | RPC | RPC log | Email | No fee | Credit line updated | EditorialDecision |
| SyncFailure-Retry-Recovery | Any | RPC | RPC log | Email | No fee | Sync retry recovers, flow resumes | SyncFailure, SyncRetry |
| EmailBounce-Recovery | Any | RPC | RPC log | Email | No fee | Alternate contact attempt | EmailFailure, InboundEmailReceived |

## Simulator Data Tables
Create a dedicated schema (for example, sim) so simulator data does not mix with production tables.

Recommended tables:
- sim_scenarios: scenario metadata, status, time mode, start_at
- sim_projects: scenario_id, rpc_project_id, title, division, tier, deadlines, budgets
- sim_chapters: scenario_id, project_id, chapter_number, title, authors
- sim_rights_items: scenario_id, project_id, chapter_id, item_id, created_type, rightsholder_name, mode_of_contact, status, fee_amount
- sim_documents: scenario_id, project_id, doc_type, filename, storage_key, uploaded_at
- sim_rightsholders: scenario_id, name, type, contact_email, portal_url
- sim_rightslink_sessions: scenario_id, rightsholder_id, quote_id, order_id, license_id, fee_amount, status
- sim_mailboxes: scenario_id, address, role (author, cds, rightsholder)
- sim_emails: scenario_id, thread_id, direction, subject, body, status, message_id
- sim_events: scenario_id, event_type, payload, scheduled_at, emitted_at, status
- sim_clock: scenario_id, clock_time, speed, paused

These tables let simulators replay deterministic scripts, generate attachments, and emit triggers without manual setup.
