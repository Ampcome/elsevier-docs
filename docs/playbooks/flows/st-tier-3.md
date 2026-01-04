# Flow S&T Tier 3 - Full Service

## Purpose
Author submits manuscript only; AI builds the permission log and seeks permissions.

## Trigger Types
- Event-based: ProjectCreatedOrUpdated, ManuscriptReceived

## Agents
- Intake and Sync Agent
- Inventory and Log Agent
- Research and Classification Agent
- Outreach and Response Agent
- Finance and Approval Agent
- Evidence and Reporting Agent

## Integrations
- emss-ingest or elsa-export
- rpc-sync
- stm-guidelines
- rightslink-automation
- outlook-mail
- crossref-lookup
- pubmed-lookup

## Steps
1) Intake project and confirm tier = Tier3.
2) Extract all third-party items from manuscript and art files.
3) Create a new RPC-format permission log with stable item IDs.
4) Enrich citations and identify rightsholders.
5) Execute permissions seeking using Flow 4 through Flow 8.

## Table Updates
- rights_items, documents, permission_requests, emails, chasers, fee_records, invoices

## Decision Rules
- Deduplicate items that appear across chapters or versions.
- Ambiguous courtesy attributions require additional research.

## Human Decision Points
- Manual review for ambiguous sources or unclear rights ownership.
