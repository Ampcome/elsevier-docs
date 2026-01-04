# Flow 09 - Project Closure

## Purpose
Close the project when all rights items are dispositioned and evidence is complete.

## Trigger Types
- State-based: ProjectReadyToClose

## Agents
- Evidence and Reporting Agent
- Coordinator Agent

## Integrations
- rpc-sync
- outlook-mail

## Inputs and Preconditions
- All rights_items are resolved, waiver, or deleted with approval
- Evidence and reporting artifacts recorded in documents

## Steps
1) Validate closure readiness.
   - All items resolved or dispositioned.
   - Licenses and confirmations uploaded.
   - Paid items have invoice fields and cost sheet prepared.
   - Credit line changes communicated.
   - Final permission log uploaded.
2) Close project in local system and RPC.
3) Send completion email with final permission log and cost sheet if exported.

## Table Updates
- projects: status = completed, completion_date
- documents: final permission_log, cost_sheet
- emails: completion email
- status_history and audit_log

## Outputs
- Project closed in RPC and local system with full evidence.

## Decision Rules
- Completion only when closure readiness checklist is satisfied.

## Human Decision Points
- None if all prerequisites are met.
