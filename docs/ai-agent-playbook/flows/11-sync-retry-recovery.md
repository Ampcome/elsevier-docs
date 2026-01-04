# Flow 11 - Sync Retry and Failure Recovery

## Purpose
Recover from RPC or ELSA sync failures without human intervention.

## Trigger Types
- Failure-based: SyncFailure
- Time-based: SyncRetry

## Agents
- Intake and Sync Agent
- Coordinator Agent

## Integrations
- rpc-sync
- elsa-export

## Inputs and Preconditions
- rpc_sync or elsa_sync has sync_status = failed
- scheduled_tasks entry exists for retry

## Steps
1) Mark sync failure and capture error details.
2) Schedule retry using scheduled_tasks.
3) Retry sync and update outcome.
4) Escalate persistent failures to human review.

## Table Updates
- rpc_sync or elsa_sync: sync_status, error_message, retry_count, next_retry_at
- scheduled_tasks: task_type = sync, next_run_at, status
- api_logs: request and response metadata
- workflow_steps: error_message and retry attempts

## Outputs
- Sync failures are retried and resolved or escalated.

## Decision Rules
- Escalate after retry_count exceeds allowed threshold.

## Human Decision Points
- Manual intervention for persistent sync failures.
