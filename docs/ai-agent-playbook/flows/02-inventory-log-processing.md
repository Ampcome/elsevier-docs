# Flow 02 - Inventory and Log Processing

## Purpose
Convert permission logs or manuscripts into structured rights items and maintain chapter tracker fields.

## Trigger Types
- Event-based: PermissionLogUploaded, ManuscriptReceived, ELSAPermissionFilesUploaded
- State-based: projects.initial_log_attached = false with available sources

## Agents
- Inventory and Log Agent

## Integrations
- rpc-sync
- elsa-export
- emss-ingest
- file-storage

## Inputs and Preconditions
- Permission log available from RPC or author/ELSA
- Manuscript or art files available (Tier 3)
- Chapter metadata may already exist from Intake and Sync

## Steps
1) Download and store source artifacts.
   - Permission logs, manuscripts, art files, and author-supplied licenses.
2) Validate log structure.
   - Ensure mandatory columns are present and Item ID is unique.
   - If missing, mark items for manual review and request corrections.
3) Parse permission logs into rights_items.
   - Create one rights_items row per permission item.
4) For Tier 3, extract third-party items from manuscripts and build a new RPC-format log.
   - Assign stable item IDs and capture chapter mapping.
5) Update chapter tracker fields when chapter-based workflows apply.

## Table Updates
- documents: document_type = permission_log, manuscript, art_file, license_file; document_category = input or working; file_url or file_path
- rights_items: project_id, chapter_id, item_id, previous_edition_item_id, image_finder_item_id, caption, source_info, original_figure_number, status = yet_to_apply
- chapters: intro_email_due_date, intro_email_sent_date, ms_due_date, first_reminder_due_date, second_reminder_due_date, first_chaser_due_date, second_chaser_due_date, permission_log_received, permission_files_received, tracker_comments
- projects: initial_log_attached = true
- status_history and audit_log for all changes

## Outputs
- Rights items and chapter tracker are populated and ready for classification.

## Decision Rules
- If permission log is incomplete (missing mandatory fields), flag for author or CDS follow-up before proceeding.
- If item IDs are missing, generate stable IDs before upload.
- Ensure item IDs are unique across chapters for consolidated logs.

## Human Decision Points
- Manual review when source citations are ambiguous or missing.
