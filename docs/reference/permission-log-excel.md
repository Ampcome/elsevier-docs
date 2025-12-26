# Permission Log Excel Structure

## Overview

The Permission Log is an Excel workbook used to track permission items for a project. It follows a standardized format with color-coded columns to indicate mandatory fields and data categories.

## File Naming Convention

```
[ISBN]_RPC-PermLog.xlsx
[ISBN]_RPC-perm log-MASTER.xlsx
RPC Permission log_[Author Name] Final.xlsx
```

## Sheet 1: Item Upload Format

### Column Categories by Color

| Color | Purpose | Fields |
|-------|---------|--------|
| **Yellow** | Mandatory fields | Core identification data |
| **Green** | Source/Rights info | Rights holder details |
| **Orange** | Date tracking | Timeline fields |
| **Blue** | Financial data | Invoice/cost tracking |

### Yellow Columns (Mandatory)

| Column | Description | Example |
|--------|-------------|---------|
| **Project ID / Publication Name** | Project identifier | PRJ-2024-12345 |
| **Permission Status (Mandatory)** | Current status | Resolved, Pending |
| **Chapter Title** | Chapter name | "Cardiovascular Imaging" |
| **Elsevier Author Name** | Book/chapter author | "Raymond J. Kim" |
| **Item ID (mandatory)** | Unique item identifier | ITM-2024-67890 |
| **Previous Edition Item ID** | Reference to prior edition | ITM-2022-12345 |
| **PII/ID** | Publication Item Identifier | S0123-4567(24)00001-X |
| **Caption Title** | Figure/table caption | "Figure 3.1 ECG tracing" |
| **Source (mandatory)** | Full source citation | "Smith J. Nature. 2023" |
| **Source Chapter** | Source chapter reference | "Chapter 5" |

### Green Columns (Source/Rights)

| Column | Description | Example |
|--------|-------------|---------|
| **Elsevier author and source author** | Combined author info | Same as source |
| **Credit Line Changes** | Change tracking | "Updated per rights holder" |
| **Original Figure Number** | Original reference | "Figure 2A" |
| **Rightsholder** | Rights holder name | "Springer Nature" |
| **Permission Required (mandatory)** | Yes/No | Yes |
| **Creator Type** | Type of content | Author Created |
| **Rightsholder Web Link** | URL | https://springer.com |
| **Mode of Contact** | Contact method | CCC, Email |
| **Rightsholder Email Address** | Contact email | permissions@springer.com |

### Orange Columns (Dates)

| Column | Description | Format |
|--------|-------------|--------|
| **Applied Date** | Date request sent | DD-MMM-YYYY |
| **Resolved Date** | Date permission granted | DD-MMM-YYYY |
| **Resolved Time (days)** | Days to resolution | Number |
| **Email Chaser 1 date** | First follow-up | DD-MMM-YYYY |
| **Email Chaser 2 date** | Second follow-up | DD-MMM-YYYY |

### Blue Columns (Financial)

| Column | Description | Example |
|--------|-------------|---------|
| **Restrictions** | Usage restrictions | "Print only" |
| **Invoice Amount** | Permission cost | 150.00 |
| **Currency** | Currency code | USD |
| **Invoice Number** | Invoice ID | INV-2024-001 |
| **Invoice Processing Mode** | Payment type | Credit card |
| **Invoice Processed Date** | Payment date | DD-MMM-YYYY |
| **Invoice Status** | Payment status | Paid |

## Sheet 2: Reference Data

### Permission Status Values

| Status | Description | When to Use |
|--------|-------------|-------------|
| **Resolved** | Permission obtained | Grant received |
| **Pending** | Awaiting response | Request sent, no reply |
| **Yet to Apply** | Not yet requested | In queue |
| **Editorial/Author Query** | Query raised | Clarification needed |
| **Waiver** | Permission waived | Free grant |
| **Deleted** | Item removed | Content not used |

### Source Types

| Source Type | Description |
|-------------|-------------|
| **Author Created** | Original work by chapter author |
| **Elsevier Books** | Content from Elsevier book |
| **Elsevier Journals** | Content from Elsevier journal |
| **Courtesy Of** | Provided as courtesy |
| **Adapted/Modified/Redrawn** | Modified from original |
| **3rd party material** | External copyrighted content |
| **Unrestricted** | No restrictions |
| **Public Domain** | No copyright |
| **STM Opt-Out** | Publisher opted out of STM |
| **STM Not Opt-Out** | STM guidelines apply |
| **Resolved by Editorial/Author** | Handled outside team |
| **Multiple Sources** | Combined from multiple sources |
| **Data from** | Data attribution |

### Creator Types

| Type | Description |
|------|-------------|
| **Author Created** | Original work by author |
| **Author's Original** | Same as Author Created |
| **Courtesy** | Provided as courtesy |
| **Used** | Existing content reused |
| **3rd Party Material** | External copyrighted work |
| **Public Domain** | No copyright restrictions |

### Mode of Contact Values

| Mode | When to Use |
|------|-------------|
| **CCC** | Copyright Clearance Center |
| **Email** | Direct email contact |
| **Online Form** | Publisher web form |
| **RightsLink** | CCC RightsLink portal |
| **(Blank)** | Not yet determined |

## Sample Permission Log Data

| Permission Status | Chapter Title | Source | Creator Type |
|-------------------|---------------|--------|--------------|
| Resolved | Soil biodiversity | Author's Original | Author Created |
| Resolved | Potential changes | Author's Original | Author Created |
| Resolved | Heavy metal mobilization | DOI: 10.1007/xxx | Springer |
| Pending | Managing organic | Waiting for reply | 3rd Party |
| Resolved | Soil as a complex | No Permission Required | Author Created |

## Credit Line Change Tracking

When credit lines change, document in the log:

| Item ID | Caption Title | Credit Line Changes |
|---------|---------------|---------------------|
| Fig-10.1 | Soil threats | From Tóth, G., et al., 2008... |
| Fig-10.2 | Data analysis | Adapted from Hassani, A., under CC BY 4.0 |
| Fig-10.3 | Synthesis diagram | Drawn from information in paper |

## Best Practices

### Data Entry Guidelines

1. **Always complete yellow columns** - These are mandatory
2. **Use dropdown values** - Select from predefined lists
3. **Date format consistency** - Use DD-MMM-YYYY
4. **Source completeness** - Include full citation with DOI
5. **Status accuracy** - Update immediately when status changes

### Quality Checks

- [ ] All mandatory (yellow) fields completed
- [ ] Status values from approved list
- [ ] Dates in correct format
- [ ] Invoice amounts in USD
- [ ] Source citations complete with DOI
- [ ] Credit lines match grant requirements

## Integration with RPC

The Permission Log syncs with RPC:

1. **Download** from RPC at project start
2. **Update** locally as work progresses
3. **Upload** back to RPC periodically
4. **Final upload** at project completion

### File Attachments

For each project, attach:
- `[ISBN]_RPC-PermLog.xlsx` - Main permission log
- `[ISBN]_Cost Sheet.xlsx` - Financial summary
- Permission grant files (PDF emails, licenses)
