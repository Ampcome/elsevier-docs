# Flow HS Tier 0 - Validation Only

## Purpose
Author or CDS obtains permissions; AI validates logs and evidence and uploads to RPC.

## Trigger Types
- Event-based: ProjectCreatedOrUpdated, PermissionLogUploaded, ELSAPermissionFilesUploaded

## Agents
- Intake and Sync Agent
- Inventory and Log Agent
- Evidence and Reporting Agent

## Integrations
- rpc-sync, outlook-mail

## Steps
1) Intake project and confirm tier = Tier0.
2) Download permission log and licenses from RPC or author.
3) Validate completeness and scope.
4) Upload logs and evidence to RPC and mark items resolved or waived.
5) Generate reports if required and close project.

## Table Updates
- documents, rights_items, license_checks, projects, status_history

## Decision Rules
- If license scope does not match project usage, escalate to editorial or CDS.

## Human Decision Points
- Any license scope exceptions or missing evidence.
