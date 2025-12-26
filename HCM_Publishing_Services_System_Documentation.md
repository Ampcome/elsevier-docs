# HCM Publishing Services - System of Records Documentation

## 1. Organization Overview

### About Publishing Services
- **Organization Size**: 60+ FTE (Full-Time Employees)
- **Processes Handled**: 12 different processes
- **Annual Volume**:
  - 70,000 requests
  - 6,000 projects
  - 10,000 system record updates

### Mission
Centrally manage multiple business and content processes for multiple business units in different geographies across the end-to-end publishing workflow.

---

## 2. Publishing Services Processes

### Core Processes
| Process Category | Process Name |
|------------------|--------------|
| Setup | EMSS Site Set-up |
| Contributors | List of Contributors Confirmation |
| Review | Proposal Review Administration |
| Copies | Gratis Copies Management |
| Data | Data Management |
| Assessment | Technical Assessment |
| Agreements | Agreements Management |
| Payee | Payee Information Management |
| Permissions | Permissions Seeking |
| Permissions | Permissions Granting |
| Corrections | Post-Publication Corrections |
| CRM | Customer Relationship Management |

### Process Workflow Stages
1. **Content Planning and Research**
2. **Proposal and Commissioning**
   - Proposal Review
   - EMSS Site Setup
3. **Manuscript Development**
4. **Content Production**
5. **Printing, Warehousing and Publishing (P&E)**
   - Gratis Copies Management
6. **Post Publication Processes**
   - Post Pub Corrections
   - Permissions Granting

### Supporting Processes (Orange Layer)
- Agreements Management
- Permissions Seeking
- LOC Administration
- Technical Assessment
- Data Management
- Payee Information Management
- Customer Relationship Management

---

## 3. Stakeholders

### Internal Stakeholders
| Department |
|------------|
| Global Content Partners |
| Clinical Solutions |
| Legal |
| Finance |
| Nursing and Health Education |
| Technology |
| Operations Teams |

### External Stakeholders (Customers)
| Stakeholder Type |
|------------------|
| Authors |
| Contributors |
| Editors |
| Reviewers |
| Rightsholders |
| Suppliers |

---

## 4. Permissions Seeking Module

### Overview
Obtain permissions from internal and external rights holders.

### External Stakeholders
- Authors
- Contributors
- Editors
- Rightsholders

### Internal Stakeholders
- Global Content Partners
- Clinical Solutions
- Nursing and Health Education
- EMEA/APAC

### KPIs
- **Timeliness**: Completion 30 days prior to FTP
- **Volume**:
  - ST (Standard): 1480 projects/year
  - HS (Health Sciences): 770 projects/year
- **FTE Count**: 19

### Applications Used
- Rights and Permissions Collector DB (Permissions Database)
- ELSA
- EMSS

### Workflows Supported
- HS (Health Sciences)
- Clinics
- RREF
- Translations
- APAC
- Nursing
- Journals
- E-products

---

## 5. Permission Tiers & Service Types

### Division-Based Tiers

#### Divisions: HS, Translation, APAC, Journal, and E-products (IPOC, Mosby skills, Clinical Key Essentials, etc.)

| Tier | Description |
|------|-------------|
| Tier 0 | CDS/Author obtains all permissions. CS validates and uploads the logs and files into RPC |
| Tier 4 | CDS provides permission log. CS obtains permissions. CS uploads the logs and files into RPC |
| Rule of 10 | No permission seeking, CS only does the Rule of 10 assessment |

#### Divisions: RREF, Hot Topics, and MRW

| Tier | Description |
|------|-------------|
| Tier 1 | Author obtains all permissions and provides permissions log. CS validates and uploads the logs and files into RPC |
| Tier 2 | Author provides permission log. CS obtains permissions. CS uploads the logs and files into RPC |
| Tier 3 | Author submits manuscript. CS creates permission log and obtains permissions. CS uploads the logs and files into RPC |

### Role Definitions
- **CDS** - Content Development Specialist
- **CS** - Copyrights Specialist
- **RPC** - Rights and Permissions Collector

### Service Types in RPC
- Tier 4(HS - Full service)

---

## 6. Rights & Permissions Collector (RPC) System

### System URL
`https://app-services.cwsrpc.elsevier.net/rp-collector-web/`

### Login Screen Fields
| Field | Type | Required |
|-------|------|----------|
| User Name | Text Input | Yes (*) |
| Password | Password Input | Yes (*) |
| Login Button | Button | - |
| Forgot your Password? | Link | - |

### Main Navigation
- Home > Projects
- Permissions Tracker
- Create Project

### Dashboard Metrics
| Metric | Display |
|--------|---------|
| Active Projects | Count (e.g., 47, 2865) |
| Completed Projects | Count (e.g., 579, 8890) |

### Projects List View - Table Columns
| Column | Description |
|--------|-------------|
| Division | Business division |
| Title | Project title |
| Service Type | Tier classification |
| Editorial Contact | Assigned editor |
| Deadline | Due date |
| Publication Date | Expected publish date |
| Assigned To | Team member |
| Total Permissions Pending | Count |
| Total Permissions | Count |

### Search & Filter Options
- Search by: ISBN/Cost center/Name
- Search by: Division/Title/Project ID/Assignee/Editor

---

## 7. Project Details Screen

### Project Details Tab

#### Service Details Section
| Field | Sample Value |
|-------|--------------|
| Received Date | 30-Sep-2025 |
| *Division | HS |
| *Sub Division | Clinical Solutions |
| Project Reference No | DEL_Kim_4_murugans |
| *ISBN/Manifestation Id | 9780443124976 |
| *Location | New Delhi |

#### Editorial Contact Details Section
| Field | Sample Value |
|-------|--------------|
| *Name | Garima Malhotra |
| *Email | g.malhotra@elsevier.com |
| Invited Editorial Users | - |
| Freelancer Name | - |
| Freelancer Email | - |

#### Project Details Section
| Field | Sample Value |
|-------|--------------|
| *Author(s) | Raymond J. Kim |
| *Title | Cardiovascular Magnetic Resonance |
| *Edition | 4 |
| *Author(s)/Editor(s) email addresses | raymond.kim@duke.edu |
| *Projected publication date | 01-Jul-2026 |
| *Permission deadline date | 10-Jan-2026 |
| Files to printer date | 11-Mar-2026 |
| *Transmittal date | 18-Sep-2025 |
| *Ownership | Elsevier Inc. |
| *Service Type | Tier 4(HS - Full service) |
| *The platform used for this title is | EMSS |
| *Language | English |
| Free to translate | No |
| *Are any translations expected? | No |
| *High priority title? | No |
| Are previous edition permission files available? | No |

#### Other Details Section
| Field | Sample Value |
|-------|--------------|
| Brief description of the project | - |
| Will the project come in batches? | Yes |
| Batch Information | November 4, 2025 - 6/12 |
| Total Budget for all Project Permissions | - |
| Maximum Cost Limit per Permission Item | - |
| Permission invoices to be paid by/against | - |
| *Manuscript delivery date | 15-Feb-2024 |
| *Number of Chapters | 42 |
| *Book Price | $0.00 |
| *Print run | 457 |
| *Page count | 602 |
| *Distribution | Worldwide |
| *Format | Print and electronic |
| *In which form(s) will the project files be submitted to the Copyrights Team? | EMSS, Shared drive, Email |

### Right Item Assignments Tab

#### Table Columns
| Column | Description |
|--------|-------------|
| Item ID | Unique identifier |
| Creator Type | Author Created, Courtesy, etc. |
| Chapter No. | Chapter number |
| Rightsholders | Rights holder name |
| Permission Status | Resolved, Pending, Deleted |
| Restrictions | No Res, restrictions info |
| Invoice Amount | Cost if applicable |
| Resolved Time | Days to resolve |
| Send Email | Email action |

#### Item Status Badges
| Badge | Count |
|-------|-------|
| Total Items | Variable (e.g., 651) |
| Total items pending | Variable |
| Total items in query | Variable |
| Total items yet to apply | Variable |
| Total fee spent | USD amount |

### Chapter Tracker Tab

#### Table Columns
| Column | Description |
|--------|-------------|
| Chapter No. | Number |
| Chapter Title | Title text |
| Authors | Author names |
| Intro Email Due Date | Date |
| Intro Email Sent Date | Date |
| MS Due Date | Date |
| First Reminder Due Date | Date |
| Second Reminder Sent Date | Date |
| First Chaser Due Date | Date |
| First Chaser Sent Date | Date |
| Second Chaser Due Date | Date |
| Permission Received | Yes/No |
| Permission Status | Pending |
| Comments | Text |
| Intro Email Due Date | Date |

### Documents Tab
| Feature | Description |
|---------|-------------|
| Upload new Document | Button |
| Document Title | File name |
| File Name | System filename |
| Uploaded Date | Date |

#### Sample Documents
- Kim9780443124976_RPC-PermLog.xlsx
- Kim9780443124976_RPC-PermLog.xlsx

---

## 8. Permissions Tracker Screen

### URL
`https://app-services.cwsrpc.elsevier.net/rp-collector-web/permissions-tracker`

### Project Level View - Table Columns
| Column | Description |
|--------|-------------|
| Division | Business unit |
| Title | Project title |
| Project ID | Unique identifier |
| Assignee | Team member |
| Editorial Contact | Editor |
| Additional Contact | Secondary contact |
| Total RightsItems | Count |
| Resolved RightsItems | Count |
| To be worked RightsItems | Count |

### Actions Available
- Save
- Refresh
- Send WSR (Weekly Status Report)
- Send WSR With Attachment
- Send Analysis Report
- Columns (customize view)
- Export Data

---

## 9. Analysis Report Screen

### URL
`https://app-services.cwsrpc.elsevier.net/rp-collector-web/analysis-report/{id}`

### Report Header
- Send Report With Attachment (Button)
- Send Report (Button)

### Report Fields
| Field | Description | Sample Value |
|-------|-------------|--------------|
| Total no of Permission items | Count | 404 |
| Permissions to be cleared | Count | 404 |
| Elsevier permissions | Count | 0 |
| Third Party permissions Split | Publishers/Companies/Courtesy of/First time Contacts | 0/0/NA/0/0/NA |
| High Fee permission items | Count | 0 |
| High TAT copyright holders | Count | 0 |
| Restriction list | Dropdown | Choose Option (Available/Not Available/Not Applicable) |
| Chapter author information | Dropdown | Choose Option (Available/Not Available) |
| Approximate project completion date | Date | Jan 14, 2026 |

### Additional Notes Section
- Free text area for analysis notes
- Example: "For f12-01, In the provided Elsevier source book, this figure is credited to another source and upon contacting, the rightsholder American Medical Association, is charging a very high fee of $6,561.80. Hence, please check for the possibilities of replacement or deletion and kindly confirm the same."

---

## 10. Permission Log (Excel) Fields

### Sheet 1: Item Upload Format

#### Core Columns (Yellow - Mandatory)
| Column | Description |
|--------|-------------|
| Project ID / Publication Name | Project identifier |
| Permission Status (Mandatory) | Status value |
| Chapter Title | Chapter name |
| Elsevier Author Name | Author name |
| Item ID (mandatory) | Unique item ID |
| Previous Edition Item ID | Reference to previous |
| PII/ID | Publication identifier |
| Caption Title | Caption text |
| Source (mandatory) | Source information |
| Source Chapter | Source chapter |

#### Additional Columns (Green)
| Column | Description |
|--------|-------------|
| Elsevier author and source author | Author info |
| Credit Line Changes | Change tracking |
| Original Figure Number | Figure reference |
| Rightsholder | Rights holder name |
| Permission Required (mandatory) | Yes/No |
| Creator Type | Type of creator |
| Rightsholder Web Link | URL |
| Mode of Contact | Contact method |
| Rightsholder Email Address | Email |

#### Date Columns (Orange)
| Column | Description |
|--------|-------------|
| Applied Date | Application date |
| Resolved Date | Resolution date |
| Resolved Time (days) | Duration |

#### Communication Columns
| Column | Description |
|--------|-------------|
| Email Chaser 1 date | First chase |
| Email Chaser 2 date | Second chase |

#### Financial Columns (Blue)
| Column | Description |
|--------|-------------|
| Restrictions | Restriction info |
| Invoice Amount | Cost |
| Currency | Currency code |
| Invoice Number | Invoice ID |
| Invoice Processing Mode | Processing type |
| Invoice Processed Date | Date |
| Invoice Status | Status |

#### Service Columns
| Column | Description |
|--------|-------------|
| Service Icer Char | Service character |

### Sheet 2: Reference Data

#### Permission Status Values
| Status | Description |
|--------|-------------|
| Resolved | Permission obtained |
| Pending | Awaiting response |
| Yet to Apply | Not yet requested |
| Editorial/Author Query | Query raised |
| Waiver | Waived |
| Deleted | Removed |

#### Source Types
| Source Type |
|-------------|
| Author Created |
| Elsevier Books |
| Elsevier Journals |
| Courtesy Of |
| Adapted/Modified/Redrawn |
| 3rd party material |
| Unrestricted |
| Public Domain |
| STM Opt-Out |
| STM Not Opt-Out |
| Resolved by Editorial/Author |
| Multiple Sources |
| Data from |

#### Creator Types
| Type |
|------|
| Author Created |
| Courtesy |
| Used |
| 3rd Party Material |

#### Mode of Contact
| Mode |
|------|
| CCC |
| Email |
| Online Form |
| RightsLink |
| (Blanks) |

---

## 11. Copyright Clearance Center (CCC) RightsLink Integration

### System URL
`https://s100.copyright.com/`

### Quick Price Estimate Form

#### "I would like to..." Options
- reuse in a book/textbook

#### Requestor Type Options
| Option |
|--------|
| make a selection |
| Author of this Wiley article |
| Commercial/For-profit organization |
| Government agency |
| Medical communication company |
| Medical educational organization |
| Non-commercial/Not-for-profit organization |
| Non-governmental organization |
| Publisher, for-for-profit |
| Publisher, not-for-profit |
| Pharmaceutical/medical products company |
| Public research institute |
| Publisher, STM |
| Training organization |

#### Format Options
| Format |
|--------|
| make a selection |
| Print |
| Electronic |
| Print and electronic |

#### Portion Options
| Portion |
|---------|
| make a selection |
| Full article |
| Text extract |
| Figure/table |
| Abstract |

#### Translation Options
| Option |
|--------|
| make a selection |
| No |
| Yes, including English rights |
| Yes, without English rights |

#### Circulation Options
| Option |
|--------|
| make a selection |
| (various options) |

#### Currency Selection
- USD - $

### About Your Work Form Fields
| Field | Required | Type |
|-------|----------|------|
| Title of new book | Yes (*) | Text |
| Lead author | Yes (*) | Text |
| Publisher | Yes (*) | Dropdown |
| Publisher imprint | No | Text |
| Expected publication date | Yes (*) | Month/Year |
| Expected number of pages | No | Number |

#### Publisher Options (Partial List)
| Publisher |
|-----------|
| AIP Publishing |
| American Association for the Advancement of Science (AAAS) |
| American Association of Critical-Care Nurses |
| American Chemical Society |
| American Mathematical Society |
| American Physical Society |
| American Psychological Association |
| American Society for Parenteral and Enteral Nutrition (ASPEN) |
| American Society of Civil Engineers |
| American Society of Mechanical Engineers |
| Apple Academic Press |
| Association for Computing Machinery (ACM) |
| Begell House |
| BioExcel Publishing |
| Bioscientifica |
| BMJ |
| British Small Animal Veterinary Association (BSAVA) |
| Burleigh Dodds Science Publishing Ltd |
| CABI |
| Elsevier |

### Additional Information Form
| Field | Type |
|-------|------|
| Order reference number | Text |
| Portions (Figure/table description) | Text |
| The Requesting Person / Organization to Appear on the License | Text (Required *) |
| Number of figures/tables | Number |

### About Your Works - Selection Table
| Column | Description |
|--------|-------------|
| Title of new book | Book title |
| Publisher/Producer/Sponsor | Publisher name |
| Date | Publication date |

### Pricing Display
- PRICE: Pending / 0.00 USD
- SAVE QUOTE (Button)
- CONTINUE (Button)

---

## 12. STM Permissions Guidelines

### URL
`https://www.stm-assoc.org/what-we-do/core-services/ip-copyright/permissions/permissions-guidelines/`

### Key Information
- Download the 2024 version of the Permission Guidelines (PDF, HTML)
- Publisher must be a member of STM to participate
- Contact: info@stm-assoc.org
- Based on principle of reciprocity
- Must be a publisher of primary research
- Quarterly STM Permissions guidelines roundtable

### Reciprocity Requirement
A publishing house must offer more than 50% of content that is neither CC-BY nor CC-0 to meet the requirement.

### STM Publisher Benefits
- Can request permission through the rights link RCCC
- Free of charge for up to 3 figures/tables for fellow signatory publishers

---

## 13. ELSA (Elsevier Author) System

### System URL
`https://app.elsa.elsevier.com/`

### Chapter View Screen
#### URL Pattern
`https://app.elsa.elsevier.com/document/{id}/write`

#### Navigation Tabs
- Write
- Activity & Versions
- Permissions Files
- Figures
- Tables
- Permission Log
- Art Log
- LaTeX files

#### Chapter Information Display
| Field | Value |
|-------|-------|
| Chapter Number | 8. |
| Title | Quantification of the sediment budget of river systems |
| View Mode | Toggle |
| Staff Review | Progress indicator (5/6 Stages) |

#### Chapter Structure (Outline)
- 1. Introduction
- 2. Principles and concepts
  - 2.1 Sediment source-to-...
  - 2.2 Types of river systems...
  - 2.3 Sediment budget of...
- 3. Controls on river sedimentation
  - 3.1 Tectonics

#### Chapter Metadata
- Affiliation
- Contributor (Author)
- Abstract
- Word Count: 9627 Words
- Publishing Assistant (1 ALERTS)

### Project Settings Screen
| Section | Fields |
|---------|--------|
| General Information | Project name |
| Project Settings | Various settings |
| Import Previous Edition | Import options |
| Publishing Assistant | Assistant settings |

### Dates & Milestones Tab
| Column | Description |
|--------|-------------|
| Name | Chapter name |
| Location | Part number |
| Currently Editing | Editor |
| Responsible Editor | Assigned editor |
| Chapter Notes | Notes |
| 1. Not Started | Status |
| 2. Draft | Status |
| 3. Staff Review | Status |

### Reports & Jobs Tab
| Column | Description |
|--------|-------------|
| # | Row number |
| Report | Report type |
| Owner | Creator |
| Created | Date/time |
| Status | complete/pending |

#### Report Types
- Project Status Report
- Contributor Agreement Report
- Contributor Payments by Project Report

---

## 14. Email Templates

### 1. New Project Assignment Email (to Editorial Contact)

**Subject**: New Project: < [Project Title] >

**From**: rpcapplication@elsevier.com

**Template**:
```
ELSEVIER                Rights & Permissions Collector

Dear [Editorial Contact Name]:

The Copyrights Team is happy to work with you on this project. We have
assigned the project to [Assigned Team Member], who will contact you
directly with more information.

Please introduce Permissions Helpdesk team (permissionshelpdesk@else-
vier.com) to the editors/ authors of this title at the earliest to assist on the
permissions process.

With best regards,
The Copyrights Team
```

### 2. Introduction Email (to Rightsholder)

**Subject**: RE: Introduction Email: < [Book Title], ISBN: [ISBN] >

**From**: [Copyrights Specialist]@elsevier.com (e.g., s.murugan@elsevier.com)

**Template**:
```
Hi [Rightsholder Name],

Happy New Year!

I am Saravanan, who has been assigned with the title "[Book Title], [Edition], ISBN: [ISBN]". I am happy to work with you on the permissions of this project.

I have downloaded the permission log from RPC and request you to please provide the manuscripts & art files for this title.

Also, please provide the print run for this title as it is not mentioned in RPC.

I look forward to hearing from you. Many thanks in advance and have a wonderful day!

Thanks & Regards,
Saravanan Murugan
Senior Copyrights Specialist - Copyrights Team
ELSEVIER | Operations
Tel: +91 44 33784356 |
Email: s.murugan@elsevier.com | url: www.elsevier.com
Twitter | Facebook | LinkedIn |
```

### 3. Permission Request Email (to External Rightsholder)

**Subject**: Elsevier Permission Request: [PHI_Reference]_[Figure Number]

**From**: Permissions Seeking (ELS) <permissionsseeking@elsevier.com>

**Template**:
```
Dear [Rightsholder Name],

Greetings from Elsevier!

I am Saravanan working as a copyrights specialist at Elsevier. We are interested in using one of the figures copyrighted to you in our upcoming publication and we request your permission to use it in our Book. I have listed the details of the request below.

Book Title          [Book Title]/[Edition] edition
Author of the Book  [Author Name]
Format              Print & Electronic
Distribution        Worldwide
Chapter Title       [Chapter Title]
Chapter Author Name [Chapter Author Name]

We request your permission for Elsevier and its licensees, affiliates, successors and assigns to use, reproduce or, if it is necessary, to redraw or modify the material listed below in this and all subsequent editions of this Elsevier work and all revisions, versions, derivative works, translations, ancillaries, adaptations, supplementary materials, custom editions, and in advertising and promotion thereof, in all languages, in all formats and media now known or hereafter developed, throughout the world and in perpetuity. We will give full credit to the original source.

Source reference:
[Source Reference - e.g., "Courtesy 3M."]

[Figure Image]
```

### 4. Credit Line Change Email

**Subject**: Credit Line Change : [Book Title] <[ISBN]>

**From**: s.murugan@elsevier.com

**To**: [Rightsholder], [Author], [Editorial Contacts]

**Template**:
```
Dear [Rightsholder Name],

I am writing to you regarding a credit line change for the permissions project, [Book Title].

Please note the change to be made to the credit line for the below listed permission item(s).

| Item ID | Caption Title | Changes to be made to the Credit Line |
|---------|---------------|---------------------------------------|
| [Item ID] | [Caption] | [New Credit Line Source] |

Please get back to me if you require any clarification.

Regards,
Saravanan Murugan
```

### 5. Weekly Status Report (WSR) Email

**Subject**: Weekly Status Report - [Book Title]:Surgical Technology, [Edition], [ISBN]

**From**: Permissionseeking@elsevier.com

**Template**:
```
Hi [Rightsholder Name],

Good day! Please find below the status report of the project, [Book Title], [Edition].

| Field | Value |
|-------|-------|
| Total no of Permission items | [Count] |
| Permissions to be worked | [Count] |
| Permissions Processed | [Count] |
| Permissions Resolved | [Count] |
| Permissions Yet to be Resolved | [Count] |
| Permissions in DE Query | [Count] |
| Permissions Yet to Apply | [Count] |
| Publication date | [Date] |
| Last Batch received date | [Single Batch/Date] |
| Project Deadline date | [Date] |
| Invoice amount spent till date ($) | [Amount] |

DE Query details:

| Item ID | Rightsholder | Comments |
|---------|--------------|----------|
| [Item ID] | [Rightsholder] | [Comment] |

[Additional rows as needed]
```

### 6. Project Completion Email

**Subject**: Project Completion : [Book Title] <[ISBN]>

**From**: s.murugan@elsevier.com (or s.murugan@elsefier.com)

**Attachments**:
- [ISBN]_PermissionLog.xlsx
- [ISBN]_Cost Sheet.xlsx

**Template**:
```
Hi [Rightsholder Name],

Hope this email finds you well.

Please find the attached final permission log and cost sheet for this title: [Book Title] [ISBN]

Thank you for your support with this project.

You will receive an automated survey email. I request you to fill in the survey and provide us with your valuable feedback which will help us improve our service.

Do let us know if you encounter any trouble in receiving the survey email. Have a nice day!

Regards,
Saravanan Murugan
```

### 7. Analysis Report Email

**Subject**: Analysis Report - [Book Title]: [ISBN]

**From**: Permissionseeking@elsevier.com

**Template**:
```
Hi [Editorial Contact Name],

Please find below the Analysis report of the title - [Book Title], [ISBN].

| Field | Value |
|-------|-------|
| Total no of Permission items | [Count] |
| Permissions to be cleared | [Count] |
| Elsevier permissions | [Count] |
| Third Party permissions Split | Publishers: [X], Companies: [X], Courtesy of: [X], First time Contacts: [X], Total: [X] |
| High Fee permission items | [Count] |
| High TAT copyright holders | [Count] |
| Restriction list | [Not Applicable/Available] |
| Chapter author information | [Not Available/Available] |
| Approximate project completion date | [Date] |

Additional Notes:
[Notes about specific items, high fees, or issues]
```

### 8. Permissions Update Email (to Authors)

**Subject**: < [Book Title] ; [ISBN] > : Permissions update

**From**: permissionshelpdesk@elsevier.com

**Attachments**:
- Sample permission log.xlsx
- Permission log.xlsx
- Permission Guidelines.docx

**Template**:
```
Dear Author,

I hope you are well. I am writing with regard to the permissions for the book [Book Title].

As you are likely already aware, as the author you are responsible for obtaining written permission to reuse any third-party images, figures, tables and/or substantial text excerpts appearing in your [chapter/book] and for providing copies of these permissions.

Kindly note that we cannot legally publish the book until we receive the permission files for your chapter/book.

If you have accepted writing the book/chapters in EMSS platform. Please follow the below steps:

- Step 1: We ask that you submit both the completed permission log and copies of all permission licenses for any third-party images, figures, tables, boxes used in your [chapter/book] to Permissions Helpdesk (permissionshelpdesk@elsevier.com). Please ensure to update the yellow highlighted columns in the permission log which are mandatory fields. A sample permission log is also attached for your reference.

- Step 2: Obtain any necessary permissions licenses or other approvals in writing from the rightsholders of the materials – this is usually but not always the publisher for any published works. Please also be aware that some publishers may have a longer turnaround time and some permissions may also be subject to fees.

- Step 3: If your [chapter/book] exclusively contains only figures/tables created by you or your co-author and therefore requires no permissions, please confirm the same to Permissions Helpdesk.
```

### 9. Permission Reminder Emails

**Subject**: Re: Permission Reminder<[Author Name] / [Chapter Title], [ISBN]>

**Email Chain Pattern**:
- First Reminder
- Second Reminder
- First Chaser
- Second Chaser
- Third Chaser

**Reminder Schedule Fields in RPC**:
| Field | Description |
|-------|-------------|
| Intro Email Due Date | Initial email date |
| Intro Email Sent Date | Sent confirmation |
| MS Due Date | Manuscript due |
| First Reminder Due Date | First reminder |
| Second Reminder Sent Date | Second reminder sent |
| First Chaser Due Date | First follow-up |
| First Chaser Sent Date | First follow-up sent |
| Second Chaser Due Date | Second follow-up |

---

## 15. File Naming Conventions

### Permission Log Files
- `[ISBN]_RPC-PermLog.xlsx`
- `[ISBN]_RPC-perm log-MASTER`
- `RPC Permission log_[Author Name] Final`
- `$RPC Permission log_[Author Name] Final`

### Cost Sheet Files
- `[ISBN]_Cost Sheet.xlsx`

### Analysis Report Files
- `Analysis Report - [Author Name]: [Title], [ISBN]`

### Figure List Files
- `21263_figlist_CPM_MRM_RP`

### Chapter Upload Files
- `chapter_upload 1 - Copy`

### Permission Grants Folder
- `Permission Grants` (folder)

---

## 16. Workflow File Location Structure

### OneDrive/SharePoint Path
```
Saravanan - Reed Elsevier Group ICO: Reed Elsevier Inc
└── Desktop
    └── Backup
        └── [Author Name], [Edition] - [Language]
            ├── Permission Grants/
            ├── 21263_figlist_CPM_MRM_RP
            ├── Sample RPC Permission log
            └── [Additional files]
```

### File Types Used
| Extension | Application |
|-----------|-------------|
| .xlsx | Microsoft Excel Workbook |
| .docx | Microsoft Word Document |
| .pdf | Adobe Acrobat Document |
| .msg | Outlook Item (Email) |

---

## 17. Integration Points

### External Systems
| System | Purpose | URL |
|--------|---------|-----|
| CCC RightsLink | Permission requests for non-STM publishers | s100.copyright.com |
| STM Permissions | Permissions between STM member publishers | stm-assoc.org |
| Wiley Online Library | Source content verification | onlinelibrary.wiley.com |
| PubMed/NIH | Source content verification | pubmed.ncbi.nlm.nih.gov |
| ResearchGate | Source content verification | researchgate.net |
| Google Search | Source verification | google.com |

### Internal Systems
| System | Purpose |
|--------|---------|
| EMSS | Electronic Manuscript Submission System |
| ELSA | Elsevier Author Platform |
| RPC | Rights and Permissions Collector |

### Bookmarks Bar Tools (Common)
| Tool | Purpose |
|------|---------|
| Search-Association | Association search |
| ElsevierAI Pro | AI assistance |
| NonSolus | Reference tool |
| CCC | Copyright Clearance Center |
| Scopus - Document | Document search |
| ClinicalKey | Clinical reference |
| AGAL | Unknown |
| R & P Collector | RPC quick access |
| STM Publishers list | Publisher reference |
| Elsa | ELSA quick access |
| EMSS | EMSS quick access |

---

## 18. Contributor Payments Report

### Excel Structure
| Column | Description |
|--------|-------------|
| ROLE | Contributor role |
| PHYSICAL ADDRESS | Address |
| CURRENCY TYPE | Currency code |
| COMPENSATION AMOUNT | Payment amount |
| CHAPTER NAME | Chapter title |
| CHAPTER NUMBER | Chapter number |
| PRINT OR EBOOK | Format type |

### Chapter List Example
1. Introduction to Medical-Engineering Interdisciplinary Microrobotic
2. Functional Design of Microrobots
3. Actuation Systems
4. Control Strategies
5. Imaging and Feedback Modalities
6. Integrated System Framework
7. Applications for Embolization and Occlusion
8. Applications for Thrombus Removal
9. Applications for Biofilm Eradication
10. Applications for Cancer Therapy
11. Challenges and Prospects for Clinical Applications
12. Intelligent Development of Microrobotic Systems

---

## 19. Project Content Manager Report

### Excel Columns
| Column | Description |
|--------|-------------|
| PROJECT CONTENT MANAGER(S) | Manager name |
| PROJECT CONTENT MANAGER EMAIL(S) | Email address |
| PROJECT EDITOR(S) | Editor name |
| PUBLICATION DATE | Date |
| CONTRIBUTOR FIRST NAME | First name |

---

## 20. Key Contacts and Roles

### Elsevier Team Members (from screenshots)
| Name | Role | Location |
|------|------|----------|
| Saravanan Murugan | Senior Copyrights Specialist | ELS-CHN |
| Subash Balakrishnan | Team Member | ELS-CHN |
| Rajendrababu, Hemamalini | Team Member | ELS-CHN |
| Babu, Jaya Shapna | Team Member | ELS-CHN |
| Balu, Vinoth Kumar | Team Member | ELS-CHN |
| Patrick | Team Member | - |
| Wesley | Team Member | - |
| Wenchong Wang | Editorial Contact | - |
| Siddharth Khattri | Editorial Contact | - |

### Email Addresses
| Purpose | Email |
|---------|-------|
| RPC Application | rpcapplication@elsevier.com |
| Permissions Seeking | permissionseeking@elsevier.com |
| Permissions Helpdesk | permissionshelpdesk@elsevier.com |
| Individual (Saravanan) | s.murugan@elsevier.com |
| Individual (Balakrishnan) | S.Balakrishnan1@Elsevier.Com |

---

## 21. System Notifications and Alerts

### External Email Warning
```
*** External email: use caution ***
```

### Trusted Partners Notice
```
*** External email: use caution. Browse home.relx.com -> Trusted partners to verify this Sender ***
```

### Meeting Recording Notice
```
Patrick invited Fireflies.ai here to record & take notes.
View Security & Privacy info: https://fireflies.ai/policy

Type:
'/ff leave' - Remove Fireflies

View Realtime notes here:
[Fireflies link]
```

### Tactiq Transcription Notice
```
Hi, I'm transcribing this call with my Tactiq AI Extension:
https://tactiq.io/transcribing
```

---

## 22. Summary Statistics

### System Capacity
| Metric | Value |
|--------|-------|
| Total Active Projects (Sample) | 47 - 2,865 |
| Total Completed Projects (Sample) | 579 - 8,890 |
| Annual Requests | 70,000 |
| Annual Projects | 6,000 |
| Annual System Record Updates | 10,000 |
| Organization FTE | 60+ |
| Different Processes | 12 |

### Permission Processing
| Metric | Sample Value |
|--------|--------------|
| Total Permission Items (per project) | 28-1308 |
| Permissions to be worked | Variable |
| Permissions Processed | Variable |
| Permissions Resolved | Variable |
| Typical Project Duration | 30 days prior to FTP |

---

---

## 23. ELSA Platform - Additional Features

### Permissions Files Tab
**URL Pattern**: `https://app.elsa.elsevier.com/document/{id}/resources/{resource-id}/edit?projectId={project-id}`

| Feature | Description |
|---------|-------------|
| Upload | Button to upload granted permissions files |
| Table Columns | Name, Size, Uploaded By, Uploaded Date, Placed in Document |
| Purpose | Upload all Granted Permissions files and supplemental files to share with co-contributors |
| Save Button | Saves uploaded files |

### Permission Log Tab
**URL Pattern**: `https://app.elsa.elsevier.com/document/{id}/permissionlogreport?projectId={project-id}`

| Column | Description |
|--------|-------------|
| # | Row number |
| Owner | Person who created the report |
| Report | Report type (Permission Logs) |
| Created→ | Creation date/time |
| Status | Waiting, Complete |

- **Run Button**: Generates permission log report
- Reports are queued and status updates when complete

### Publishing Assistant Tab
| Column | Description |
|--------|-------------|
| Name | Chapter name |
| Location | Section/Part location |
| Current Workflow Stage | Production, Draft, etc. |
| Word Count | Total words in chapter |
| Figures | Number of figures |
| References | Number of references |
| Tables | Number of tables |
| Boxes | Number of boxes |
| Callouts | Number of callouts |
| Permissions | Number of permission items |

**Download project reports** button available at top of tab.

### ELSA Project List View
**URL**: `https://app.elsa.elsevier.com/project/list`

| Feature | Description |
|---------|-------------|
| Search by project name | Text search field |
| Filter by Editor/Author | Dropdown filter |
| View Options | All projects, Due dates |
| Table Columns | Project Name, Editors/Authors, Publication Date |

---

## 24. RPC Chapter Tracker - Detailed View

### Chapter-Level Permission Tracking
| Column | Description |
|--------|-------------|
| Chapter No. | Chapter number |
| Chapter Title | Full chapter title |
| Authors | Chapter author names |
| Editor Email | Click to edit |
| Chapter Submitted | Yes/No/Date |
| Permission Received | Yes/No |
| Permission Status | Pending, Resolved (dropdown) |
| Comments | Free text field |

### Permission Status Dropdown Options
| Status | Description |
|--------|-------------|
| Pending | Awaiting resolution |
| Resolved | Permission obtained |
| Permission log and licenses yet to be received | Waiting for author submission |
| Permission log received, permission licenses yet to be received | Partial submission |

### Chapter Statistics Bar
| Metric | Display |
|--------|---------|
| Total Chapter | Count (e.g., 31) |
| Chapter completed | Count (e.g., 31) |
| Chapter pending | Count (e.g., 0) |
| Chapter completion | Percentage (e.g., 100%) |

### Action Buttons
- Save
- Upload
- Bulk Update
- Columns (customize view)
- Export Data

---

## 25. RPC Project Documents Tab

### Document Management Interface
| Feature | Description |
|---------|-------------|
| Upload new Document | Button to add files |
| Download document(s) | Button to download selected |
| Checkbox Selection | Select multiple documents |

### Document Table Columns
| Column | Description |
|--------|-------------|
| Document Title | Display name |
| File Name | System filename |
| Uploaded Date ↕ | Sortable date column |

### Common Document Types
| Document Type | Naming Convention |
|---------------|-------------------|
| Chapter Zip Files | Chapter 3, 6, 8, 9, 13, 16, 20.zip |
| Permission Logs | Chapter 1, 4, 7 & 10 Permission Log.xlsx |
| AWP Files | All chapters AWP.pdf / All chapters AWP.zip |
| Complete Packages | All chapters Complete.zip |

---

## 26. Permission Log Excel - Detailed Structure

### Column Headers (Full View)
| Column | Color Code | Description |
|--------|------------|-------------|
| Project ID / Publication Name | Yellow | Project identifier |
| Permission Status (Mandatory) | Yellow | Resolved, Pending, etc. |
| Chapter Title | Yellow | Chapter name |
| Elsevier Author Name | Yellow | Book/chapter author |
| Item ID (mandatory) | Yellow | Unique item identifier |
| Previous Edition Item ID | - | Reference to prior edition |
| PII/ID | - | Publication Item Identifier |
| Caption Title | - | Figure/table caption |
| Source (mandatory) | Green | Source reference |
| Source Chapter | - | Source chapter reference |
| Elsevier author and source author | Green | Combined author info |
| Credit Line Changes | Green | Change tracking |
| Original Figure Number | Green | Original reference number |
| Rightsholder | Green | Rights holder name |
| Permission Required (mandatory) | Green | Yes/No |
| Creator Type | Green | Author Created, Courtesy, etc. |
| Rightsholder Web Link | - | URL |
| Mode of Contact | - | CCC, Email, etc. |

### Creator Type Values
| Type | Description |
|------|-------------|
| Author Created | Original work by chapter author |
| Author's Original | Same as Author Created |
| Public Domain | No copyright restrictions |
| Courtesy Of | Provided as courtesy |
| 3rd Party Material | External copyrighted material |

### Sample Permission Log Data
| Permission Status | Chapter Title | Source | Creator Type |
|-------------------|---------------|--------|--------------|
| Resolved | Soil biodiversity | Author's Original | Author Created |
| Resolved | Potential changes | Author's Original | Author Created |
| Resolved | Heavy metal mobilization | Source citation with DOI | Springer |
| Resolved | Managing organic | Author's Original | Author Created |
| Resolved | Soil as a complex | No Permission Required | Author Created |

---

## 27. Credit Line Change Report

### Excel Structure
| Column | Description |
|--------|-------------|
| Chapter Title | Chapter name |
| Item Id | Figure/table identifier |
| Caption Title | Original caption |
| Creditline Changes | New/updated credit line text |

### Credit Line Examples
| Item | Original | Updated Credit Line |
|------|----------|---------------------|
| Figure 10.1 | - | From Tóth, G., Montanarella, L., Rusco, E., 2008. Threats to soil quality in Europe. Joint Research Centre... |
| Figure 10.2 | - | Adapted from the original Hassani, A., Azapagic, A., Shokri, N., 2021... used under CC BY 4.0 |
| Figure 10.3 | - | Figure was drawn to synthesize information described in the paper (Daliakopoulos, I.N., Tsanis, I.K...) |

---

## 28. CCC RightsLink - Request Details Form

### Type of Use (TOU) Options
| Option | Description |
|--------|-------------|
| Educational/Instructional Program | Academic use |
| Commercial | For-profit use |
| Internal Business Use | Company internal |
| Promotional | Marketing materials |

### Portion Type Options
| Option |
|--------|
| Chapter/article |
| Figure/table |
| Text extract |
| Full work |

### Rights Requested Options
| Option | Description |
|--------|-------------|
| Main product | Primary publication |
| Promotional | Marketing use |
| Internal | Company internal use |

### Additional Form Fields
| Field | Required | Options |
|-------|----------|---------|
| Distribution * | Yes | Worldwide, Specific territories |
| Translation * | Yes | Original language of publication, Specific language |
| Format | Yes | Print, Electronic, Print and Electronic |
| Copies for the Disabled? * | Yes | Yes, No |
| Page Range(s) | No | Text input |
| Total Number of Pages * | Yes | Number input |

---

## 29. Permission Grant Documentation

### PDF Email Format (Author Confirmation)
```
From: [Author Name] <email@institution.edu>
Sent: [Date and Time]
To: [Copyrights Specialist]
Subject: Re: Permission Reminder - [Project Title], [ISBN]

*** External email: use caution ***

All tables and figures are my original creation
[Date]

[Author Name] napsal:
Dear Dr. [Author Name],

Hope this mail finds you well!
```

### Confirmation Statement Templates
| Type | Statement |
|------|-----------|
| Original Creation | "All tables and figures are my original creation" |
| Figure Replacement | "The authors of Chapter [X] want to replace [figure]. The attached figure is original; therefore, no permission is required." |
| No Third-Party Content | "My [chapter/book] exclusively contains only figures/tables created by me or my co-author and therefore requires no permissions" |

---

## 30. Editorial System (editorial.elsevier.com)

### URL
`https://editorial.elsevier.com/app/book?execution={id}`

### All Other Contributions Assigned To Me View
| Column | Description |
|--------|-------------|
| MANUSCRIPT AUTHORS | Author names |
| CURRENT STATUS DUE DATE | Status with deadline |
| PREVIOUS WORKFLOW STEP | Prior stage |
| LAST SENT | Date last action |

### Status Indicators
| Color | Meaning |
|-------|---------|
| Green squares | On track |
| Orange squares | Attention needed |
| Red flag | Overdue/urgent |

### Workflow Steps
| Step | Description |
|------|-------------|
| PM | Project Manager review |
| Creation | Initial creation |
| Production | In production |

### Sample Book Chapters (Carbon Nano-onions Project)
1. For internal Elsevier use only
2. Preface
3. 1: Carbon nano-onions
4. 2: Carbon nano-onions derived nanocomposites
5. 3: Advancements in carbon nano-onions reinforced conjugated matrix nanocomposites
6. 4: Cutting-edge thermoplastic nanocomposites with carbon nano-onions nano-additives

---

## 31. Permission Logs Report (ELSA Export)

### Report Header
```
Selected Parameters:
Project Id: [Project GUID]

Permission Logs Report for a Project
```

### Report Columns
| Column | Description |
|--------|-------------|
| Project ID / Publication Name | Full project name |
| Permission Status (Mandatory) | No Permission Needed, Resolved, etc. |
| Chapter Number | Chapter number |
| Chapter Title | Full chapter title |
| Elsevier Author Name | Chapter author |

### Status Values in Report
| Status | Meaning |
|--------|---------|
| No Permission Needed | Original content, no third-party material |
| Resolved | Permission obtained |
| Pending | Awaiting response |

---

## 32. Tier 1, 2, and 3 Workflow Details

### Tier 1 (Author Obtains All)
1. Author obtains all permissions
2. Author provides completed permission log
3. CS validates log completeness
4. CS uploads logs and files to RPC

### Tier 2 (Author Provides Log, CS Obtains)
1. Author provides permission log identifying items needing permission
2. CS reviews and validates log
3. CS contacts rightsholders to obtain permissions
4. CS tracks responses and chasers
5. CS uploads completed logs and files to RPC

### Tier 3 (Full Service)
1. Author submits manuscript only
2. CS reviews manuscript for third-party content
3. CS creates permission log from scratch
4. CS identifies all items requiring permissions
5. CS contacts all rightsholders
6. CS tracks all responses
7. CS uploads completed logs and files to RPC

### Tier 4 (HS Full Service)
Same as Tier 3, specifically for Health Sciences division with additional complexity handling.

---

## 33. ELSA Support Resources

### Help URLs
| Resource | URL |
|----------|-----|
| ELSA FAQ | https://service.elsevier.com/app/answers/detail/a_id/17532/ |
| ELSA Support Hub | https://service.elsevier.com/app/home/supporthub/elsa/ |
| ELSA Support Email | elsasupport@elsevier.com |

### ELSA Chapter Status Indicators
| Icon | Status | Description |
|------|--------|-------------|
| Red circle | Not Started | Chapter not begun |
| Orange circle | Draft | In draft stage |
| Yellow circle | Staff Review | Under editorial review |
| Green circle | Production | In production |
| Blue checkmark | Complete | Chapter finished |

---

## 34. Project Statistics Summary

### Sample Project: Medical-Engineering Interdisciplinary Microrobotic Systems
| Metric | Value |
|--------|-------|
| Total Chapters | 12 |
| Chapters in Production | 6 |
| Word Count Range | 1313 - 2318 |
| Figures per Chapter | 3-18 inserted |
| References per Chapter | 0-13 |
| Tables per Chapter | 0-3 inserted |
| Expected Callouts | 0-18 |
| Permissions per Chapter | 4-21 |

### Sample Project: Hospital and Healthcare Security
| Metric | Value |
|--------|-------|
| Total Chapters | 31 |
| Chapters Completed | 31 |
| Chapters Pending | 0 |
| Completion Rate | 100% |

### Sample Project: Applied Sports Analytics
| Metric | Value |
|--------|-------|
| Publication Date | 01-Nov-26 |
| ISBN | 9780443490682 |
| Status | In Production |
| Sections | Multiple (I, II) |
| Chapters | The Evolution of Sport Analytics, The Pythagorean Theorem of Sports, Applying the Pythagorean Theorem, Correlation, etc. |

---

## 35. Chapter Document Format (Word)

### Standard Chapter Structure
```
1    Chapter

2    INTRODUCTION TO [CHAPTER TITLE]

3    [SUBTITLE IF APPLICABLE]

4    [Blank line]

5    [Author Name] [Credentials]

6    [Address Line 1]

7    [Institution/Organization]

8    [Email Address]
```

### Author Credentials Format
| Component | Example |
|-----------|---------|
| Name | Paul J. Newey |
| Degrees | MBChB (Hons) BSc (Hons) DPhil MRCP |
| Position | Mailbox 12, Level 5, Division of Molecular & Clinical Medicine |
| Institution | Ninewells Hospital & Medical School, University of Dundee |
| Location | UK, DD1 9SY |
| Email | p.newey@dundee.ac.uk |

---

*Document Generated: December 2025*
*Source: HCM Publishing Services Demo Session Screenshots*
*System: Rights & Permissions Collector (RPC)*
*Organization: Elsevier / RELX Group*
