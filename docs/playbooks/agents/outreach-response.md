# Agent Runbook - Outreach and Response Agent

## Purpose
Send permission requests, manage chasers, and process inbound responses.

## Primary Responsibilities
- Create permission_requests and send outbound communications.
- Schedule and send reminders and chasers.
- Capture inbound responses and update rights items.
- Upload evidence and correspondence.

## Trigger Types
- State-based: ReadyToRequest, PendingChaserDue
- Event-based: InboundEmailReceived, RightsLinkEvent
- Time-based: ScheduledChaser
- Failure-based: EmailFailure

## Flows Covered
- Flow 04: Permission Request Execution
- Flow 05: Follow-Up and Escalation
- Flow 06: Response Handling

## Tables Read
- rights_items, rightsholders, email_templates
- permission_requests, emails, chasers

## Tables Written
- permission_requests: request_type, mode_of_contact, status, response fields
- emails: direction, subject, body, status, sent_at
- chasers: chaser_number, scheduled_date, status
- rights_items: status, apply_date, resolve_date, restrictions, credit_line_change, chaser dates
- documents: permission_grant, correspondence, license_file
- status_history, audit_log

## Integrations
- outlook-mail
- rightslink-automation
- publisher-portal-form

## Idempotency Rules
- Do not send duplicate requests for the same rights_item.
- Do not send a chaser if an open chaser already exists for the same cadence step.

## Failure Handling
- On email failure, try alternate contact, then escalate.
- On RightsLink error, retry or route to portal or email.

## Human Decision Points
- Replacement or deletion decisions after escalation.
- Acceptability of conditional permissions.
