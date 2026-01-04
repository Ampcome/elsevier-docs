# Agent Runbook - Inventory and Log Agent

## Purpose
Parse permission logs or manuscripts into rights items and update chapter tracker fields.

## Primary Responsibilities
- Download permission logs or manuscripts and store artifacts.
- Validate log structure and mandatory fields.
- Create rights_items records.
- Maintain chapter tracker fields for S&T Tier 1 workflows.

## Trigger Types
- Event-based: PermissionLogUploaded, ManuscriptReceived, ELSAPermissionFilesUploaded
- State-based: projects.initial_log_attached = false

## Flows Covered
- Flow 02: Inventory and Log Processing

## Tables Read
- projects, documents, chapters

## Tables Written
- rights_items: item_id, source_info, caption, chapter_id, status = yet_to_apply
- documents: permission_log, manuscript, art_file, license_file
- chapters: intro_email_due_date, reminder and chaser dates, permission_log_received, permission_files_received
- projects: initial_log_attached
- status_history, audit_log

## Integrations
- rpc-sync
- elsa-export
- emss-ingest
- file-storage

## Idempotency Rules
- Ensure item_id uniqueness within a project.
- Prevent duplicate rights_items on repeated log uploads.

## Failure Handling
- If logs are incomplete, mark for manual review and trigger reminders.

## Human Decision Points
- Manual review when critical fields are missing or ambiguous.
