# Flow 05 - Follow-Up and Escalation

## Purpose
Send reminders, chasers, and escalate unresponsive rights items.

## Trigger Types
- State-based: PendingChaserDue
- Time-based: ScheduledChaser
- Failure-based: EmailFailure

## Agents
- Outreach and Response Agent
- Coordinator Agent

## Integrations
- outlook-mail

## Inputs and Preconditions
- rights_items.status = pending
- next_chaser_due is set or chapter tracker dates exist

## Steps
1) Determine the next follow-up date.
   - Use chapter tracker dates when available.
   - If not, use default rights-item cadence: 14, 28, 42 days; escalation at 60 days.
2) Create chaser record.
   - Set chaser_number and scheduled_date.
3) Send reminder email.
   - Use the appropriate template (first reminder, second reminder, first chaser, second chaser, third chaser).
4) Update chaser status and rights item dates.
   - Update chaser1_date, chaser2_date, chaser3_date and next_chaser_due.
5) Escalate when cadence is exhausted.
   - Attempt alternate email and phone contact.
   - Move to editorial_query and notify CDS or editorial for replacement or deletion.

## Table Updates
- chasers: chaser_number, scheduled_date, status, sent_at
- emails: template_id, direction = outbound, status, sent_at
- rights_items: chaser_count, chaser1_date, chaser2_date, chaser3_date, next_chaser_due, status
- status_history and audit_log

## Outputs
- Items are actively pursued and escalated when unresponsive.

## Decision Rules
- Escalation path: alternate email, phone attempt, mark editorial query, recommend replacement or deletion.
- Deadlines may tighten cadence if permission_deadline is approaching.

## Human Decision Points
- Replacement or deletion decision after escalation.
