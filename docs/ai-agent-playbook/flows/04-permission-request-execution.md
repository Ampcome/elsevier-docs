# Flow 04 - Permission Request Execution

## Purpose
Generate and send permission requests through the correct channel and set pending status with follow-up schedules.

## Trigger Types
- State-based: ReadyToRequest
- Event-based: EditorialDecision (manual request requested)

## Agents
- Outreach and Response Agent

## Integrations
- rightslink-automation
- publisher-portal-form
- outlook-mail

## Inputs and Preconditions
- rights_items.permission_required = true
- rights_items.mode_of_contact is set
- rightsholder contact data is available

## Steps
1) Build the request package.
   - Include book title, edition, ISBN, format (print, electronic, both), distribution (worldwide), chapter title and author, publication date, permission deadline, print run, and requested reuse scope.
2) Create permission_requests record.
   - Set request_type, mode_of_contact, request_content, submitted_at, status = sent.
3) Execute via channel.
   - RightsLink: requestor type = STM Publisher, reuse type = Book or Textbook, format = print or electronic or both, print run, translation, territory = worldwide.
   - Web form: submit required fields and capture form_submission_id.
   - Email: send permission request using template and include figure image if required.
4) Update rights_items.
   - Set status = pending, apply_date, next_chaser_due.
5) Schedule follow-ups.
   - Create chasers or scheduled_tasks based on cadence.

## Table Updates
- permission_requests: rights_item_id, request_type, mode_of_contact, request_content, submitted_at, status
- emails: direction = outbound, to_address, subject, body_text or body_html, status, message_id
- rightslink_sessions: order_id, confirmation_number, fee_quoted, fee_amount, fee_currency, status
- rights_items: status = pending, apply_date, next_chaser_due, mode_of_contact
- chasers or scheduled_tasks
- status_history and audit_log

## Outputs
- Requests are sent and tracked for each item.

## Decision Rules
- Contact routing priority: STM route, RightsLink, web form, direct email.
- Use RightsLink only when publisher supports it and terms are acceptable.
- If STM notification-only applies, no request is sent; item is waived.

## Human Decision Points
- None for standard routing; exceptions are flagged for review.
