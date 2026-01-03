# Elsevier Permissions Workflow - Database Schema

This document defines all database tables required for the automation solution, organized by domain.

---

## Table of Contents

1. [Core Domain Tables](#1-core-domain-tables)
2. [Rights & Permissions Tables](#2-rights--permissions-tables)
3. [Publisher & Rightsholder Tables](#3-publisher--rightsholder-tables)
4. [Communication Tables](#4-communication-tables)
5. [Financial Tables](#5-financial-tables)
6. [Integration Tables](#6-integration-tables)
7. [Workflow & Automation Tables](#7-workflow--automation-tables)
8. [Audit & Logging Tables](#8-audit--logging-tables)
9. [Reference/Lookup Tables](#9-referencelookup-tables)
10. [Entity Relationship Diagram](#10-entity-relationship-diagram)

---

## 1. CORE DOMAIN TABLES

### 1.1 `projects`
Central table for all permission projects.

```sql
CREATE TABLE projects (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  -- External References
  rpc_project_id VARCHAR(50) UNIQUE,          -- RPC system ID
  elsa_project_id VARCHAR(50),                -- ELSA system ID (S&T)
  ems_project_id VARCHAR(50),                 -- EMS system ID (HS)

  -- Project Details
  project_title VARCHAR(500) NOT NULL,
  isbn VARCHAR(20),
  imprint VARCHAR(100),
  division VARCHAR(50) NOT NULL,              -- 'Health Sciences' | 'Science & Technology'
  tier VARCHAR(20) NOT NULL,                  -- 'Tier0' | 'Tier1' | 'Tier2' | 'Tier3' | 'Tier4' | 'RuleOf10'

  -- Publication Details
  language VARCHAR(50) DEFAULT 'English',
  print_run INTEGER,
  page_count INTEGER,
  formats JSONB,                              -- ['Print', 'Electronic', 'Translation']

  -- Budget
  permission_budget DECIMAL(12, 2),
  max_cost_per_item DECIMAL(10, 2),
  currency VARCHAR(3) DEFAULT 'USD',
  current_spend DECIMAL(12, 2) DEFAULT 0,

  -- People (FK to users table)
  cds_user_id UUID REFERENCES users(id),
  cs_user_id UUID REFERENCES users(id),
  book_author VARCHAR(255),

  -- Dates
  publication_date DATE,
  permission_deadline DATE,
  analysis_deadline DATE,

  -- Document Handling
  submission_route VARCHAR(50),               -- 'EMS Shared Drive' | 'Email' | 'EMSS'
  initial_log_attached BOOLEAN DEFAULT FALSE,

  -- Status
  status VARCHAR(50) DEFAULT 'new',           -- 'new' | 'in_progress' | 'pending_items' | 'completed' | 'on_hold'
  completion_date TIMESTAMP,

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  created_by UUID REFERENCES users(id),

  CONSTRAINT valid_division CHECK (division IN ('Health Sciences', 'Science & Technology')),
  CONSTRAINT valid_tier CHECK (tier IN ('Tier0', 'Tier1', 'Tier2', 'Tier3', 'Tier4', 'RuleOf10'))
);

CREATE INDEX idx_projects_status ON projects(status);
CREATE INDEX idx_projects_division ON projects(division);
CREATE INDEX idx_projects_tier ON projects(tier);
CREATE INDEX idx_projects_deadline ON projects(permission_deadline);
```

### 1.2 `users`
All users in the system (CS, CDS, managers, authors).

```sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  -- Identity
  email VARCHAR(255) UNIQUE NOT NULL,
  full_name VARCHAR(255) NOT NULL,

  -- Role
  role VARCHAR(50) NOT NULL,                  -- 'cs' | 'cds' | 'team_manager' | 'author' | 'admin'
  department VARCHAR(100),

  -- External References
  employee_id VARCHAR(50),

  -- Contact
  phone VARCHAR(50),
  alternate_email VARCHAR(255),

  -- Status
  is_active BOOLEAN DEFAULT TRUE,

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),

  CONSTRAINT valid_role CHECK (role IN ('cs', 'cds', 'team_manager', 'author', 'admin'))
);

CREATE INDEX idx_users_role ON users(role);
CREATE INDEX idx_users_email ON users(email);
```

### 1.3 `chapters`
Book chapters (especially for S&T Tier 1 workflow).

```sql
CREATE TABLE chapters (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,

  -- Chapter Details
  chapter_number INTEGER,
  chapter_title VARCHAR(500),

  -- Author Info
  author_name VARCHAR(255),
  author_email VARCHAR(255),

  -- Dates
  ms_due_date DATE,
  ms_received_date DATE,

  -- Status
  status VARCHAR(50) DEFAULT 'pending',       -- 'pending' | 'received' | 'validated' | 'complete'
  permissions_status VARCHAR(50),             -- 'not_started' | 'in_progress' | 'complete'

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_chapters_project ON chapters(project_id);
CREATE INDEX idx_chapters_status ON chapters(status);
```

---

## 2. RIGHTS & PERMISSIONS TABLES

### 2.1 `rights_items`
Individual items requiring permission (figures, tables, images).

```sql
CREATE TABLE rights_items (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
  chapter_id UUID REFERENCES chapters(id),

  -- Item Identification
  item_id VARCHAR(50),                        -- e.g., "Fig 3.1"
  previous_edition_item_id VARCHAR(50),
  image_finder_item_id VARCHAR(50),

  -- Source Information
  caption TEXT,
  source_info TEXT NOT NULL,
  original_figure_number VARCHAR(50),

  -- Rightsholder (FK)
  rightsholder_id UUID REFERENCES rightsholders(id),
  rightsholder_web_link VARCHAR(500),

  -- Classification
  author_is_source_author BOOLEAN DEFAULT FALSE,
  created_type VARCHAR(50) NOT NULL,          -- See reference table
  permission_required BOOLEAN,
  notification_required BOOLEAN DEFAULT FALSE,

  -- Contact Method
  mode_of_contact VARCHAR(50),                -- 'RightsLink' | 'CCC' | 'Email' | 'WebForm' | 'None'

  -- Status
  status VARCHAR(50) DEFAULT 'yet_to_apply',  -- See reference table
  apply_date DATE,
  resolve_date DATE,

  -- Chaser Tracking
  chaser1_date DATE,
  chaser2_date DATE,
  chaser3_date DATE,
  next_chaser_due DATE,
  chaser_count INTEGER DEFAULT 0,

  -- Credit & Restrictions
  credit_line_original TEXT,
  credit_line_change TEXT,
  restrictions TEXT,

  -- Financial (FK)
  fee_record_id UUID REFERENCES fee_records(id),

  -- Notes
  comments TEXT,
  internal_notes TEXT,

  -- DOI/Article Info
  doi VARCHAR(100),
  article_title VARCHAR(500),
  article_url VARCHAR(500),
  journal_name VARCHAR(255),
  volume_issue_pages VARCHAR(100),
  publication_year INTEGER,

  -- Confidence & Review
  identification_confidence VARCHAR(20),      -- 'high' | 'medium' | 'low'
  needs_manual_review BOOLEAN DEFAULT FALSE,
  reviewed_by UUID REFERENCES users(id),
  reviewed_at TIMESTAMP,

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),

  CONSTRAINT valid_status CHECK (status IN (
    'resolved', 'pending', 'yet_to_apply', 'editorial_query',
    'author_query', 'deleted', 'waiver'
  )),
  CONSTRAINT valid_mode_of_contact CHECK (mode_of_contact IN (
    'RightsLink', 'CCC', 'Email', 'WebForm', 'None'
  ))
);

CREATE INDEX idx_rights_items_project ON rights_items(project_id);
CREATE INDEX idx_rights_items_status ON rights_items(status);
CREATE INDEX idx_rights_items_rightsholder ON rights_items(rightsholder_id);
CREATE INDEX idx_rights_items_doi ON rights_items(doi);
CREATE INDEX idx_rights_items_next_chaser ON rights_items(next_chaser_due) WHERE status = 'pending';
```

### 2.2 `permission_requests`
Tracks each permission request submission.

```sql
CREATE TABLE permission_requests (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  rights_item_id UUID NOT NULL REFERENCES rights_items(id) ON DELETE CASCADE,

  -- Request Details
  request_type VARCHAR(50) NOT NULL,          -- 'permission' | 'notification' | 'stm_notification'
  mode_of_contact VARCHAR(50) NOT NULL,

  -- RightsLink Specific
  rightslink_confirmation VARCHAR(100),
  rightslink_order_id VARCHAR(100),

  -- Email Specific
  email_message_id VARCHAR(255),
  email_recipient VARCHAR(255),

  -- Web Form Specific
  form_submission_id VARCHAR(100),
  form_url VARCHAR(500),

  -- Request Content
  request_content TEXT,                       -- Email body or form data

  -- Response
  response_received BOOLEAN DEFAULT FALSE,
  response_date TIMESTAMP,
  response_content TEXT,
  response_type VARCHAR(50),                  -- 'approved' | 'denied' | 'fee_quoted' | 'more_info_needed'

  -- Status
  status VARCHAR(50) DEFAULT 'sent',          -- 'draft' | 'sent' | 'delivered' | 'responded' | 'failed'

  -- Metadata
  submitted_at TIMESTAMP DEFAULT NOW(),
  submitted_by UUID REFERENCES users(id),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_permission_requests_item ON permission_requests(rights_item_id);
CREATE INDEX idx_permission_requests_status ON permission_requests(status);
```

### 2.3 `license_checks`
Tracks license verification for each item.

```sql
CREATE TABLE license_checks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  rights_item_id UUID NOT NULL REFERENCES rights_items(id) ON DELETE CASCADE,

  -- License Details
  license_type VARCHAR(50),                   -- 'CC-BY-4.0' | 'CC-BY-NC-4.0' | etc.
  license_url VARCHAR(500),
  license_verified BOOLEAN DEFAULT FALSE,

  -- Compatibility Check
  commercial_use_allowed BOOLEAN,
  modifications_allowed BOOLEAN,
  permission_needed BOOLEAN,

  -- Verification
  verified_at TIMESTAMP,
  verified_by UUID REFERENCES users(id),
  verification_source VARCHAR(100),           -- 'publisher_page' | 'article_page' | 'crossref'

  -- Notes
  notes TEXT,

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_license_checks_item ON license_checks(rights_item_id);
```

---

## 3. PUBLISHER & RIGHTSHOLDER TABLES

### 3.1 `publishers`
Master list of publishers.

```sql
CREATE TABLE publishers (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  -- Identity
  name VARCHAR(255) NOT NULL,
  normalized_name VARCHAR(255),               -- For matching
  aliases JSONB,                              -- Alternative names

  -- STM Status
  stm_member BOOLEAN DEFAULT FALSE,
  stm_status VARCHAR(50),                     -- 'opt_in' | 'opt_out' | 'non_member'
  stm_status_verified_at TIMESTAMP,

  -- Contact Information
  permissions_email VARCHAR(255),
  permissions_url VARCHAR(500),
  general_email VARCHAR(255),
  phone VARCHAR(50),

  -- RightsLink
  rightslink_enabled BOOLEAN DEFAULT FALSE,
  rightslink_publisher_id VARCHAR(100),

  -- CCC
  ccc_enabled BOOLEAN DEFAULT FALSE,
  ccc_publisher_id VARCHAR(100),

  -- Response Metrics
  avg_response_days INTEGER,
  typical_fee_range VARCHAR(100),

  -- Notes
  special_instructions TEXT,
  notes TEXT,

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),

  CONSTRAINT valid_stm_status CHECK (stm_status IN ('opt_in', 'opt_out', 'non_member'))
);

CREATE INDEX idx_publishers_name ON publishers(normalized_name);
CREATE INDEX idx_publishers_stm ON publishers(stm_status);
```

### 3.2 `publisher_name_mappings`
Maps CrossRef/external names to internal publisher IDs.

```sql
CREATE TABLE publisher_name_mappings (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  publisher_id UUID NOT NULL REFERENCES publishers(id) ON DELETE CASCADE,

  -- External Name
  external_name VARCHAR(500) NOT NULL,
  source VARCHAR(50) NOT NULL,                -- 'crossref' | 'pubmed' | 'manual'

  -- Matching
  is_primary BOOLEAN DEFAULT FALSE,
  confidence_score DECIMAL(3, 2),             -- 0.00 - 1.00

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW(),
  verified_by UUID REFERENCES users(id),

  UNIQUE(external_name, source)
);

CREATE INDEX idx_publisher_mappings_name ON publisher_name_mappings(external_name);
```

### 3.3 `rightsholders`
Individual or organizational rightsholders (may or may not be publishers).

```sql
CREATE TABLE rightsholders (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  -- Type
  type VARCHAR(50) NOT NULL,                  -- 'publisher' | 'society' | 'individual' | 'institution' | 'government'

  -- Reference to Publisher (if applicable)
  publisher_id UUID REFERENCES publishers(id),

  -- Identity
  name VARCHAR(255) NOT NULL,

  -- Contact
  contact_email VARCHAR(255),
  contact_url VARCHAR(500),
  alternate_email VARCHAR(255),
  phone VARCHAR(50),

  -- Notes
  notes TEXT,

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),

  CONSTRAINT valid_type CHECK (type IN ('publisher', 'society', 'individual', 'institution', 'government'))
);

CREATE INDEX idx_rightsholders_name ON rightsholders(name);
CREATE INDEX idx_rightsholders_type ON rightsholders(type);
CREATE INDEX idx_rightsholders_publisher ON rightsholders(publisher_id);
```

---

## 4. COMMUNICATION TABLES

### 4.1 `emails`
All emails sent/received by the system.

```sql
CREATE TABLE emails (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  -- References
  project_id UUID REFERENCES projects(id),
  rights_item_id UUID REFERENCES rights_items(id),
  permission_request_id UUID REFERENCES permission_requests(id),

  -- Email Details
  direction VARCHAR(10) NOT NULL,             -- 'outbound' | 'inbound'
  template_id UUID REFERENCES email_templates(id),

  -- Addresses
  from_address VARCHAR(255) NOT NULL,
  to_address VARCHAR(255) NOT NULL,
  cc_addresses JSONB,
  bcc_addresses JSONB,
  reply_to VARCHAR(255),

  -- Content
  subject VARCHAR(500) NOT NULL,
  body_text TEXT,
  body_html TEXT,
  attachments JSONB,                          -- [{filename, size, content_type, storage_key}]

  -- External IDs
  message_id VARCHAR(255),                    -- Email Message-ID header
  thread_id VARCHAR(255),
  external_id VARCHAR(255),                   -- Resend/SendGrid ID

  -- Status
  status VARCHAR(50) DEFAULT 'pending',       -- 'pending' | 'sent' | 'delivered' | 'bounced' | 'failed'
  sent_at TIMESTAMP,
  delivered_at TIMESTAMP,
  opened_at TIMESTAMP,

  -- Error Handling
  error_message TEXT,
  retry_count INTEGER DEFAULT 0,

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW(),
  created_by UUID REFERENCES users(id)
);

CREATE INDEX idx_emails_project ON emails(project_id);
CREATE INDEX idx_emails_rights_item ON emails(rights_item_id);
CREATE INDEX idx_emails_status ON emails(status);
CREATE INDEX idx_emails_thread ON emails(thread_id);
```

### 4.2 `email_templates`
Email templates for various communications.

```sql
CREATE TABLE email_templates (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  -- Template Identity
  code VARCHAR(100) UNIQUE NOT NULL,          -- 'CDS_INTRO' | 'PERMISSION_REQUEST' | etc.
  name VARCHAR(255) NOT NULL,
  description TEXT,
  category VARCHAR(50),                       -- 'introduction' | 'request' | 'chaser' | 'notification'

  -- Content
  subject_template VARCHAR(500) NOT NULL,
  body_template TEXT NOT NULL,
  body_html_template TEXT,

  -- Variables
  available_variables JSONB,                  -- [{name, description, required}]

  -- Usage
  division VARCHAR(50),                       -- NULL = all | 'Health Sciences' | 'Science & Technology'
  tier VARCHAR(20),                           -- NULL = all | specific tier

  -- Status
  is_active BOOLEAN DEFAULT TRUE,

  -- Versioning
  version INTEGER DEFAULT 1,

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  created_by UUID REFERENCES users(id)
);

CREATE INDEX idx_email_templates_code ON email_templates(code);
CREATE INDEX idx_email_templates_category ON email_templates(category);
```

### 4.3 `chasers`
Scheduled follow-up chasers.

```sql
CREATE TABLE chasers (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  rights_item_id UUID NOT NULL REFERENCES rights_items(id) ON DELETE CASCADE,

  -- Chaser Details
  chaser_number INTEGER NOT NULL,             -- 1, 2, 3
  scheduled_date DATE NOT NULL,

  -- Status
  status VARCHAR(50) DEFAULT 'scheduled',     -- 'scheduled' | 'sent' | 'cancelled' | 'skipped'
  sent_at TIMESTAMP,

  -- Email Reference
  email_id UUID REFERENCES emails(id),

  -- Result
  response_received BOOLEAN DEFAULT FALSE,
  response_date TIMESTAMP,

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_chasers_item ON chasers(rights_item_id);
CREATE INDEX idx_chasers_scheduled ON chasers(scheduled_date) WHERE status = 'scheduled';
CREATE INDEX idx_chasers_status ON chasers(status);
```

---

## 5. FINANCIAL TABLES

### 5.1 `fee_records`
Permission fees quoted and processed.

```sql
CREATE TABLE fee_records (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  rights_item_id UUID NOT NULL REFERENCES rights_items(id) ON DELETE CASCADE,

  -- Fee Details
  fee_amount DECIMAL(10, 2) NOT NULL,
  fee_currency VARCHAR(3) NOT NULL,
  fee_amount_usd DECIMAL(10, 2),              -- Normalized to USD

  -- Quote Details
  quoted_at TIMESTAMP DEFAULT NOW(),
  quote_reference VARCHAR(100),
  quote_valid_until DATE,

  -- Budget Check
  within_item_limit BOOLEAN,
  within_project_budget BOOLEAN,
  budget_at_time DECIMAL(12, 2),
  spend_at_time DECIMAL(12, 2),

  -- Approval
  approval_status VARCHAR(50) DEFAULT 'pending', -- 'pending' | 'approved' | 'rejected' | 'editorial_query'
  approval_requested_at TIMESTAMP,
  approved_at TIMESTAMP,
  approved_by UUID REFERENCES users(id),
  rejection_reason TEXT,

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_fee_records_item ON fee_records(rights_item_id);
CREATE INDEX idx_fee_records_approval ON fee_records(approval_status);
```

### 5.2 `invoices`
Invoices for approved fees.

```sql
CREATE TABLE invoices (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  fee_record_id UUID NOT NULL REFERENCES fee_records(id),
  project_id UUID NOT NULL REFERENCES projects(id),

  -- Invoice Details
  invoice_number VARCHAR(100),
  invoice_date DATE,
  due_date DATE,

  -- Amount
  amount DECIMAL(10, 2) NOT NULL,
  currency VARCHAR(3) NOT NULL,

  -- Vendor
  vendor_name VARCHAR(255),
  vendor_id VARCHAR(100),

  -- Processing
  processing_mode VARCHAR(50),                -- 'standard' | 'urgent'
  submitted_to_payments_at TIMESTAMP,

  -- Status
  status VARCHAR(50) DEFAULT 'pending',       -- 'pending' | 'submitted' | 'approved' | 'paid' | 'rejected'
  paid_at TIMESTAMP,
  payment_reference VARCHAR(100),

  -- Documents
  invoice_document_url VARCHAR(500),

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  created_by UUID REFERENCES users(id)
);

CREATE INDEX idx_invoices_project ON invoices(project_id);
CREATE INDEX idx_invoices_status ON invoices(status);
CREATE INDEX idx_invoices_fee_record ON invoices(fee_record_id);
```

### 5.3 `budget_transactions`
Track all budget changes.

```sql
CREATE TABLE budget_transactions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id UUID NOT NULL REFERENCES projects(id),

  -- Transaction Details
  transaction_type VARCHAR(50) NOT NULL,      -- 'fee_approved' | 'fee_rejected' | 'adjustment' | 'refund'
  amount DECIMAL(10, 2) NOT NULL,
  currency VARCHAR(3) NOT NULL,

  -- References
  fee_record_id UUID REFERENCES fee_records(id),
  invoice_id UUID REFERENCES invoices(id),

  -- Balance
  balance_before DECIMAL(12, 2),
  balance_after DECIMAL(12, 2),

  -- Notes
  description TEXT,

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW(),
  created_by UUID REFERENCES users(id)
);

CREATE INDEX idx_budget_transactions_project ON budget_transactions(project_id);
```

---

## 6. INTEGRATION TABLES

### 6.1 `rpc_sync`
Sync status with RPC system.

```sql
CREATE TABLE rpc_sync (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  -- Entity Reference
  entity_type VARCHAR(50) NOT NULL,           -- 'project' | 'rights_item'
  entity_id UUID NOT NULL,
  rpc_id VARCHAR(100),

  -- Sync Status
  last_sync_at TIMESTAMP,
  last_sync_direction VARCHAR(10),            -- 'push' | 'pull'
  sync_status VARCHAR(50),                    -- 'synced' | 'pending' | 'failed' | 'conflict'

  -- Data
  local_hash VARCHAR(64),                     -- Hash of local data
  remote_hash VARCHAR(64),                    -- Hash of RPC data
  pending_changes JSONB,

  -- Error Handling
  error_message TEXT,
  retry_count INTEGER DEFAULT 0,
  next_retry_at TIMESTAMP,

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),

  UNIQUE(entity_type, entity_id)
);

CREATE INDEX idx_rpc_sync_entity ON rpc_sync(entity_type, entity_id);
CREATE INDEX idx_rpc_sync_status ON rpc_sync(sync_status);
```

### 6.2 `elsa_sync`
Sync status with ELSA system (S&T).

```sql
CREATE TABLE elsa_sync (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  -- Entity Reference
  entity_type VARCHAR(50) NOT NULL,           -- 'project' | 'chapter' | 'permission_report'
  entity_id UUID NOT NULL,
  elsa_id VARCHAR(100),

  -- Sync Status
  last_sync_at TIMESTAMP,
  sync_status VARCHAR(50),

  -- Data
  elsa_data JSONB,                            -- Cached ELSA data

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),

  UNIQUE(entity_type, entity_id)
);

CREATE INDEX idx_elsa_sync_entity ON elsa_sync(entity_type, entity_id);
```

### 6.3 `crossref_cache`
Cache CrossRef API responses.

```sql
CREATE TABLE crossref_cache (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  -- DOI
  doi VARCHAR(100) UNIQUE NOT NULL,

  -- Cached Data
  response_data JSONB NOT NULL,

  -- Extracted Fields (for quick access)
  publisher_name VARCHAR(255),
  title VARCHAR(500),
  journal_name VARCHAR(255),
  publication_year INTEGER,

  -- Cache Control
  fetched_at TIMESTAMP DEFAULT NOW(),
  expires_at TIMESTAMP,

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_crossref_cache_doi ON crossref_cache(doi);
CREATE INDEX idx_crossref_cache_publisher ON crossref_cache(publisher_name);
```

### 6.4 `rightslink_sessions`
Track RightsLink automation sessions.

```sql
CREATE TABLE rightslink_sessions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  rights_item_id UUID NOT NULL REFERENCES rights_items(id),
  permission_request_id UUID REFERENCES permission_requests(id),

  -- Session Details
  session_started_at TIMESTAMP DEFAULT NOW(),
  session_ended_at TIMESTAMP,

  -- RightsLink Data
  article_url VARCHAR(500),
  order_id VARCHAR(100),
  confirmation_number VARCHAR(100),

  -- Fee
  fee_quoted BOOLEAN DEFAULT FALSE,
  fee_amount DECIMAL(10, 2),
  fee_currency VARCHAR(3),

  -- Status
  status VARCHAR(50),                         -- 'started' | 'completed' | 'failed' | 'abandoned'

  -- Automation Details
  steps_completed JSONB,                      -- [{step, completed_at, data}]
  screenshots JSONB,                          -- [{step, url}]

  -- Error Handling
  error_message TEXT,

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_rightslink_sessions_item ON rightslink_sessions(rights_item_id);
CREATE INDEX idx_rightslink_sessions_status ON rightslink_sessions(status);
```

---

## 7. WORKFLOW & AUTOMATION TABLES

### 7.1 `workflow_executions`
Track workflow runs.

```sql
CREATE TABLE workflow_executions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  -- Workflow Reference
  workflow_id VARCHAR(100) NOT NULL,          -- 'elsevier-permissions-agent' etc.
  workflow_version VARCHAR(20),

  -- Context
  project_id UUID REFERENCES projects(id),
  rights_item_id UUID REFERENCES rights_items(id),

  -- Execution Details
  trigger_type VARCHAR(50),                   -- 'webhook' | 'scheduled' | 'manual'
  trigger_data JSONB,

  -- Status
  status VARCHAR(50) DEFAULT 'running',       -- 'running' | 'completed' | 'failed' | 'cancelled'
  started_at TIMESTAMP DEFAULT NOW(),
  completed_at TIMESTAMP,

  -- Result
  result JSONB,
  error_message TEXT,

  -- AI Agent Details
  agent_model VARCHAR(100),
  total_iterations INTEGER,
  total_tokens_used INTEGER,

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_workflow_executions_project ON workflow_executions(project_id);
CREATE INDEX idx_workflow_executions_status ON workflow_executions(status);
CREATE INDEX idx_workflow_executions_workflow ON workflow_executions(workflow_id);
```

### 7.2 `workflow_steps`
Individual steps within workflow executions.

```sql
CREATE TABLE workflow_steps (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  workflow_execution_id UUID NOT NULL REFERENCES workflow_executions(id) ON DELETE CASCADE,

  -- Step Details
  step_number INTEGER NOT NULL,
  step_name VARCHAR(100) NOT NULL,
  node_id VARCHAR(100),

  -- Execution
  started_at TIMESTAMP DEFAULT NOW(),
  completed_at TIMESTAMP,
  duration_ms INTEGER,

  -- Status
  status VARCHAR(50),                         -- 'running' | 'completed' | 'failed' | 'skipped'

  -- Input/Output
  input_data JSONB,
  output_data JSONB,

  -- AI Specific
  tool_calls JSONB,                           -- [{tool, input, output}]
  tokens_used INTEGER,

  -- Error
  error_message TEXT,

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_workflow_steps_execution ON workflow_steps(workflow_execution_id);
```

### 7.3 `scheduled_tasks`
Scheduled/recurring tasks.

```sql
CREATE TABLE scheduled_tasks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  -- Task Definition
  task_type VARCHAR(100) NOT NULL,            -- 'weekly_status_report' | 'chaser_check' | etc.

  -- Reference
  project_id UUID REFERENCES projects(id),
  rights_item_id UUID REFERENCES rights_items(id),

  -- Schedule
  schedule_type VARCHAR(50) NOT NULL,         -- 'once' | 'recurring'
  scheduled_at TIMESTAMP,
  cron_expression VARCHAR(100),               -- For recurring

  -- Execution
  last_run_at TIMESTAMP,
  next_run_at TIMESTAMP,
  run_count INTEGER DEFAULT 0,

  -- Status
  status VARCHAR(50) DEFAULT 'active',        -- 'active' | 'paused' | 'completed' | 'cancelled'

  -- Task Data
  task_data JSONB,

  -- End Condition
  end_condition VARCHAR(100),                 -- 'project_complete' | 'date' | 'count'
  end_date DATE,
  max_runs INTEGER,

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  created_by UUID REFERENCES users(id)
);

CREATE INDEX idx_scheduled_tasks_next_run ON scheduled_tasks(next_run_at) WHERE status = 'active';
CREATE INDEX idx_scheduled_tasks_project ON scheduled_tasks(project_id);
```

---

## 8. AUDIT & LOGGING TABLES

### 8.1 `audit_log`
Comprehensive audit trail.

```sql
CREATE TABLE audit_log (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  -- Action Details
  action VARCHAR(100) NOT NULL,               -- 'create' | 'update' | 'delete' | 'status_change' | etc.
  entity_type VARCHAR(50) NOT NULL,
  entity_id UUID NOT NULL,

  -- Context
  project_id UUID REFERENCES projects(id),

  -- User
  user_id UUID REFERENCES users(id),
  user_email VARCHAR(255),

  -- Change Details
  old_values JSONB,
  new_values JSONB,
  changed_fields JSONB,                       -- List of changed field names

  -- Source
  source VARCHAR(50),                         -- 'web' | 'api' | 'workflow' | 'sync'
  workflow_execution_id UUID REFERENCES workflow_executions(id),

  -- Request Context
  ip_address INET,
  user_agent TEXT,

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_audit_log_entity ON audit_log(entity_type, entity_id);
CREATE INDEX idx_audit_log_project ON audit_log(project_id);
CREATE INDEX idx_audit_log_user ON audit_log(user_id);
CREATE INDEX idx_audit_log_created ON audit_log(created_at);

-- Partition by month for performance
-- CREATE TABLE audit_log_2024_01 PARTITION OF audit_log
--   FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');
```

### 8.2 `status_history`
Track status changes for projects and items.

```sql
CREATE TABLE status_history (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  -- Entity Reference
  entity_type VARCHAR(50) NOT NULL,           -- 'project' | 'rights_item' | 'invoice'
  entity_id UUID NOT NULL,

  -- Status Change
  old_status VARCHAR(50),
  new_status VARCHAR(50) NOT NULL,

  -- Reason
  reason TEXT,

  -- User
  changed_by UUID REFERENCES users(id),
  changed_by_system BOOLEAN DEFAULT FALSE,

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_status_history_entity ON status_history(entity_type, entity_id);
CREATE INDEX idx_status_history_created ON status_history(created_at);
```

### 8.3 `api_logs`
External API call logs.

```sql
CREATE TABLE api_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  -- API Details
  api_name VARCHAR(100) NOT NULL,             -- 'crossref' | 'rpc' | 'elsa' | 'rightslink'
  endpoint VARCHAR(500) NOT NULL,
  method VARCHAR(10) NOT NULL,

  -- Request
  request_headers JSONB,
  request_body JSONB,

  -- Response
  response_status INTEGER,
  response_headers JSONB,
  response_body JSONB,
  response_time_ms INTEGER,

  -- Context
  entity_type VARCHAR(50),
  entity_id UUID,
  workflow_execution_id UUID REFERENCES workflow_executions(id),

  -- Error
  error_message TEXT,

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_api_logs_api ON api_logs(api_name);
CREATE INDEX idx_api_logs_created ON api_logs(created_at);

-- Retention policy: Keep only 90 days
-- DELETE FROM api_logs WHERE created_at < NOW() - INTERVAL '90 days';
```

---

## 9. REFERENCE/LOOKUP TABLES

### 9.1 `created_types`
Reference table for created type classifications.

```sql
CREATE TABLE created_types (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  code VARCHAR(50) UNIQUE NOT NULL,
  name VARCHAR(100) NOT NULL,
  description TEXT,

  -- Rules
  permission_required BOOLEAN NOT NULL,
  notification_required BOOLEAN DEFAULT FALSE,
  fee_expected BOOLEAN DEFAULT FALSE,

  -- Guidance
  guidance_text TEXT,

  -- Status
  is_active BOOLEAN DEFAULT TRUE,

  -- Order
  display_order INTEGER
);

-- Seed data
INSERT INTO created_types (code, name, permission_required, notification_required, fee_expected, description) VALUES
  ('AUTHOR_CREATED', 'Author Created', FALSE, FALSE, FALSE, 'Content created by the book author'),
  ('ELSEVIER_BOOKS', 'Elsevier Books', FALSE, FALSE, FALSE, 'Content from Elsevier book publications'),
  ('ELSEVIER_JOURNALS', 'Elsevier Journals', FALSE, FALSE, FALSE, 'Content from Elsevier journal publications'),
  ('COURTESY_INDIVIDUAL', 'Courtesy (Individual)', TRUE, FALSE, TRUE, 'Content courtesy of an individual'),
  ('COURTESY_COMPANY', 'Courtesy (Company)', TRUE, FALSE, TRUE, 'Content courtesy of a company'),
  ('ADAPTED', 'Adapted', TRUE, FALSE, TRUE, 'Content adapted from original source'),
  ('MODIFIED', 'Modified', TRUE, FALSE, TRUE, 'Content modified from original'),
  ('REDRAWN', 'Redrawn', TRUE, FALSE, TRUE, 'Content redrawn from original'),
  ('THIRD_PARTY', 'Third-Party Material', TRUE, FALSE, TRUE, 'Third-party copyrighted content'),
  ('STM_OPT_OUT', 'STM Opt-Out', FALSE, FALSE, FALSE, 'STM member publisher that opted out'),
  ('STM_NOT_OPT_OUT', 'STM Not Opt-Out', FALSE, TRUE, FALSE, 'STM member requiring notification'),
  ('UNRESTRICTED', 'Unrestricted (Previous Edition)', FALSE, FALSE, FALSE, 'Previously cleared content'),
  ('PUBLIC_DOMAIN', 'Public Domain', FALSE, FALSE, FALSE, 'No copyright protection'),
  ('DATA_FROM', 'Data From', FALSE, FALSE, FALSE, 'Data citation only'),
  ('MULTIPLE_SOURCES', 'Multiple Sources', TRUE, FALSE, TRUE, 'Content from multiple sources'),
  ('RESOLVED_BY_AUTHOR', 'Resolved by Author', TRUE, FALSE, TRUE, 'Author obtained permission');
```

### 9.2 `permission_statuses`
Reference table for permission status values.

```sql
CREATE TABLE permission_statuses (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  code VARCHAR(50) UNIQUE NOT NULL,
  name VARCHAR(100) NOT NULL,
  description TEXT,

  -- Categorization
  is_terminal BOOLEAN DEFAULT FALSE,          -- Is this a final status?
  requires_action BOOLEAN DEFAULT FALSE,

  -- Display
  color VARCHAR(20),                          -- For UI
  icon VARCHAR(50),
  display_order INTEGER
);

-- Seed data
INSERT INTO permission_statuses (code, name, is_terminal, requires_action, description) VALUES
  ('resolved', 'Resolved', TRUE, FALSE, 'Permission granted or not required'),
  ('pending', 'Pending', FALSE, TRUE, 'Awaiting response from rightsholder'),
  ('yet_to_apply', 'Yet to Apply', FALSE, TRUE, 'Permission request not yet submitted'),
  ('editorial_query', 'Editorial Query', FALSE, TRUE, 'Requires editorial decision'),
  ('author_query', 'Author Query', FALSE, TRUE, 'Requires author action'),
  ('deleted', 'Deleted', TRUE, FALSE, 'Item removed from publication'),
  ('waiver', 'Waiver', TRUE, FALSE, 'Fee waiver granted');
```

### 9.3 `currencies`
Currency reference with exchange rates.

```sql
CREATE TABLE currencies (
  code VARCHAR(3) PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  symbol VARCHAR(5),

  -- Exchange Rate (to USD)
  exchange_rate_to_usd DECIMAL(10, 6),
  rate_updated_at TIMESTAMP,

  -- Status
  is_active BOOLEAN DEFAULT TRUE
);

-- Seed data
INSERT INTO currencies (code, name, symbol, exchange_rate_to_usd) VALUES
  ('USD', 'US Dollar', '$', 1.000000),
  ('EUR', 'Euro', '€', 1.100000),
  ('GBP', 'British Pound', '£', 1.270000),
  ('INR', 'Indian Rupee', '₹', 0.012000),
  ('JPY', 'Japanese Yen', '¥', 0.006700),
  ('CHF', 'Swiss Franc', 'CHF', 1.130000);
```

---

## 10. ENTITY RELATIONSHIP DIAGRAM

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              CORE DOMAIN                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐                │
│  │    users     │     │   projects   │     │   chapters   │                │
│  ├──────────────┤     ├──────────────┤     ├──────────────┤                │
│  │ id           │◄────│ cds_user_id  │────►│ project_id   │                │
│  │ email        │     │ cs_user_id   │     │ chapter_title│                │
│  │ role         │     │ tier         │     │ author_email │                │
│  └──────────────┘     │ division     │     └──────────────┘                │
│                       └──────────────┘                                      │
│                              │                                              │
│                              │ 1:N                                          │
│                              ▼                                              │
│                       ┌──────────────┐                                      │
│                       │ rights_items │                                      │
│                       ├──────────────┤                                      │
│                       │ project_id   │───┐                                  │
│                       │ status       │   │                                  │
│                       │ created_type │   │                                  │
│                       │ doi          │   │                                  │
│                       └──────────────┘   │                                  │
│                              │           │                                  │
│              ┌───────────────┼───────────┼───────────────┐                  │
│              │               │           │               │                  │
│              ▼               ▼           ▼               ▼                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │ permission_  │  │ fee_records  │  │  chasers     │  │license_checks│    │
│  │ requests     │  ├──────────────┤  ├──────────────┤  └──────────────┘    │
│  ├──────────────┤  │ fee_amount   │  │ chaser_number│                      │
│  │ request_type │  │ approval_    │  │ scheduled_   │                      │
│  │ mode_of_     │  │   status     │  │   date       │                      │
│  │   contact    │  └──────────────┘  └──────────────┘                      │
│  └──────────────┘         │                                                 │
│         │                 │                                                 │
│         │                 ▼                                                 │
│         │          ┌──────────────┐                                         │
│         │          │   invoices   │                                         │
│         │          └──────────────┘                                         │
│         │                                                                   │
│         ▼                                                                   │
│  ┌──────────────┐                                                           │
│  │    emails    │                                                           │
│  └──────────────┘                                                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                         PUBLISHER DOMAIN                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────┐     ┌──────────────────┐     ┌──────────────┐            │
│  │  publishers  │────►│publisher_name_   │     │rightsholders │            │
│  ├──────────────┤     │    mappings      │     ├──────────────┤            │
│  │ stm_status   │     └──────────────────┘     │ type         │            │
│  │ rightslink_  │                              │ publisher_id │◄───────────┤
│  │   enabled    │◄─────────────────────────────│              │            │
│  └──────────────┘                              └──────────────┘            │
│                                                       ▲                     │
│                                                       │                     │
│                                           (from rights_items.rightsholder_id)
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                         INTEGRATION DOMAIN                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │   rpc_sync   │  │  elsa_sync   │  │crossref_cache│  │ rightslink_  │    │
│  ├──────────────┤  ├──────────────┤  ├──────────────┤  │  sessions    │    │
│  │ entity_type  │  │ entity_type  │  │ doi          │  ├──────────────┤    │
│  │ entity_id    │  │ entity_id    │  │ response_data│  │ order_id     │    │
│  │ sync_status  │  │ elsa_data    │  │              │  │ fee_quoted   │    │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                         WORKFLOW DOMAIN                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐                │
│  │  workflow_   │────►│ workflow_    │     │ scheduled_   │                │
│  │  executions  │     │   steps      │     │   tasks      │                │
│  ├──────────────┤     ├──────────────┤     ├──────────────┤                │
│  │ workflow_id  │     │ step_name    │     │ task_type    │                │
│  │ status       │     │ tool_calls   │     │ next_run_at  │                │
│  └──────────────┘     └──────────────┘     └──────────────┘                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                           AUDIT DOMAIN                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐                │
│  │  audit_log   │     │status_history│     │   api_logs   │                │
│  ├──────────────┤     ├──────────────┤     ├──────────────┤                │
│  │ action       │     │ old_status   │     │ api_name     │                │
│  │ entity_type  │     │ new_status   │     │ endpoint     │                │
│  │ old_values   │     │ entity_id    │     │ response_    │                │
│  │ new_values   │     │              │     │   status     │                │
│  └──────────────┘     └──────────────┘     └──────────────┘                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Summary: Table Count by Domain

| Domain | Tables | Purpose |
|--------|--------|---------|
| Core Domain | 3 | projects, users, chapters |
| Rights & Permissions | 3 | rights_items, permission_requests, license_checks |
| Publisher & Rightsholder | 3 | publishers, publisher_name_mappings, rightsholders |
| Communication | 3 | emails, email_templates, chasers |
| Financial | 3 | fee_records, invoices, budget_transactions |
| Integration | 4 | rpc_sync, elsa_sync, crossref_cache, rightslink_sessions |
| Workflow & Automation | 3 | workflow_executions, workflow_steps, scheduled_tasks |
| Audit & Logging | 3 | audit_log, status_history, api_logs |
| Reference/Lookup | 3 | created_types, permission_statuses, currencies |
| **Total** | **28** | |

---

## Indexes Summary

Key indexes for performance:
- All foreign keys indexed
- Status fields for filtering active work
- Date fields for scheduling/deadlines
- DOI for lookup
- Email/name fields for searching

## Partitioning Recommendations

For high-volume tables:
- `audit_log` - Partition by month
- `api_logs` - Partition by month (with 90-day retention)
- `emails` - Partition by month
- `workflow_steps` - Partition by execution date
