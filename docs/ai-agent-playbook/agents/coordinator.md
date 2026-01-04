# Agent Runbook - Coordinator Agent

## Purpose
Orchestrate the multi-agent system, enforce idempotency, schedule work, and manage SLA risk.

## Primary Responsibilities
- Start and track workflow_executions and workflow_steps for every run.
- Evaluate state-based triggers and dispatch work to the correct agent.
- Schedule time-based tasks (chasers, weekly reports, deadline checks, sync retries).
- Prevent duplicate actions across agents.
- Maintain audit_log and status_history consistency.

## Trigger Types
- State-based: ReadyToRequest, PendingChaserDue, ProjectReadyToClose, FeeApprovalPending
- Time-based: ScheduledChaser, WeeklyStatusReport, DeadlineRisk, SyncRetry
- Failure-based: SyncFailure, EmailFailure, RightsLinkFailure

## Flows Covered
- Flow 01: Intake and Sync (coordination)
- Flow 05: Follow-Up and Escalation (scheduling)
- Flow 08: Evidence and Reporting (weekly report scheduling)
- Flow 09: Project Closure (readiness checks)
- Flow 10: Audit and Observability
- Flow 11: Sync Retry and Failure Recovery (retry scheduling)

## Tables Read
- projects, rights_items, scheduled_tasks
- workflow_executions, workflow_steps
- status_history, audit_log
- rpc_sync, elsa_sync

## Tables Written
- workflow_executions, workflow_steps
- scheduled_tasks
- status_history, audit_log

## Integrations
- None directly; delegates to other agents.

## Idempotency Rules
- Do not schedule a new task if an active scheduled_tasks entry already exists for the same entity and purpose.
- Do not start a duplicate workflow_executions run if a running execution exists for the same project or rights_item.

## Failure Handling
- If any integration error is detected, ensure api_logs entries exist and schedule retry tasks.

## Human Decision Points
- None. Escalation decisions are routed by other agents.
