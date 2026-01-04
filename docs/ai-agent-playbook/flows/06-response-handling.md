# Flow 06 - Response Handling

## Purpose
Capture inbound responses, apply outcomes, and store evidence.

## Trigger Types
- Event-based: InboundEmailReceived, RightsLinkEvent

## Agents
- Outreach and Response Agent

## Integrations
- outlook-mail
- rightslink-automation

## Inputs and Preconditions
- permission_requests.status = sent
- Inbound response from email or portal

## Steps
1) Capture response details.
   - Parse response content, terms, and restrictions.
2) Update permission request.
   - Set response_received, response_date, response_type, response_content.
3) Apply outcome to rights item.
   - Granted: status = resolved, resolve_date set.
   - Denied: status = editorial_query; replacement decision required.
   - Conditional: status = editorial_query if terms not acceptable.
4) Store evidence and license checks.
   - Upload permission grants, correspondence, and license files.
   - Record license scope checks and credit line requirements.

## Table Updates
- permission_requests: response_received, response_date, response_type, response_content, status
- rights_items: status, resolve_date, restrictions, credit_line_change
- documents: document_type = permission_grant, license_file, correspondence
- license_checks: license_type, permission_needed, license_verified, commercial_use_allowed, modifications_allowed
- status_history and audit_log

## Outputs
- Items are resolved or moved into an editorial decision state with evidence captured.

## Decision Rules
- License scope must match project usage (format, distribution, editions, translations).
- Credit line changes must be captured and communicated.

## Human Decision Points
- Acceptance of conditional permissions or restrictive terms.
