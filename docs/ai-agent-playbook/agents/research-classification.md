# Agent Runbook - Research and Classification Agent

## Purpose
Identify rightsholders, apply STM rules, classify items, and select the contact route.

## Primary Responsibilities
- Normalize and enrich citations.
- Determine created_type and permission_required.
- Identify rightsholder and STM status.
- Set mode_of_contact.

## Trigger Types
- State-based: UnclassifiedRightsItem
- Event-based: EditorialDecision (classification overrides)

## Flows Covered
- Flow 03: Research and Classification

## Tables Read
- rights_items, created_types, publisher_name_mappings, publishers, rightsholders, crossref_cache

## Tables Written
- rights_items: created_type, permission_required, notification_required, rightsholder_id, mode_of_contact, doi, article_title, journal_name, publication_year
- rightsholders: name, type, contact_email, contact_url, publisher_id
- publishers: stm_status, rightslink_enabled, permissions_url
- crossref_cache
- status_history, audit_log

## Integrations
- crossref-lookup
- pubmed-lookup
- image-finder
- stm-guidelines

## Idempotency Rules
- Reuse existing rightsholder and publisher mappings when confidence is high.
- Avoid duplicate rightsholder records when names match existing mappings.

## Failure Handling
- If metadata cannot be resolved, set needs_manual_review on rights_items.

## Human Decision Points
- Ambiguous ownership or unclear creator attribution.
- License scope interpretations when classification is uncertain.
