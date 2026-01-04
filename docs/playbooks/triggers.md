# Triggers Overview

This page summarizes the trigger types used across all flows. These triggers make the system autonomous by automatically dispatching the right agent when data changes or deadlines arrive.

## Event-Based Triggers
- ProjectCreatedOrUpdated: inbound RPC/ELSA/EMSS project assignment or update.
- PermissionLogUploaded: permission log attached or available for download.
- ManuscriptReceived: manuscript or art files available.
- ELSAPermissionFilesUploaded: author uploads licenses or permissions files.
- InboundEmailReceived: rightsholder or author reply received.
- RightsLinkEvent: RightsLink quote, order confirmation, or license issuance.
- EditorialDecision: approval, replacement, deletion, or credit line change decision received.

## State-Based Triggers
- UnclassifiedRightsItem: rights_items missing created_type, permission_required, rightsholder_id, or mode_of_contact.
- ReadyToRequest: rights_items.status = yet_to_apply and permission_required = true.
- PendingChaserDue: rights_items.status = pending and next_chaser_due reached.
- FeeApprovalPending: fee_records.approval_status = pending.
- ProjectReadyToClose: all rights_items are resolved, waiver, or deleted.
- SyncStale: rpc_sync or elsa_sync last_sync_at older than the allowed interval.

## Time-Based Triggers
- ScheduledChaser: scheduled_tasks task due for reminders.
- DeadlineRisk: projects.permission_deadline within warning threshold.
- WeeklyStatusReport: scheduled weekly WSR generation.
- SyncRetry: scheduled sync retry after failure.

## Failure-Based Triggers
- SyncFailure: rpc_sync or elsa_sync sync_status = failed.
- EmailFailure: emails.status = failed or bounced.
- RightsLinkFailure: rightslink_sessions.status = error.
