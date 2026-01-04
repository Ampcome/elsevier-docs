# Assistents.ai Flow Build Guide for Elsevier

## Purpose
This guide maps the Elsevier autonomous permissions flows and simulator flows to Assistents.ai workflow builder mechanics. It includes required actions, triggers, node configs, and data payloads so the AI Coder can build every flow consistently.

## Platform Behavior Summary
- Workflows are graphs of `trigger` and `action` nodes with edges.
- Supported trigger types in the UI: `manual`, `webhook`, `schedule`.
- Action nodes execute system actions or plugin actions.
- Cross-flow handoff is done by an HTTP Request action that calls the next flow's execute endpoint and passes input payload.

## Required Integrations and Connectors
1. Elsevier DB Connector
   - Integration type: `database`
   - Connection string: the Elsevier workflow DB (where `projects`, `rights_items`, etc. live).
   - Used by all Database Query actions.

2. Simulator Endpoints (HTTP)
   - RPC, ELSA, EMSS, Email, RightsLink, Portal simulators are called using HTTP Request actions.
   - These can be internal simulator flows or external mock endpoints.

3. AI Agents (optional but recommended)
   - Use `ai-agents/run-agent` for parsing logs, extracting items, and classifying rightsholders.
   - Requires `AI_GATEWAY_API_KEY` configured in the environment.

4. Email Integration (optional)
   - If you prefer real email instead of simulator, use Resend/Postmark plugin actions.

## Cross-Flow Triggering Requirement
The platform requires authentication for `/api/workflows/{id}/execute`. Workflow HTTP Request steps do not carry a user session. To allow flow-to-flow handoff, you must do one of the following:

- Option A (recommended): Create a small webhook gateway endpoint that validates a workflow API key and triggers `/api/workflows/{id}/execute` server-side.
- Option B: Temporarily run all core steps inside a single workflow until a gateway exists.

This guide assumes Option A is available. The HTTP Request nodes below call the gateway or the `/execute` endpoint directly.

## Standard Trigger Payload (used by all flows)
All flows accept the same input shape:

```json
{
  "event_type": "ProjectCreatedOrUpdated",
  "payload": {
    "rpc_project_id": "RPC-123",
    "project_title": "Book Title",
    "division": "Science & Technology",
    "tier": "Tier2",
    "isbn": "978-...",
    "permission_deadline": "2026-02-01",
    "publication_date": "2026-05-01",
    "submission_route": "RPC",
    "permission_budget": 3500,
    "max_cost_per_item": 200,
    "currency": "USD",
    "cs_name": "Auto CS",
    "cs_email": "auto-cs@example.test",
    "cds_name": "Auto CDS",
    "cds_email": "auto-cds@example.test"
  }
}
```

## Template Variables (Important)
- Use template autocomplete in the UI to insert variables.
- Format: `{{@<nodeId>:<Label>.<fieldPath>}}`
- Trigger data is at the root of trigger output.
- Use `payload` fields directly, e.g. `{{@triggerNode:Trigger.payload.rpc_project_id}}`.

## Action Config Reference
- Database Query
  - `dbQuery`: SQL string with template variables.
- HTTP Request
  - `endpoint`: URL
  - `httpMethod`: GET/POST/PUT/PATCH/DELETE
  - `httpHeaders`: JSON string
  - `httpBody`: JSON string (for POST/PUT/PATCH)
- Condition
  - `condition`: expression string (use template variables)
- Human Input
  - `humanInputFields`: configure form fields
- AI Agent
  - Action type: `ai-agents/run-agent`
  - `prompt`, `system`, `model`, `tools`

---

# CORE ELSEVIER FLOWS

## Flow 01 - Intake and Sync
**Trigger:** Webhook (manual for testing)

**Nodes and Config**
1. Trigger: `Webhook Intake`
   - Trigger type: webhook

2. Action: `Upsert Project` (Database Query)
   - SQL (use template variables from trigger payload):

```sql
insert into projects (
  rpc_project_id,
  project_title,
  division,
  tier,
  isbn,
  publication_date,
  permission_deadline,
  permission_budget,
  max_cost_per_item,
  currency,
  submission_route,
  status
)
values (
  '{{@trigger:payload.rpc_project_id}}',
  '{{@trigger:payload.project_title}}',
  '{{@trigger:payload.division}}',
  '{{@trigger:payload.tier}}',
  '{{@trigger:payload.isbn}}',
  '{{@trigger:payload.publication_date}}',
  '{{@trigger:payload.permission_deadline}}',
  {{@trigger:payload.permission_budget}},
  {{@trigger:payload.max_cost_per_item}},
  '{{@trigger:payload.currency}}',
  '{{@trigger:payload.submission_route}}',
  'new'
)
on conflict (rpc_project_id) do update set
  project_title = excluded.project_title,
  division = excluded.division,
  tier = excluded.tier,
  isbn = excluded.isbn,
  publication_date = excluded.publication_date,
  permission_deadline = excluded.permission_deadline,
  permission_budget = excluded.permission_budget,
  max_cost_per_item = excluded.max_cost_per_item,
  currency = excluded.currency,
  submission_route = excluded.submission_route,
  updated_at = now();
```

3. Action: `Upsert Chapters` (Database Query)
   - Optional if chapter data is provided. Use one node per chapter batch or a stored procedure if available.

4. Action: `Update rpc_sync` (Database Query)

```sql
insert into rpc_sync (entity_type, entity_id, rpc_id, sync_status, last_sync_at)
select 'project', id, rpc_project_id, 'synced', now()
from projects
where rpc_project_id = '{{@trigger:payload.rpc_project_id}}'
on conflict (entity_type, entity_id) do update set
  sync_status = 'synced',
  last_sync_at = now(),
  updated_at = now();
```

5. Action: `Decide Next Trigger` (Condition)
   - Condition if log is available:

```
{{@trigger:payload.permission_log_available}} === true
```

6. Action: `Emit PermissionLogUploaded` (HTTP Request)
   - POST `/api/workflows/{Flow02Id}/execute`
   - Body:

```json
{
  "input": {
    "event_type": "PermissionLogUploaded",
    "payload": {{@trigger:payload}}
  }
}
```

7. Action: `Emit ManuscriptReceived` (HTTP Request)
   - Only if Tier 3 and log missing

```json
{
  "input": {
    "event_type": "ManuscriptReceived",
    "payload": {{@trigger:payload}}
  }
}
```

---

## Flow 02 - Inventory and Log Processing
**Trigger:** Webhook

**Nodes and Config**
1. Trigger: `Log Processing Trigger`

2. Action: `Fetch Log or Manuscript` (HTTP Request)
   - Call simulator or RPC/ELSA/EMSS endpoint.

3. Action: `Store Document` (Database Query)

```sql
insert into documents (project_id, document_type, document_category, file_name, file_url)
select id, 'permission_log', 'input', 'permission_log.xlsx', '{{@fetchLog:data.file_url}}'
from projects
where rpc_project_id = '{{@trigger:payload.rpc_project_id}}';
```

4. Action: `Parse Source` (AI Agent)
   - Prompt: “Extract all rights items from provided log/manuscript and return structured JSON.”

5. Action: `Insert Rights Items` (Database Query)
   - Insert one row per extracted item.

6. Action: `Emit ReadyToClassify` (HTTP Request)

```json
{
  "input": {
    "event_type": "ReadyToClassify",
    "payload": {{@trigger:payload}}
  }
}
```

---

## Flow 03 - Research and Classification
**Trigger:** Webhook

**Nodes and Config**
1. Trigger: `Classification Trigger`
2. Database Query: load `rights_items` with status `yet_to_apply`.
3. AI Agent: classify rightsholder + mode_of_contact.
4. Database Query: update `rights_items` with classification.
5. HTTP Request: emit `ReadyToRequest` to Flow 04.

---

## Flow 04 - Permission Request Execution
**Trigger:** Webhook

**Nodes and Config**
1. Trigger: `Request Execution Trigger`
2. Database Query: load `rights_items` with status `ready_to_request`.
3. Condition: `mode_of_contact` equals `email`.
4. HTTP Request: call Email Simulator.
5. Condition: `mode_of_contact` equals `rightslink`.
6. HTTP Request: call RightsLink Simulator.
7. Condition: `mode_of_contact` equals `portal`.
8. HTTP Request: call Portal Simulator.
9. Database Query: update item status to `requested` + set `next_chaser_due`.

---

## Flow 05 - Follow-Up and Escalation
**Trigger:** Schedule

**Nodes and Config**
1. Trigger: `Chaser Schedule` (cron)
2. Database Query: select items where `next_chaser_due <= today`.
3. HTTP Request: send chaser via Email/Portal simulators.
4. Database Query: update `next_chaser_due` and increment chaser count.

---

## Flow 06 - Response Handling
**Trigger:** Webhook

**Nodes and Config**
1. Trigger: `Inbound Response`
2. AI Agent: parse response and decision.
3. Database Query: update `rights_items.status`.
4. Condition: if fee required → emit `FeeApprovalPending` to Flow 07.
5. Condition: if all resolved → emit `ProjectReadyToClose` to Flow 09.

---

## Flow 07 - Fees and Approvals
**Trigger:** Webhook

**Nodes and Config**
1. Trigger: `Fee Approval Trigger`
2. Database Query: compare `fee_amount` vs `projects.max_cost_per_item`.
3. Condition: within limit.
4. Database Query: mark fee approved.
5. Human Input: if over limit.
6. Database Query: record decision.

---

## Flow 08 - Evidence and Reporting
**Trigger:** Webhook + Schedule

**Nodes and Config**
1. Trigger: `Reporting Trigger`
2. Database Query: gather project summary.
3. AI Agent: generate report text.
4. HTTP Request: store docs to file storage.
5. HTTP Request: upload to RPC.
6. Database Query: update `documents`.

---

## Flow 09 - Project Closure
**Trigger:** Webhook

**Nodes and Config**
1. Trigger: `Closure Trigger`
2. Database Query: verify all rights_items resolved.
3. Condition: if true.
4. HTTP Request: update RPC project status.
5. Database Query: update `projects.status = completed`.

---

## Flow 10 - Audit and Observability
**Trigger:** Schedule

**Nodes and Config**
1. Trigger: `Audit Schedule`
2. Database Query: find stale items and overdue projects.
3. HTTP Request: send metrics or notifications.

---

## Flow 11 - Sync Retry and Failure Recovery
**Trigger:** Schedule + Webhook

**Nodes and Config**
1. Trigger: `Retry Trigger`
2. Database Query: find failed `rpc_sync` / `elsa_sync` rows.
3. HTTP Request: retry RPC/ELSA sync simulator.
4. Database Query: update sync state.
5. HTTP Request: emit `ProjectCreatedOrUpdated` to Flow 01.

---

# SIMULATOR FLOWS

## Simulator - RPC Intake by Book Name
**Trigger:** Manual

**Nodes and Config**
1. Trigger: Manual
2. Human Input:
   - Field: `book_name` (text)
3. Database Query: find project

```sql
select * from sim_projects
where project_title ilike '%' || '{{@trigger:book_name}}' || '%'
limit 2;
```

4. Condition: if 1 result.
5. HTTP Request: call Flow 01 `/execute` with payload.
6. Database Query: insert into `sim_events`.

---

## Simulator - RPC Permission Log Upload
**Trigger:** Manual

**Nodes and Config**
1. Trigger: Manual
2. Human Input: `book_name`
3. Database Query: fetch project + log
4. HTTP Request: emit `PermissionLogUploaded` to Flow 02

---

## Simulator - ELSA Export
**Trigger:** Manual or Webhook

**Nodes and Config**
1. Trigger
2. Database Query: get `sim_documents` log
3. HTTP Request: emit `PermissionLogUploaded` to Flow 02

---

## Simulator - EMSS Manuscript Delivery
**Trigger:** Manual or Webhook

**Nodes and Config**
1. Trigger
2. Database Query: get manuscript doc
3. HTTP Request: emit `ManuscriptReceived` to Flow 02

---

## Simulator - Email Service
**Trigger:** Webhook

**Nodes and Config**
1. Trigger (webhook)
2. Database Query: insert outbound into `sim_emails`.
3. Condition: determine response scenario.
4. HTTP Request: emit `InboundEmailReceived` to Flow 06.

---

## Simulator - RightsLink
**Trigger:** Webhook

**Nodes and Config**
1. Trigger
2. Database Query: insert `sim_rightslink_sessions`.
3. HTTP Request: emit `RightsLinkEvent` to Flow 06.

---

## Simulator - Publisher Portal
**Trigger:** Webhook

**Nodes and Config**
1. Trigger
2. Database Query: store portal submission.
3. HTTP Request: emit `InboundEmailReceived` or `EditorialDecision`.

---

## Simulator - Scheduler and Time
**Trigger:** Schedule

**Nodes and Config**
1. Trigger (schedule)
2. Database Query: read `sim_clock` and `sim_events` for due events.
3. HTTP Request: emit `ScheduledChaser`, `WeeklyStatusReport`, `DeadlineRisk`.
4. Database Query: mark events emitted.

---

## Notes for AI Coder
- Use template autocomplete in each node config to avoid wrong node IDs.
- For HTTP Request nodes calling flows, wrap input in `{ "input": { ... } }`.
- If the flow gateway is not available yet, keep the emit steps disabled and manually start the next flow.
- Keep all flow names stable and consistent with this guide.
