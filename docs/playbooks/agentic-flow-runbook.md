# Agentic Permissions System - Per Flow Runbook

## Scope
This runbook defines the end-to-end flows for a multi-agent autonomous permissions system, aligned to the current-state documentation. It includes trigger types, agent responsibilities, integrations, rules, data mappings, and table updates so developers can implement each step in a multi-agent runtime.

## System of Record and Sources
- RPC is the system of record for projects, rights items, reporting outputs, and document storage.
- ELSA and EMSS are upstream sources for manuscripts, author data, and permission logs.
- External sources include CCC RightsLink, STM guidelines, publisher portals, and research databases.
- The local database mirrors state and drives automation. All actions must be written back to RPC when applicable.

## Shared State (Database Tables)
- Core entities: projects, chapters, rights_items
- Rightsholders and routing: publishers, publisher_name_mappings, rightsholders, created_types, crossref_cache
- Requests and comms: permission_requests, emails, chasers, rightslink_sessions
- Fees and finance: fee_records, invoices, budget_transactions, currencies
- Evidence and reports: documents, license_checks
- Orchestration and audit: workflow_executions, workflow_steps, scheduled_tasks, rpc_sync, elsa_sync, status_history, audit_log, api_logs

## Agent Roles
- Coordinator Agent: orchestration, priorities, scheduling, idempotency, SLA risk
- Intake and Sync Agent: RPC, ELSA, EMSS ingestion and sync
- Inventory and Log Agent: permission log and manuscript parsing, chapter tracker maintenance
- Research and Classification Agent: rightsholder identification, STM rules, routing
- Outreach and Response Agent: outbound requests, reminders, response capture
- Finance and Approval Agent: fees, approvals, invoices, budgets
- Evidence and Reporting Agent: evidence validation, reports, closure

## Integrations (Plugin Names)
- rpc-sync: RPC project, items, logs, documents, report send
- elsa-export: permission log exports, chapter metadata
- emss-ingest: manuscript and project metadata for HS
- rightslink-automation: CCC RightsLink quoting and licensing
- stm-guidelines: STM member list and opt-in or opt-out status
- outlook-mail: outbound and inbound email
- crossref-lookup: DOI and publisher metadata
- pubmed-lookup: medical citation verification
- image-finder: internal Elsevier asset lookup
- publisher-portal-form: publisher web form submissions
- file-storage: persistent storage for logs, licenses, reports, screenshots

## Templates (Email)
- Intro email to authors (Tier 1 and chapter tracking)
- Permission request email to rightsholders
- Credit line change email
- Weekly Status Report (WSR)
- Project completion email with permission log and cost sheet
- Reminder and chaser sequence (first reminder, second reminder, first chaser, second chaser, third chaser)

## Default Email Addresses
- Permission requests: permissionseeking@elsevier.com
- Permissions helpdesk: permissionshelpdesk@elsevier.com
- RPC notifications: rpcapplication@elsevier.com

## Artifact Recording Model (Table-Based)
- All operational artifacts are represented as records in documents with metadata fields such as document_type, document_category, title, file_url or file_path, and tags.
- File naming conventions only apply when exporting or uploading files into external systems that require a filename (RPC uploads, emailed attachments, or external portals). If the system stores only metadata, filenames are optional.
- Examples of exported filenames, if required:
  - Permission log: [ISBN]_RPC-PermLog.xlsx
  - Cost sheet: [ISBN]_Cost Sheet.xlsx
  - Analysis report: Analysis Report - [Author Name]: [Title], [ISBN]
  - WSR report: Weekly Status Report - [Book Title], [Edition], [ISBN]
  - Credit line change report: Credit Line Change - [Book Title], [ISBN]

## Status and Value Mapping

### Internal Statuses (rights_items.status)
- yet_to_apply
- pending
- resolved
- waiver
- editorial_query
- author_query
- deleted

### RPC Status Mapping
- RPC New or In Progress -> rights_items.status = yet_to_apply or pending
- RPC Pending Response -> rights_items.status = pending
- RPC Escalated -> rights_items.status = editorial_query or author_query
- RPC Resolved -> rights_items.status = resolved
- RPC Granted -> rights_items.status = resolved
- RPC Denied -> rights_items.status = editorial_query (replacement decision)
- RPC Not Needed -> rights_items.status = waiver

### Mode of Contact Values
- RightsLink, CCC, WebForm, Email, None

### Permission Log Status Values
- Resolved -> rights_items.status = resolved
- Pending -> rights_items.status = pending
- Yet to Apply -> rights_items.status = yet_to_apply
- Editorial or Author Query -> rights_items.status = editorial_query or author_query
- Waiver -> rights_items.status = waiver
- Deleted -> rights_items.status = deleted

## Classification and Rules

### Created Types (Required List)
- AUTHOR_CREATED: no permission required
- ELSEVIER_BOOKS: no permission required
- ELSEVIER_JOURNALS: no permission required
- COURTESY_INDIVIDUAL: verify existing permission
- COURTESY_COMPANY: verify existing permission
- ADAPTED: permission required
- MODIFIED: permission required
- REDRAWN: permission required depends on extent of changes
- THIRD_PARTY: permission required
- STM_OPT_OUT: no permission required
- STM_NOT_OPT_OUT: notification only
- UNRESTRICTED: no permission required
- PUBLIC_DOMAIN: no permission required
- DATA_FROM: credit only
- MULTIPLE_SOURCES: check each source
- RESOLVED_BY_AUTHOR: verify existing permission

### STM Guidelines Thresholds
- Figures or tables: up to 3 per journal article or book chapter
- Text: up to 400 words per extract or 800 words total for journal articles
- STM applies only when the source publisher is a member and use is scholarly
- If STM thresholds exceeded, treat as permission required

### Mode of Contact Routing (Priority)
1) STM route (notification-only or no request based on opt-out logic)
2) CCC RightsLink (quote and license)
3) Publisher portal web form
4) Direct email outreach

### Rule of 10
- Applies when 10 or fewer items are reused from a single source book
- If the count exceeds 10, escalate to bulk publisher request
- Document the assessment and any escalation in rights_items.comments and documents

### Fee Handling Rules
- If fee <= projects.max_cost_per_item and total spend <= projects.permission_budget, auto-approve
- If fee exceeds per-item or project budget, set rights_items.status = editorial_query
- If fee exceeds total budget, recommend replacement or deletion

### License Compatibility Matrix
- CC-BY-4.0: commercial use allowed, modifications allowed, permission not required
- CC-BY-NC-4.0: permission required if commercial
- CC-BY-NC-ND-4.0: permission required if commercial or modified
- CC-BY-SA-4.0: permission not required but same license required
- All Rights Reserved: permission required

### Chaser Cadence (Current State)
- Chapter tracker cadence is date-driven, not fixed offsets
- Rights-item cadence defaults used when no chapter schedule exists:
  - Chaser 1: 14 days after request
  - Chaser 2: 28 days after request
  - Chaser 3: 42 days after request (final email + phone attempt)
  - Escalation: 60 days after request (editorial decision)
- HS Tier 4 and general follow-up guidance also shows 0, 7, 14, 21, 28 day pattern; use project deadlines to pick the most conservative schedule

## Data Mapping and Validation

### Project-Level Required Fields
- projects.project_title, projects.division, projects.tier
- projects.isbn, projects.publication_date, projects.permission_deadline
- projects.formats, projects.print_run, projects.language
- projects.permission_budget, projects.max_cost_per_item, projects.currency
- projects.cds_user_id, projects.cs_user_id (if assignment available)

### Rights Item Required Fields
- rights_items.item_id, rights_items.source_info, rights_items.caption
- rights_items.chapter_id (if chapter-based)
- rights_items.created_type, rights_items.permission_required
- rights_items.mode_of_contact, rights_items.status

### Permission Log Mapping (Excel -> Tables)
- Project ID or Publication Name -> projects.id and rights_items.project_id
- Permission Status -> rights_items.status
- Chapter Title -> chapters.chapter_title and rights_items.chapter_id
- Elsevier Author Name -> chapters.author_name
- Item ID -> rights_items.item_id
- Previous Edition Item ID -> rights_items.previous_edition_item_id
- Caption Title -> rights_items.caption
- Source -> rights_items.source_info
- Source Chapter -> chapters.chapter_number or documents.tags.source_chapter
- Original Figure Number -> rights_items.original_figure_number
- Rightsholder -> rightsholders.name and rights_items.rightsholder_id
- Permission Required -> rights_items.permission_required
- Creator Type -> rights_items.created_type
- Rightsholder Web Link -> rights_items.rightsholder_web_link
- Mode of Contact -> rights_items.mode_of_contact
- Rightsholder Email -> rightsholders.contact_email
- Applied Date -> rights_items.apply_date
- Resolved Date -> rights_items.resolve_date
- Email Chaser dates -> rights_items.chaser1_date, chaser2_date, chaser3_date
- Restrictions -> rights_items.restrictions
- Invoice Amount, Currency -> fee_records.fee_amount, fee_records.fee_currency
- Invoice Number -> invoices.invoice_number
- Invoice Processing Mode -> invoices.processing_mode
- Invoice Processed Date -> invoices.paid_at
- Invoice Status -> invoices.status

### Chapter Tracker Mapping
- chapters.intro_email_due_date, intro_email_sent_date
- chapters.ms_due_date, ms_received_date
- chapters.first_reminder_due_date, first_reminder_sent_date
- chapters.second_reminder_due_date, second_reminder_sent_date
- chapters.first_chaser_due_date, first_chaser_sent_date
- chapters.second_chaser_due_date, second_chaser_sent_date
- chapters.permission_log_received, permission_files_received, chapter_submitted
- chapters.permissions_status, status, tracker_comments

### ELSA Export to RPC Conversion
- Export only when ELSA status allows reporting (Staff Review or later)
- If item IDs missing, generate stable IDs before upload
- If source strings incomplete, enrich via crossref-lookup or pubmed-lookup
- Ensure chapter mapping is consistent; unique item IDs across chapters

## Trigger Model
Triggers are grouped into event-based, state-based, time-based, and failure-based categories. Each flow lists the trigger types it responds to.

### Event-Based Triggers
- ProjectCreatedOrUpdated: rpc_sync or elsa_sync has new project data
- PermissionLogUploaded: documents.document_type = permission_log
- ManuscriptReceived: documents.document_type = manuscript or art_file
- ELSAPermissionFilesUploaded: documents.document_type = license_file from ELSA
- InboundEmailReceived: emails.direction = inbound
- RightsLinkEvent: rightslink_sessions.status changes or confirmation_number set
- EditorialDecision: rights_items.comments or internal decision record received

### State-Based Triggers
- UnclassifiedRightsItem: rights_items.created_type or permission_required is null
- ReadyToRequest: rights_items.status = yet_to_apply and permission_required = true
- PendingChaserDue: rights_items.status = pending and next_chaser_due reached
- FeeApprovalPending: fee_records.approval_status = pending
- ProjectReadyToClose: all rights_items are resolved, waiver, or deleted
- SyncStale: rpc_sync.last_sync_at older than SLA

### Time-Based Triggers
- ScheduledChaser: scheduled_tasks.task_type = chaser and next_run_at reached
- DeadlineRisk: projects.permission_deadline within threshold
- WeeklyStatusReport: scheduled weekly task for reporting
- SyncRetry: scheduled_tasks.task_type = sync and next_run_at reached

### Failure-Based Triggers
- SyncFailure: rpc_sync.sync_status = failed or elsa_sync.sync_status = failed
- EmailFailure: emails.status = failed or bounced
- RightsLinkFailure: rightslink_sessions.status = error

## Flow 1: Intake and Sync
Purpose
- Create or refresh project and chapter state in the local system.

Trigger Types
- Event-based: ProjectCreatedOrUpdated
- State-based: SyncStale
- Time-based: SyncRetry
- Failure-based: SyncFailure

Agents
- Intake and Sync Agent, Coordinator Agent

Integrations
- rpc-sync, elsa-export, emss-ingest

Steps
1) Pull project metadata from RPC, ELSA, or EMSS.
   Writes: projects (project_title, division, tier, isbn, publication_date, permission_deadline, permission_budget, max_cost_per_item, formats, print_run, submission_route), audit_log.
2) Create or update chapters if provided.
   Writes: chapters (chapter_number, chapter_title, author_name, author_email, ms_due_date), audit_log.
3) Record sync metadata and hash for conflict detection.
   Writes: rpc_sync or elsa_sync (sync_status, last_sync_at, local_hash, remote_hash, pending_changes), api_logs.
4) Start workflow execution and mark project active.
   Writes: workflow_executions, workflow_steps, projects.status = active, status_history.

Outputs
- Project and chapters are current and eligible for downstream flows.

## Flow 2: Inventory and Log Processing
Purpose
- Convert incoming logs or manuscripts into rights_items.

Trigger Types
- Event-based: PermissionLogUploaded, ManuscriptReceived, ELSAPermissionFilesUploaded
- State-based: projects.initial_log_attached = false with available sources

Agents
- Inventory and Log Agent

Integrations
- rpc-sync, elsa-export, emss-ingest, file-storage

Steps
1) Download and store the source artifact.
   Writes: documents (document_type = permission_log or manuscript or art_file, document_category = input, file_url or file_path).
2) Parse permission log into rights_items.
   Writes: rights_items (item_id, previous_edition_item_id, caption, source_info, original_figure_number, chapter_id, status = yet_to_apply), status_history.
3) For Tier 3, create a new RPC-format permission log from manuscript extraction.
   Writes: documents (document_type = permission_log, document_category = working).
4) Update chapter tracker fields if chapter-based.
   Writes: chapters (intro_email_due_date, first_reminder_due_date, second_reminder_due_date, first_chaser_due_date, second_chaser_due_date, permission_log_received, permission_files_received, tracker_comments).
5) Mark project log attachment state.
   Writes: projects.initial_log_attached = true, audit_log.

Outputs
- Rights items and chapter tracker are populated.

## Flow 3: Research and Classification
Purpose
- Determine permission requirement, rightsholder, and routing.

Trigger Types
- State-based: UnclassifiedRightsItem
- Event-based: EditorialDecision (classification overrides)

Agents
- Research and Classification Agent

Integrations
- crossref-lookup, pubmed-lookup, image-finder, stm-guidelines

Steps
1) Classify created_type and permission_required using created_types.
   Writes: rights_items (created_type, permission_required, notification_required), status_history.
2) Enrich metadata using research sources.
   Writes: crossref_cache (doi, publisher_name, title, journal_name, publication_year), rights_items (doi, article_title, journal_name, publication_year, identification_confidence).
3) Map publisher to rightsholder and STM status.
   Writes: publishers (stm_status, rightslink_enabled, permissions_url), rightsholders (publisher_id, contact_email), rights_items (rightsholder_id).
4) Apply STM thresholds and notification logic.
   Writes: rights_items (permission_required, notification_required, status = waiver if STM notification only).
5) Select mode_of_contact.
   Writes: rights_items (mode_of_contact).

Outputs
- Items are routed to the correct execution path or closed as no permission needed.

## Flow 4: Permission Request Execution
Purpose
- Create and send outbound permission requests.

Trigger Types
- State-based: ReadyToRequest
- Event-based: EditorialDecision (manual request requested)

Agents
- Outreach and Response Agent

Integrations
- rightslink-automation, publisher-portal-form, outlook-mail

Steps
1) Build the outbound request package with project usage details.
   Fields used: book title, edition, ISBN, format, distribution, publication date, permission deadline, print run, chapter, item image.
2) Create permission request record.
   Writes: permission_requests (rights_item_id, request_type, mode_of_contact, request_content, submitted_at, status = sent).
3) Send request through the selected channel.
   Writes: emails (direction = outbound, subject, body_text or body_html, status), rightslink_sessions (order_id, confirmation_number), permission_requests (email_message_id, rightslink_confirmation, form_submission_id).
4) Mark item as pending and schedule follow-up.
   Writes: rights_items (status = pending, apply_date, next_chaser_due), chasers or scheduled_tasks, status_history.

Outputs
- Requests are sent and tracked per item.

## Flow 5: Follow-Up and Escalation
Purpose
- Drive the reminder cadence and escalate unresponsive items.

Trigger Types
- State-based: PendingChaserDue
- Time-based: ScheduledChaser
- Failure-based: EmailFailure

Agents
- Outreach and Response Agent, Coordinator Agent

Integrations
- outlook-mail

Steps
1) Create a chaser record for the next scheduled reminder.
   Writes: chasers (rights_item_id, chaser_number, scheduled_date, status = scheduled).
2) Send the reminder email.
   Writes: emails (template_id, status = sent, sent_at), chasers (status = sent, sent_at).
3) Update chaser counters and due dates.
   Writes: rights_items (chaser_count, chaser1_date, chaser2_date, chaser3_date, next_chaser_due).
4) Attempt alternate contacts and phone if no response.
   Writes: rights_items.internal_notes, emails (alternate contact attempts).
5) Escalate after full cadence.
   Writes: rights_items (status = editorial_query or author_query, comments), emails (escalation notice), status_history.

Outputs
- Items remain active until resolved or escalated.

## Flow 6: Response Handling
Purpose
- Capture responses and update item outcomes.

Trigger Types
- Event-based: InboundEmailReceived, RightsLinkEvent

Agents
- Outreach and Response Agent

Integrations
- outlook-mail, rightslink-automation

Steps
1) Capture response details.
   Writes: permission_requests (response_received, response_date, response_content, response_type, status = responded).
2) Apply outcome.
   Writes: rights_items (status = resolved and resolve_date if granted; editorial_query if denied; restrictions and credit_line_change if required).
3) Store evidence and validation details.
   Writes: documents (permission_grant, correspondence, license_file), license_checks (license_type, permission_needed, license_verified), status_history.

Outputs
- Requests are resolved or moved into a decision path with evidence attached.

## Flow 7: Fees and Approvals
Purpose
- Capture fee quotes, enforce budgets, and manage invoices.

Trigger Types
- Event-based: RightsLinkEvent, InboundEmailReceived (fee quote)
- State-based: FeeApprovalPending

Agents
- Finance and Approval Agent

Integrations
- rightslink-automation, outlook-mail

Steps
1) Record fee quote and evaluate thresholds.
   Writes: fee_records (fee_amount, fee_currency, quote_reference, within_item_limit, within_project_budget, approval_status), rights_items (fee_record_id).
2) Auto-approve or request approval.
   Writes: fee_records (approval_status), rights_items (status = editorial_query if approval required), emails (approval request).
3) After approval, create invoice and update budget.
   Writes: invoices (fee_record_id, amount, currency, status), budget_transactions (amount, balance_before, balance_after), status_history.
4) If rejected, mark for replacement or deletion.
   Writes: fee_records (approval_status = rejected), rights_items (status = editorial_query or deleted), emails (decision notice).

Outputs
- Fees are controlled and approvals are captured before payment.

## Flow 8: Evidence and Reporting
Purpose
- Validate evidence, generate reports, and update stakeholders.

Trigger Types
- State-based: rights_items.status = resolved or waiver
- Time-based: WeeklyStatusReport, DeadlineRisk

Agents
- Evidence and Reporting Agent

Integrations
- rpc-sync, outlook-mail, file-storage

Steps
1) Validate license scope and credit line rules.
   Writes: license_checks (commercial_use_allowed, modifications_allowed, permission_needed), rights_items (restrictions, credit_line_change).
2) Upload evidence and working artifacts.
   Writes: documents (permission_log, cost_sheet, credit_line_report, analysis_report, wsr_report).
3) Generate analysis report fields.
   Required data: total items, permissions to be cleared, elsevier permissions, third party split, high fee items, high TAT holders, restriction list, chapter author info, estimated completion date.
4) Generate weekly status report fields.
   Required data: total items, permissions to be worked, processed, resolved, yet to be resolved, in query, yet to apply, publication date, last batch received date, project deadline, invoice spend to date.
5) Send reports to stakeholders.
   Writes: emails (WSR, analysis report), status_history.

Outputs
- Reporting and evidence are complete and auditable.

## Flow 9: Project Closure
Purpose
- Close the project when all items are dispositioned and evidence is complete.

Trigger Types
- State-based: ProjectReadyToClose

Agents
- Evidence and Reporting Agent, Coordinator Agent

Integrations
- rpc-sync, outlook-mail

Steps
1) Validate completion readiness.
   Checks: all rights_items terminal, all licenses uploaded, paid items have invoices, credit line changes communicated, final permission log attached.
   Writes: audit_log (completion readiness check).
2) Close project.
   Writes: projects (status = completed, completion_date), status_history.
3) Send completion email with final log and cost sheet if exported.
   Writes: emails (completion), documents (final permission_log and cost_sheet).

Outputs
- Project closed in the system of record with full evidence.

## Flow 10: Audit and Observability
Purpose
- Maintain a complete audit trail for all actions and integrations.

Trigger Types
- Event-based: Any state change
- Failure-based: Any integration error

Agents
- Coordinator Agent

Integrations
- None

Steps
1) Record status transitions.
   Writes: status_history (entity_type, entity_id, old_status, new_status, reason).
2) Record change details and external calls.
   Writes: audit_log, api_logs, workflow_executions, workflow_steps.

Outputs
- Full audit trail for compliance and debugging.

## Flow 11: Sync Retry and Failure Recovery
Purpose
- Recover from RPC or ELSA sync failures without manual intervention.

Trigger Types
- Failure-based: SyncFailure
- Time-based: SyncRetry

Agents
- Intake and Sync Agent, Coordinator Agent

Integrations
- rpc-sync, elsa-export

Steps
1) Mark sync failure and store error details.
   Writes: rpc_sync or elsa_sync (sync_status = failed, error_message, retry_count), api_logs.
2) Schedule retry.
   Writes: scheduled_tasks (task_type = sync, next_run_at, status = active).
3) Retry sync and update outcome.
   Writes: rpc_sync or elsa_sync (sync_status = success or failed, last_sync_at), workflow_steps.

Outputs
- Sync failures are retried and recovered without human intervention.

## Tier-Specific Flow Overrides

### HS Tier 4 Flow
- Input: CDS permission log from RPC.
- Uses flows 1 to 9 with full outreach, STM routing, chasers, fee handling, reporting, and closure.

### HS Tier 0 Flow
- Input: author or CDS permission log and licenses.
- Uses flows 1, 2, 3, 8, and 9. No outbound requests.

### HS Rule of 10 Flow
- Input: list of reused items from one source.
- Uses flows 1, 2, 3, and 8. If threshold exceeded, uses flows 4 to 7 for bulk permissions.

### S&T Tier 1 Flow
- Input: author-driven permissions and chapter tracker.
- Uses flows 1, 2, 5, 8, and 9. No outbound requests unless validation fails.

### S&T Tier 2 Flow
- Input: author log via ELSA export.
- Uses flows 1 to 9 with log conversion and full outreach.

### S&T Tier 3 Flow
- Input: manuscript only.
- Uses flows 1 to 9 with log creation and full outreach.

## Completion Criteria (Global)
- All rights_items are in resolved, waiver, or deleted status with approval if required.
- Evidence and reporting artifacts are recorded in documents.
- Fees and invoices are recorded for paid permissions.
- Audit and status history are complete for all transitions.
