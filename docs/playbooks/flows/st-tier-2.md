# Flow S&T Tier 2 - Author Log, AI Seeks

## Purpose
Author provides a log; AI converts to RPC format and seeks permissions.

## Trigger Types
- Event-based: ProjectCreatedOrUpdated, PermissionLogUploaded, ManuscriptReceived
- State-based: UnclassifiedRightsItem

## Agents
- Intake and Sync Agent
- Inventory and Log Agent
- Research and Classification Agent
- Outreach and Response Agent
- Finance and Approval Agent
- Evidence and Reporting Agent

## Integrations
- elsa-export
- rpc-sync
- stm-guidelines
- rightslink-automation
- outlook-mail
- crossref-lookup
- pubmed-lookup

## Steps
1) Wait until ELSA permissions report is available (Staff Review or later).
2) Export report and assess quality.
3) Convert ELSA export to RPC format.
   - Ensure item IDs exist and are stable.
   - Enrich missing source strings.
   - Normalize chapter mapping.
   - Apply created type classification.
4) Execute permissions seeking using Flow 4 through Flow 8.

## Table Updates
- rights_items, documents, permission_requests, emails, chasers, fee_records, invoices

## Decision Rules
- Missing item IDs must be generated before RPC upload.
- Incomplete source details require enrichment before outreach.

## Human Decision Points
- Manual review for incomplete or ambiguous ELSA exports.
