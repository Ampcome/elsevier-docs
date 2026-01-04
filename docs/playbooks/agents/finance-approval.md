# Agent Runbook - Finance and Approval Agent

## Purpose
Manage fees, approvals, invoices, and budget transactions.

## Primary Responsibilities
- Create fee records from quotes.
- Enforce project budget rules.
- Generate invoices and update budget transactions.

## Trigger Types
- Event-based: RightsLinkEvent, InboundEmailReceived (fee quote)
- State-based: FeeApprovalPending

## Flows Covered
- Flow 07: Fees and Approvals

## Tables Read
- rights_items, projects, fee_records

## Tables Written
- fee_records: fee_amount, fee_currency, approval_status, approved_at, approved_by
- rights_items: fee_record_id, status = editorial_query when approval needed
- invoices: amount, currency, processing_mode, status, paid_at
- budget_transactions: transaction_type, amount, balance_before, balance_after
- status_history, audit_log

## Integrations
- rightslink-automation
- outlook-mail

## Idempotency Rules
- One fee_record per rights_item per quote.
- One invoice per fee_record unless updated with new invoice number.

## Failure Handling
- If approvals stall, re-notify CDS or editorial.

## Human Decision Points
- Fee approvals and replacement decisions.
