# Flow HS Rule of 10

## Purpose
Assess reuse volume from a single source book and determine whether permission seeking is required.

## Trigger Types
- Event-based: ProjectCreatedOrUpdated, PermissionLogUploaded
- State-based: UnclassifiedRightsItem

## Agents
- Inventory and Log Agent
- Research and Classification Agent
- Evidence and Reporting Agent

## Integrations
- rpc-sync

## Steps
1) Identify items sourced from the same publication.
2) Count occurrences of reused items.
3) If count <= 10, document compliance and mark as waiver.
4) If count > 10, initiate bulk permission request and track as a grouped request.
5) Upload assessment and evidence to RPC.

## Table Updates
- rights_items (status, comments)
- documents (assessment notes)
- status_history

## Decision Rules
- Rule of 10 applies only to reuse from a single source book.
- If threshold exceeded, escalate to publisher request.

## Human Decision Points
- Replacement or deletion decisions when bulk permissions are not feasible.
