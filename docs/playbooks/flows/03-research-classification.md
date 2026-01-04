# Flow 03 - Research and Classification

## Purpose
Identify the rightsholder, determine permission requirements, apply STM rules, and set routing for each rights item.

## Trigger Types
- State-based: UnclassifiedRightsItem
- Event-based: EditorialDecision (classification overrides)

## Agents
- Research and Classification Agent

## Integrations
- crossref-lookup
- pubmed-lookup
- image-finder
- stm-guidelines

## Inputs and Preconditions
- rights_items created with source_info and item metadata
- created_types and publishers populated

## Steps
1) Validate and normalize source citation.
   - Extract DOI, publisher, title, year, and URL.
2) Look up metadata.
   - Use CrossRef and PubMed to confirm citation details.
3) Identify rightsholder.
   - Use publisher_name_mappings and publisher directories.
   - Check Image Finder for internal Elsevier assets.
4) Classify created_type and permission_required.
   - Map to the 16 required created types.
5) Apply STM logic.
   - Determine STM_OPT_OUT vs STM_NOT_OPT_OUT.
   - Apply thresholds for figures/tables and text.
6) Select mode_of_contact.
   - STM route, then RightsLink, then web form, then email.

## Table Updates
- rights_items: created_type, permission_required, notification_required, mode_of_contact, rightsholder_id, doi, article_title, journal_name, publication_year, identification_confidence
- rightsholders: type, name, contact_email, contact_url, publisher_id
- publishers: stm_status, rightslink_enabled, permissions_url, permissions_email
- crossref_cache: doi, publisher_name, title, journal_name, publication_year
- status_history and audit_log

## Outputs
- Items are routed to the correct path or marked as waiver if no permission required.

## Decision Rules
- STM thresholds: up to 3 figures/tables per article or chapter, 400 words per extract or 800 words total for journal text.
- STM_NOT_OPT_OUT: notification-only path unless thresholds exceeded.
- STM_OPT_OUT or non-member: permission required if third-party content.
- Elsevier-owned or public domain: no permission required.

## Human Decision Points
- Ambiguous source ownership or unclear creator attribution.
- Ambiguous license scope or attribution requirements.
