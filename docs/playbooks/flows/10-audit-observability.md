# Flow 10 - Audit and Observability

## Purpose
Maintain a complete audit trail for every state change and external call.

## Trigger Types
- Event-based: any state change
- Failure-based: any integration error

## Agents
- Coordinator Agent

## Integrations
- None

## Inputs and Preconditions
- Any update to projects, chapters, rights_items, permission_requests, emails, or finance data

## Steps
1) Record status transitions.
   - Capture old_status, new_status, and reason.
2) Record change details.
   - Store old_values, new_values, and changed_fields.
3) Log external calls.
   - Store request and response metadata.
4) Track workflow execution steps.
   - Record tool calls, inputs, outputs, and errors.

## Table Updates
- status_history: entity_type, entity_id, old_status, new_status, reason
- audit_log: entity_type, entity_id, changed_fields, old_values, new_values, source
- api_logs: api_name, endpoint, request, response, error_message
- workflow_executions and workflow_steps: status, error_message

## Outputs
- A complete audit trail for compliance and debugging.

## Decision Rules
- None. All changes must be recorded.

## Human Decision Points
- None.
