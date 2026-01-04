# Flow 08 - Evidence and Reporting

## Purpose
Validate evidence, generate reports, and communicate status to stakeholders.

## Trigger Types
- State-based: rights_items.status = resolved or waiver
- Time-based: WeeklyStatusReport, DeadlineRisk

## Agents
- Evidence and Reporting Agent

## Integrations
- rpc-sync
- outlook-mail
- file-storage

## Inputs and Preconditions
- Resolved or waived rights items
- Project nearing deadline or weekly reporting schedule

## Steps
1) Validate license scope and credit line requirements.
   - Check format, distribution, editions, translations, and restrictions.
2) Upload evidence artifacts.
   - Permission grants, license files, correspondence.
3) Generate analysis report fields.
   - Total items, permissions to be cleared, Elsevier permissions, third-party split, high fee items, high TAT holders, restriction list, chapter author information, estimated completion date.
4) Generate weekly status report fields.
   - Total items, permissions to be worked, processed, resolved, yet to be resolved, in query, yet to apply, publication date, last batch received date, project deadline, invoice spend to date.
5) Send reports to stakeholders.

## Table Updates
- license_checks: license_type, license_verified, permission_needed, commercial_use_allowed, modifications_allowed
- documents: permission_log, cost_sheet, credit_line_report, analysis_report, wsr_report
- emails: WSR and analysis report distribution
- status_history and audit_log

## Outputs
- Evidence is complete and reports are delivered.

## Decision Rules
- Credit line changes must be communicated to rightsholders and editorial.
- Reporting cadence can be adjusted based on project risk or editorial request.

## Human Decision Points
- None; reporting content is deterministic.
