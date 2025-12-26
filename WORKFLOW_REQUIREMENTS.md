# Elsevier Permissions Workflow - Developer Requirements

## 1. EXECUTIVE SUMMARY

Build an automated copyright permissions workflow system for Elsevier publications that handles ~70,000 permission requests across ~6,000 projects annually. The system automates rightsholder identification, permission requests, fee handling, and follow-up management.

---

## 2. SYSTEM OVERVIEW

### 2.1 Business Context
| Metric | Value |
|--------|-------|
| Annual permission requests | ~70,000 |
| Annual projects | ~6,000 |
| Items per typical project | ~400+ |
| Touch time per project | 23-25 hours |
| Divisions | Health Sciences (HS), Science & Technology (S&T) |

### 2.2 Workflow Tiers

| Tier | Division | Description | Volume |
|------|----------|-------------|--------|
| HS Tier 0 | Health Sciences | New editions with prior permissions | Low |
| HS Tier 4 | Health Sciences | Full service (team does everything) | High |
| HS Rule of 10 | Health Sciences | Quick turnaround (≤10 items) | Moderate |
| S&T Tier 1 | Science & Tech | Author-driven (authors get permissions) | ~95% of S&T |
| S&T Tier 2 | Science & Tech | Team seeks from author logs | Moderate |
| S&T Tier 3 | Science & Tech | Team builds log from scratch | Rare |

---

## 3. FUNCTIONAL REQUIREMENTS

### 3.1 Core Capabilities

#### 3.1.1 Rightsholder Identification
**Input:** Source citation, DOI, figure caption
**Output:** Rightsholder details, STM classification, contact method

**Process:**
1. Search academic databases (CrossRef, PubMed, Google Scholar)
2. Query internal Image Finder database
3. Extract copyright notice from publication
4. Classify against STM publisher list
5. Identify contact method (RightsLink, email, web form)

**STM Classification Categories:**
| Status | Action Required | Fee Expected |
|--------|-----------------|--------------|
| `STM_OPT_OUT` | None | No |
| `STM_NOT_OPT_OUT` | Notification only | No |
| `THIRD_PARTY` | Full permission request | Possible |
| `ELSEVIER_OWNED` | Internal only | No |
| `PUBLIC_DOMAIN` | Attribution only | No |

#### 3.1.2 Permission Application

**Contact Methods (in priority order):**
1. **CCC RightsLink** - Automated via browser automation
2. **Publisher Web Form** - Automated form filling
3. **STM Notification** - Template email
4. **Direct Email** - Permission request email

**RightsLink Parameters:**
- Requestor type: STM Publisher
- Reuse type: Book/Textbook
- Format: Print/Electronic/Both
- Print run quantity
- Translation (if applicable)
- Territory: Worldwide

#### 3.1.3 Fee Handling

**Budget Thresholds:**
| Condition | Action |
|-----------|--------|
| Fee ≤ Max per item AND total ≤ budget | Auto-approve, request CDS confirmation |
| Fee > Max per item OR would exceed budget | Flag as Editorial Query |
| Fee > Project budget | Recommend replacement/deletion |

**Invoice Processing:**
- Capture: fee amount, currency, invoice number
- Track: processing mode, processed date, status
- Submit: to payments team for processing

#### 3.1.4 Chaser Management

**Schedule:**
| Chaser | Timing | Action |
|--------|--------|--------|
| Chaser 1 | 14 days after request | Email follow-up |
| Chaser 2 | 28 days after request | Second email |
| Chaser 3 | 42 days after request | Final email + phone attempt |
| Escalation | 60 days | Mark unresponsive, escalate to CDS |

**Escalation Path:**
1. Try alternate email address
2. Attempt phone contact
3. Mark as "Editorial Query"
4. Recommend replacement/deletion

---

### 3.2 Created Types (Content Classification)

The system must classify each item into one of 16 categories:

| Created Type | Permission Required | Notes |
|--------------|---------------------|-------|
| `AUTHOR_CREATED` | No | Author's own work |
| `ELSEVIER_BOOKS` | No | Internal Elsevier content |
| `ELSEVIER_JOURNALS` | No | Internal Elsevier content |
| `COURTESY_INDIVIDUAL` | Verify | Check existing permission |
| `COURTESY_COMPANY` | Verify | Check corporate permission |
| `ADAPTED` | Yes | Modified from original |
| `MODIFIED` | Yes | Changes made to original |
| `REDRAWN` | Maybe | Depends on extent of changes |
| `THIRD_PARTY` | Yes | External content |
| `STM_OPT_OUT` | No | STM member, opted out |
| `STM_NOT_OPT_OUT` | Notify | STM member, notification required |
| `UNRESTRICTED` | No | Previous edition permission |
| `PUBLIC_DOMAIN` | No | No copyright protection |
| `DATA_FROM` | Credit | Citation/credit only |
| `MULTIPLE_SOURCES` | Check each | Evaluate separately |
| `RESOLVED_BY_AUTHOR` | Verify | Author provided permission |

---

### 3.3 License Compatibility Matrix

| License | Commercial Use | Modifications | Permission Needed |
|---------|---------------|---------------|-------------------|
| CC-BY-4.0 | Yes | Yes | No (attribution only) |
| CC-BY-NC-4.0 | No | Yes | If commercial |
| CC-BY-NC-ND-4.0 | No | No | If commercial or modified |
| CC-BY-SA-4.0 | Yes | Yes | No (same license required) |
| All Rights Reserved | No | No | Yes |

---

## 4. DATA MODELS

### 4.1 Permission Log Item

```typescript
interface PermissionLogItem {
  // Identification
  id: string;
  chapterTitle: string;
  elsevierAuthor: string;
  itemId: string;
  previousEditionItemId?: string;
  imageFinderItemId?: string;

  // Source Information
  caption: string;
  sourceInfo: string;
  originalFigureNumber: string;
  rightsHolderName: string;
  rightsHolderWebLink?: string;

  // Classification
  authorIsSourceAuthor: boolean;
  createdType: CreatedType;
  permissionRequired: boolean;
  modeOfContact: 'RightsLink' | 'CCC' | 'Email' | 'WebForm';

  // Status Tracking
  status: 'Resolved' | 'Pending' | 'Yet to apply' |
          'Editorial/Author query' | 'Deleted' | 'Waiver';
  applyDate?: Date;
  resolveDate?: Date;
  chaser1Date?: Date;
  chaser2Date?: Date;

  // Credit & Restrictions
  creditLineChange?: string;
  restrictions?: string;

  // Financial
  feeAmount?: number;
  feeCurrency?: string;
  invoiceNumber?: string;
  invoiceProcessingMode?: string;
  invoiceProcessedDate?: Date;
  invoiceStatus?: 'pending' | 'submitted' | 'paid' | 'rejected';

  // Notes
  comments?: string;
}
```

### 4.2 Project Details

```typescript
interface ProjectDetails {
  id: string;
  projectTitle: string;
  isbn?: string;
  imprint?: string;
  division: 'Health Sciences' | 'Science & Technology';
  tier: 'Tier0' | 'Tier1' | 'Tier2' | 'Tier3' | 'Tier4' | 'RuleOf10';

  // Publication Details
  language: string;
  printRun?: number;
  pageCount?: number;
  formats: ('Print' | 'Electronic' | 'Translation')[];

  // Budget
  permissionBudget: number;
  maxCostPerItem: number;
  currency: 'USD' | 'EUR' | 'GBP' | 'INR';

  // People
  cdsName: string;
  cdsEmail: string;
  csName: string;
  csEmail: string;
  bookAuthor: string;

  // Dates
  publicationDate: Date;
  permissionDeadline: Date;

  // Document Handling
  submissionRoute: 'EMS Shared Drive' | 'Email' | 'EMSS';
}
```

---

## 5. EXTERNAL INTEGRATIONS

### 5.1 Required Integrations

| System | Purpose | Method |
|--------|---------|--------|
| **RPC** | Central permissions tracking | REST API |
| **CrossRef** | DOI/metadata lookup | REST API (public) |
| **ELSA** | S&T editorial platform | Reports + API |
| **EMS** | HS manuscript platform | Shared drives, email |
| **Image Finder** | Elsevier image database | Internal API |
| **RightsLink/CCC** | Permission requests | Browser automation |
| **Email Service** | Notifications & requests | SMTP/API (Resend) |

### 5.2 API Specifications

#### CrossRef API
```http
GET https://api.crossref.org/works/{doi}
User-Agent: WorkflowBuilder/1.0 (mailto:permissions@elsevier.com)

Response:
{
  "message": {
    "DOI": "10.1038/nature12373",
    "title": ["Article Title"],
    "publisher": "Springer Science and Business Media LLC",
    "container-title": ["Nature"]
  }
}
```

#### ELSA Simulator API
```http
GET /api/simulators/elsa?publisherName=Springer%20Nature

Response:
{
  "publisher": {
    "id": "springer-nature",
    "name": "Springer Nature",
    "stmStatus": "opt-in"
  },
  "permissions": {
    "recommendation": "PROCEED_WITH_ATTRIBUTION",
    "permissionRequired": false
  }
}
```

---

## 6. WORKFLOW PHASES

### Phase 1: Project Intake
1. Receive project assignment from RPC
2. Review project details (formats, budget, deadlines)
3. Send introduction email to CDS
4. Request documents (manuscript, art files, log)

### Phase 2: Log Building
1. Parse initial log (Excel/CSV/Elsa format)
2. Normalize to RPC format
3. Validate completeness
4. Create rights items in system

### Phase 3: Rights Analysis (per item)
1. Search for source publication
2. Identify copyright holder
3. Classify STM status
4. Determine contact method
5. Set created type

### Phase 4: Permission Application
1. Route by contact method
2. Submit via RightsLink OR web form OR email
3. Record application date and details
4. Update status to "Pending"

### Phase 5: Fee Handling
1. Evaluate fee against budget
2. Compare to max per item threshold
3. Route: approve, flag, or escalate
4. Process invoices when approved

### Phase 6: Chaser Management
1. Schedule follow-ups (14, 28, 42 days)
2. Send chaser emails
3. Attempt alternates (phone, other email)
4. Escalate unresponsive cases

### Phase 7: Reporting
1. Upload rights items to RPC
2. Generate analysis report
3. Send weekly status reports
4. Track credit line changes

### Phase 8: Completion
1. Verify all items resolved
2. Complete project in RPC
3. Generate cost sheet
4. Send CSAT survey

---

## 7. AI AGENT CONFIGURATION

### 7.1 Agent Settings

```json
{
  "agentModel": "anthropic/claude-sonnet-4.0",
  "agentTemperature": 0.3,
  "agentMaxIterations": 25,
  "agentTimeout": 300,
  "agentRequireApproval": "dangerous"
}
```

### 7.2 Agent Tools

**Composed Tools (custom):**
- `identify-rightsholder` - DOI lookup, copyright extraction
- `check-stm-status` - STM classification
- `lookup-publisher-contact` - Contact details
- `send-permission-request` - Submit request
- `rpc-operations` - RPC CRUD operations
- `submit-rightslink` - RightsLink automation
- `manage-chasers` - Follow-up scheduling
- `process-invoice` - Invoice handling

**Plugin Tools (external):**
- `http-request` - API calls
- `resend/send-email` - Email sending
- `parallel/academic-search` - Multi-source search
- `perplexity/research` - Policy research
- `firecrawl/scrape` - Web scraping
- `browser-automation/extract` - Form automation

---

## 8. EMAIL TEMPLATES

### 8.1 Required Templates

1. **CDS Introduction** - Initial contact with project details
2. **Permission Request** - Standard request email
3. **STM Notification** - Notification for STM opt-out
4. **Fee Approval Request** - Request for budget approval
5. **Chaser 1/2/3** - Follow-up emails
6. **Editorial Query** - Over-budget notification
7. **Completion Notice** - Project wrap-up

### 8.2 Template Variables

```
{{projectTitle}}
{{projectId}}
{{bookAuthor}}
{{doi}}
{{articleTitle}}
{{publisher}}
{{figureDescription}}
{{feeAmount}}
{{feeCurrency}}
{{deadline}}
```

---

## 9. REPORTING REQUIREMENTS

### 9.1 Analysis Report (per project)
- Total items by status
- Items requiring attention
- Budget utilization
- Credit line changes needed
- Restrictions summary

### 9.2 Weekly Status Report
- Items resolved this week
- Items pending
- Outstanding chasers
- Budget status
- Risk items

### 9.3 Cost Sheet (at completion)
- All fees paid
- Invoice summary
- Budget vs actual

---

## 10. TESTING REQUIREMENTS

### 10.1 Scenario Coverage

Must test all combinations of:
- 16 created types
- 3 STM classifications (opt-in, opt-out, non-member)
- 4 contact methods
- License types (CC-BY variants, All Rights Reserved)
- Fee scenarios (within budget, over item limit, over project budget)
- Author matching (fee waiver eligibility)
- Restriction handling (territory, format, language)

### 10.2 Integration Tests
- CrossRef API (real)
- ELSA simulator
- Publishers simulator
- RightsLink automation (mock)
- Email sending (sandbox)

---

## 11. IMPLEMENTATION PHASES

### Phase 1: Core Infrastructure
- [ ] RPC API integration
- [ ] CrossRef integration
- [ ] Rights analysis composed tool
- [ ] Permission application composed tool

### Phase 2: Communication
- [ ] Email templates
- [ ] Email sending integration
- [ ] Chaser scheduling
- [ ] Fee handling workflow

### Phase 3: Reporting
- [ ] RPC operations workflow
- [ ] Log parsing (Excel/CSV)
- [ ] Analysis report generation
- [ ] Weekly status reports

### Phase 4: Platform Integration
- [ ] ELSA API integration
- [ ] EMS integration
- [ ] RightsLink browser automation
- [ ] Full workflow orchestration

---

## 12. ENVIRONMENT CONFIGURATION

```bash
# Required
AUTH_SECRET=
POSTGRES_URL=

# AI Providers
ANTHROPIC_API_KEY=

# External Services
CROSSREF_USER_AGENT=WorkflowBuilder/1.0

# Internal APIs (when available)
RPC_API_URL=
RPC_API_KEY=
ELSA_API_URL=
ELSA_API_KEY=
IMAGE_FINDER_API_URL=
IMAGE_FINDER_API_KEY=

# Email
RESEND_API_KEY=

# Optional
PERPLEXITY_API_KEY=
FIRECRAWL_API_KEY=
```

---

## 13. ACCEPTANCE CRITERIA

1. Process permission requests autonomously with >90% accuracy
2. Correctly classify STM status for all major publishers
3. Handle all 16 created types appropriately
4. Manage chaser schedule without manual intervention
5. Flag over-budget items for human review
6. Generate accurate analysis and status reports
7. Complete projects with full audit trail

---

## 14. ARCHITECTURE DIAGRAM

```
┌──────────────────────────────────────────────────────────────┐
│                    WORKFLOW BUILDER UI                        │
│  ┌─────────┐    ┌──────────────┐    ┌─────────────────────┐  │
│  │ Trigger │───▶│ AI Agent     │───▶│ Condition/Response  │  │
│  │ (Webhook)│    │ (Permissions)│    │                     │  │
│  └─────────┘    └──────────────┘    └─────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────────┐
│                    AI AGENT RUNTIME                           │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐  │
│  │                   COMPOSED TOOLS                        │  │
│  │  ┌─────────────────┐  ┌─────────────────────────────┐  │  │
│  │  │ identify-       │  │ check-stm-status            │  │  │
│  │  │ rightsholder    │  │ - Query ELSA simulator      │  │  │
│  │  │ - Call CrossRef │  │ - Return STM classification │  │  │
│  │  │ - Extract DOI   │  │ - Get recommendations       │  │  │
│  │  └─────────────────┘  └─────────────────────────────┘  │  │
│  │  ┌─────────────────┐  ┌─────────────────────────────┐  │  │
│  │  │ lookup-publisher│  │ send-permission-request     │  │  │
│  │  │ -contact        │  │ - Generate emails           │  │  │
│  │  │ - Get email     │  │ - Create RightsLink request │  │  │
│  │  │ - Get URL       │  │ - Track reference numbers   │  │  │
│  │  └─────────────────┘  └─────────────────────────────┘  │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐  │
│  │                   PLUGIN TOOLS                          │  │
│  │  http-request | perplexity | firecrawl | browser-auto  │  │
│  └────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────────┐
│                    EXTERNAL SERVICES                          │
│  ┌─────────────┐  ┌─────────────┐  ┌──────────────────────┐  │
│  │ CrossRef    │  │ ELSA        │  │ Publishers DB        │  │
│  │ (Real API)  │  │ (Simulator) │  │ (Simulator)          │  │
│  └─────────────┘  └─────────────┘  └──────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

---

## 15. APPENDIX

### 15.1 Publisher ID Mapping

| CrossRef Name | Internal ID |
|---------------|-------------|
| Springer Science and Business Media LLC | springer-nature |
| Elsevier BV | elsevier |
| John Wiley & Sons, Inc. | wiley |
| Informa UK Limited | taylor-francis |
| American Chemical Society (ACS) | american-chemical-society |
| Oxford University Press (OUP) | oxford-university-press |
| SAGE Publications | sage |
| Cambridge University Press | cambridge-university-press |

### 15.2 Action Codes

| Code | Description |
|------|-------------|
| NO_PERMISSION_REQUIRED | No action needed |
| ATTRIBUTION_ONLY | Just add credit line |
| NOTIFICATION_SENT | STM notification sent |
| NOTIFICATION_QUEUED | Notification pending |
| PERMISSION_REQUEST_SENT | Full request sent |
| RIGHTSLINK_REQUEST_CREATED | RightsLink order created |
| EMAIL_REQUEST_QUEUED | Email pending |
| FEE_APPROVAL_REQUIRED | Needs manager approval |
| EDITORIAL_QUERY | Escalated to editor |
| MANUAL_REVIEW_REQUIRED | Human review needed |
| CHASER_SCHEDULED | Follow-up scheduled |

### 15.3 Response Status Codes

| Status | Meaning |
|--------|---------|
| approved | Permission granted |
| pending | Awaiting response |
| pending_review | Under publisher review |
| pending_approval | Awaiting internal approval |
| editorial_query | Escalated |
| denied | Permission refused |
