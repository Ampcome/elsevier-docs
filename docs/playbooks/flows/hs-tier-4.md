# Flow HS Tier 4 - Full Service

## Purpose
CDS provides permission log; AI seeks permissions end-to-end.

## Trigger Types
- Event-based: ProjectCreatedOrUpdated, PermissionLogUploaded
- State-based: ReadyToRequest

## Agents
- Intake and Sync Agent
- Inventory and Log Agent
- Research and Classification Agent
- Outreach and Response Agent
- Finance and Approval Agent
- Evidence and Reporting Agent

## Integrations
- rpc-sync, stm-guidelines, rightslink-automation, outlook-mail, publisher-portal-form, crossref-lookup, pubmed-lookup

## Steps
1) Intake project from RPC and confirm tier = Tier4.
2) Download CDS permission log from RPC and parse into rights_items.
3) Classify each item and identify rightsholders.
4) Route each item via STM, RightsLink, portal, or email.
5) Send requests and track chasers based on project deadlines.
6) Capture responses and upload evidence.
7) Handle fees and approvals when required.
8) Generate analysis report and WSR as needed.
9) Close project when all items are resolved or dispositioned.

## Table Updates
- projects, rights_items, permission_requests, emails, chasers, rightslink_sessions, fee_records, invoices, documents, status_history

## Decision Rules
- Permission required is driven by creator type and source type.
- STM path depends on STM membership and opt-out logic.
- Fee approvals depend on project budget and per-item limits.
- Unresponsive rightsholders are escalated to CDS for replacement or deletion.

## Human Decision Points
- Fee exceptions and replacement or deletion decisions.
