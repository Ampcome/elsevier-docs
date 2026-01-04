# Flow 07 - Fees and Approvals

## Purpose
Capture fee quotes, enforce budget thresholds, and manage invoices and payments.

## Trigger Types
- Event-based: RightsLinkEvent, InboundEmailReceived (fee quote)
- State-based: FeeApprovalPending

## Agents
- Finance and Approval Agent

## Integrations
- rightslink-automation
- outlook-mail

## Inputs and Preconditions
- Fee quote present in rightslink_sessions or response content
- projects.permission_budget and projects.max_cost_per_item populated

## Steps
1) Record fee quote.
   - Capture fee amount, currency, and quote reference.
2) Evaluate budget thresholds.
   - Check per-item and project budget limits.
3) Decide path.
   - Auto-approve within limits and request CDS confirmation.
   - If over limits, set editorial_query and request approval.
   - If over project budget, recommend replacement or deletion.
4) Create invoice and update budget when approved.
   - Capture invoice number, processing mode, and status.

## Table Updates
- fee_records: fee_amount, fee_currency, fee_amount_usd, quote_reference, within_item_limit, within_project_budget, approval_status, approved_at, approved_by
- rights_items: fee_record_id, status = editorial_query if approval needed
- invoices: fee_record_id, amount, currency, processing_mode, status, invoice_number, paid_at
- budget_transactions: project_id, transaction_type, amount, balance_before, balance_after
- status_history and audit_log

## Outputs
- Fees are approved, recorded, and ready for payment processing.

## Decision Rules
- Fee <= max_cost_per_item and total spend <= permission_budget: auto-approve.
- Fee > max_cost_per_item or would exceed budget: editorial query.
- Fee > total budget: replacement or deletion recommended.

## Human Decision Points
- Editorial approval for fee exceptions and replacement decisions.
