# Agent Runbook - Intake and Sync Agent

## Purpose
Ingest project and chapter data from RPC, ELSA, and EMSS into local state and keep sync metadata current.

## Primary Responsibilities
- Pull project updates and assignments.
- Create or update projects and chapters.
- Record rpc_sync and elsa_sync state and hashes.

## Trigger Types
- Event-based: ProjectCreatedOrUpdated
- State-based: SyncStale
- Time-based: SyncRetry
- Failure-based: SyncFailure

## Flows Covered
- Flow 01: Intake and Sync
- Flow 11: Sync Retry and Failure Recovery

## Tables Read
- rpc_sync, elsa_sync, projects

## Tables Written
- projects: project_title, division, tier, isbn, publication_date, permission_deadline, permission_budget, max_cost_per_item, formats, print_run, language
- chapters: chapter_number, chapter_title, author_name, author_email, ms_due_date
- rpc_sync, elsa_sync: sync_status, last_sync_at, local_hash, remote_hash, error_message, retry_count
- audit_log, status_history, api_logs

## Integrations
- rpc-sync
- elsa-export
- emss-ingest

## Idempotency Rules
- Use rpc_project_id or elsa_project_id as natural keys.
- Do not create duplicate projects; update existing entries.

## Failure Handling
- On sync errors, set sync_status = failed and schedule retry.
- Escalate if retry_count exceeds threshold.

## Human Decision Points
- None.
