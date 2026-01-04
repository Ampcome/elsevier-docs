# Flow 01 - Intake and Sync

## Purpose
Create or refresh project and chapter state in the local system from RPC, ELSA, or EMSS, and establish authoritative sync metadata.

## Trigger Types
- Event-based: ProjectCreatedOrUpdated
- State-based: SyncStale
- Time-based: SyncRetry
- Failure-based: SyncFailure

## Agents
- Intake and Sync Agent
- Coordinator Agent

## Integrations
- rpc-sync
- elsa-export
- emss-ingest

## Inputs and Preconditions
- rpc_sync or elsa_sync records for a project are new or stale
- Projects may not exist locally
- RPC is the system of record for project metadata, deadlines, and status

## Steps
1) Pull project metadata from RPC, ELSA, or EMSS.
   - Fields include title, division, tier, ISBN, publication date, permission deadline, budgets, formats, print run, language, and submission route.
   - Capture assignment details where available (CDS and CS).
2) Create or update projects.
   - Ensure valid division and tier values.
3) Initialize chapters when chapter metadata is available.
   - Set chapter numbers, titles, authors, and due dates.
4) Record sync state and hashes.
   - Store sync status, timestamps, and any pending changes.
5) Start a workflow execution for this intake run.

## Table Updates
- projects: project_title, division, tier, isbn, publication_date, permission_deadline, permission_budget, max_cost_per_item, currency, formats, print_run, language, submission_route, cds_user_id, cs_user_id, status
- chapters: project_id, chapter_number, chapter_title, author_name, author_email, ms_due_date
- rpc_sync or elsa_sync: sync_status, last_sync_at, local_hash, remote_hash, pending_changes, error_message
- workflow_executions and workflow_steps: status, inputs, outputs, error_message
- audit_log and status_history: entity_type, entity_id, changed_fields, old_values, new_values
- api_logs: external call metadata and response status

## Outputs
- Project and chapters are current and eligible for downstream flows.

## Decision Rules
- RPC is the authoritative source for project deadlines, budgets, and completion status.
- ELSA or EMSS can provide upstream chapter data and manuscripts, but project-level changes must be aligned to RPC.

## Failure Handling
- On sync failure, set sync_status = failed and schedule retry.
- Track retry_count and next_retry_at in rpc_sync or elsa_sync.

## Human Decision Points
- None. All decisions are deterministic at this stage.
