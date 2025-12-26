# File Naming Conventions

## Overview

Consistent file naming ensures documents are organized, searchable, and properly associated with their permission items.

## Standard Format

```
[ProjectID]_[ItemID]_[DocType]_[Date]_[Version].[ext]
```

### Components

| Component | Format | Example |
|-----------|--------|---------|
| **ProjectID** | PRJ-YYYY-##### | PRJ-2024-12345 |
| **ItemID** | ITM-YYYY-##### | ITM-2024-67890 |
| **DocType** | 3-letter code | REQ, LIC, COR |
| **Date** | YYYYMMDD | 20240615 |
| **Version** | v# | v1, v2 |

## Document Type Codes

### Correspondence

| Code | Document Type |
|------|---------------|
| **REQ** | Permission request (outgoing) |
| **RES** | Response received |
| **FUP** | Follow-up message |
| **FIN** | Final/closing correspondence |

### Licenses & Approvals

| Code | Document Type |
|------|---------------|
| **LIC** | License document |
| **APR** | Approval email/letter |
| **DEN** | Denial documentation |
| **TRM** | Terms/conditions |

### Financial

| Code | Document Type |
|------|---------------|
| **INV** | Invoice |
| **QUO** | Quote |
| **PAY** | Payment confirmation |
| **PO** | Purchase order |

### Source Materials

| Code | Document Type |
|------|---------------|
| **SRC** | Source content (figure/table) |
| **CIT** | Citation/reference |
| **CRD** | Credit line |

## Examples

### Permission Request

```
PRJ-2024-12345_ITM-2024-67890_REQ_20240615_v1.pdf
```
Meaning: Permission request for item 67890 in project 12345, sent June 15, 2024, first version

### License Document

```
PRJ-2024-12345_ITM-2024-67890_LIC_20240701_v1.pdf
```
Meaning: License received for item 67890, dated July 1, 2024

### Follow-up Email

```
PRJ-2024-12345_ITM-2024-67890_FUP_20240622_v1.pdf
```
Meaning: Follow-up sent June 22, 2024

### Invoice

```
PRJ-2024-12345_ITM-2024-67890_INV_20240705_v1.pdf
```
Meaning: Invoice received July 5, 2024

## Folder Structure

### Project-Based Organization

```
/Permissions/
├── 2024/
│   ├── PRJ-2024-12345/
│   │   ├── Requests/
│   │   ├── Licenses/
│   │   ├── Correspondence/
│   │   └── Financial/
│   └── PRJ-2024-12346/
│       └── ...
└── 2023/
    └── ...
```

### Alternative: Item-Based

```
/Permissions/
├── Active/
│   ├── ITM-2024-67890/
│   │   ├── PRJ-2024-12345_ITM-2024-67890_REQ_20240615_v1.pdf
│   │   ├── PRJ-2024-12345_ITM-2024-67890_RES_20240620_v1.pdf
│   │   └── PRJ-2024-12345_ITM-2024-67890_LIC_20240701_v1.pdf
│   └── ITM-2024-67891/
└── Closed/
    └── ...
```

## Email Saving Guidelines

### What to Save

| Save | Don't Save |
|------|------------|
| All sent requests | Internal discussions |
| All responses | Duplicates |
| Approvals/denials | Auto-replies |
| Fee negotiations | |
| Final agreements | |

### How to Save

1. Save as PDF (not .msg)
2. Include complete email thread
3. Use standard naming convention
4. Attach to RPC item

## Version Control

### When to Increment

| Scenario | Version |
|----------|---------|
| Initial document | v1 |
| Minor correction | v1 (replace) |
| Significant revision | v2 |
| After response received | v2 (if revised) |
| Final signed version | FINAL |

### Version Notes

Add brief note in filename if helpful:
```
PRJ-2024-12345_ITM-2024-67890_REQ_20240615_v2_revised-scope.pdf
```

## Special Cases

### Multiple Items Same Source

When requesting multiple items from same source:
```
PRJ-2024-12345_MULTI_REQ_20240615_v1_5items.pdf
```

Reference the specific items in document or spreadsheet.

### CCC RightsLink Downloads

```
PRJ-2024-12345_ITM-2024-67890_LIC_20240701_CCC-12345678.pdf
```
Include CCC license number for reference.

### Bulk Spreadsheets

```
PRJ-2024-12345_BULK_ItemList_20240615_v1.xlsx
```
For tracking multiple items.

## Quality Checklist

Before saving:

- [ ] File name follows convention
- [ ] Document type code is correct
- [ ] Date is accurate
- [ ] Version is appropriate
- [ ] File is in correct folder
- [ ] Attached to RPC item
- [ ] PDF is readable/searchable

## Common Mistakes

| Mistake | Correct Approach |
|---------|-----------------|
| Spaces in filename | Use underscores |
| Special characters | Avoid &, %, # |
| Missing date | Always include |
| Wrong date format | Use YYYYMMDD |
| Generic names | Use specific codes |
| Duplicate files | Check before saving |
