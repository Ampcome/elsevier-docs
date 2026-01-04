# Agent Runbook - Evidence and Reporting Agent

## Purpose
Validate evidence, generate reports, and close projects.

## Primary Responsibilities
- Validate license scope and credit line requirements.
- Upload evidence artifacts and reports.
- Generate analysis and WSR outputs.
- Close projects when all items are terminal.

## Trigger Types
- State-based: rights_items.status = resolved or waiver, ProjectReadyToClose
- Time-based: WeeklyStatusReport, DeadlineRisk

## Flows Covered
- Flow 08: Evidence and Reporting
- Flow 09: Project Closure

## Tables Read
- rights_items, projects, documents

## Tables Written
- documents: permission_log, cost_sheet, credit_line_report, analysis_report, wsr_report
- license_checks: license_verified, permission_needed, commercial_use_allowed, modifications_allowed
- projects: status = completed, completion_date
- emails: WSR, completion email
- status_history, audit_log

## Integrations
- rpc-sync
- outlook-mail
- file-storage

## Idempotency Rules
- Do not upload duplicate reports for the same period unless versioned.
- Close project only once and only when closure checklist is satisfied.

## Failure Handling
- If reports fail to generate, retry and log in api_logs.

## Human Decision Points
- None when evidence is complete; escalate only if required artifacts are missing.
