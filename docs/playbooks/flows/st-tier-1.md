# Flow S&T Tier 1 - Author Obtains

## Purpose
Author obtains permissions; AI manages chapter tracker, reminders, validation, and uploads.

## Trigger Types
- Event-based: ProjectCreatedOrUpdated, PermissionLogUploaded, ELSAPermissionFilesUploaded
- Time-based: ScheduledChaser

## Agents
- Intake and Sync Agent
- Inventory and Log Agent
- Outreach and Response Agent
- Evidence and Reporting Agent

## Integrations
- elsa-export
- outlook-mail
- rpc-sync

## Steps
1) Intake project and confirm tier = Tier1.
2) Initialize chapter tracker fields and intro email schedule.
3) Send intro and reminder emails to chapter authors.
4) Receive permission logs and licenses via ELSA or email.
5) Validate each chapter package.
   - Item IDs present and stable
   - Source details complete
   - Licenses match scope
   - Restrictions and credit lines captured
6) Consolidate chapter logs into a project-level log.
7) Upload log and evidence to RPC.
8) Close project when all chapters are complete.

## Table Updates
- chapters (tracker fields, permission_log_received, permission_files_received, permissions_status)
- documents (permission_log, license_file)
- emails (intro and reminders)
- rights_items (status updates if required)
- projects (completion status)

## Decision Rules
- If author packages are incomplete, continue reminders and escalate to CDS or editor.

## Human Decision Points
- Decisions on incomplete or missing author documentation.
