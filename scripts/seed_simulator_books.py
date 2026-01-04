#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import os
import re
import sys
import time
from pathlib import Path
from typing import Iterable, List, Optional

from pypdf import PdfReader
import psycopg
from psycopg.types.json import Json

BOOK_DEFAULTS = {
    "big_data_analysis_of_nanoscience_bibliometrics_patent_and_funding_data_2000_2019": (
        "Science & Technology",
        "Tier2",
    ),
    "coevolution_and_prediction_of_coupled_human_water_systems": (
        "Science & Technology",
        "Tier3",
    ),
    "from_globular_proteins_to_amyloids": ("Health Sciences", "Tier0"),
    "guidelines_for_climate_adaptive_forest_restoration_and_reforestation_projects": (
        "Science & Technology",
        "Tier2",
    ),
    "inclusive_radio_communications_for_5g_and_beyond": ("Science & Technology", "Tier1"),
    "science_for_policy_handbook": ("Science & Technology", "Tier2"),
    "tissue_barriers_in_disease_injury_and_regeneration": ("Health Sciences", "Tier4"),
}

CREATED_TYPE_BY_TIER = {
    "Tier0": "validation_only",
    "Tier1": "author_log",
    "Tier2": "author_log",
    "Tier3": "manuscript_scan",
    "Tier4": "log_provided",
    "RuleOf10": "rule_of_10",
}

BUDGET_BY_TIER = {
    "Tier0": 0,
    "Tier1": 1500,
    "Tier2": 3500,
    "Tier3": 6000,
    "Tier4": 2500,
    "RuleOf10": 0,
}

FIGURE_RE = re.compile(r"\bfig(?:ure)?\.?\s*(\d+(?:\.\d+)?[a-z]?)", re.IGNORECASE)
TABLE_RE = re.compile(r"\btable\.?\s*(\d+(?:\.\d+)?[a-z]?)", re.IGNORECASE)
CHAPTER_RE = re.compile(r"chapter[-_ ]*(\d+)(?:[-_ ]*([A-Za-z]))?", re.IGNORECASE)


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def title_from_dirname(name: str) -> str:
    name = name.replace("_", " ").replace("-", " ")
    words = [w for w in name.split() if w]
    title = " ".join(w.capitalize() for w in words)
    title = re.sub(r"\b(\d+)g\b", lambda m: f"{m.group(1)}G", title, flags=re.IGNORECASE)
    return title


def safe_truncate(value: Optional[str], max_len: Optional[int]) -> Optional[str]:
    if value is None:
        return None
    if max_len is None:
        return value
    value = str(value)
    if len(value) <= max_len:
        return value
    return value[:max_len]


def build_scenario_name(slug: str) -> str:
    base = f"{slug}-base"
    if len(base) <= 255:
        return base
    digest = hashlib.sha1(base.encode("utf-8")).hexdigest()[:6]
    return f"{base[: 255 - 7]}-{digest}"


def extract_chapter_number(filename: str) -> Optional[int]:
    match = CHAPTER_RE.search(filename)
    if not match:
        return None
    base = int(match.group(1))
    letter = match.group(2)
    if not letter:
        return base
    return base * 100 + (ord(letter.upper()) - ord("A") + 1)


def derive_chapter_title(path: Path) -> str:
    stem = path.stem.replace("_", " ")
    stem = re.sub(r"---+", " - ", stem)
    stem = re.split(r"\b(19|20)\d{2}\b", stem)[0]
    stem = re.sub(r"(?i)^chapter\s*[-_ ]*\d+\s*[-_ ]*", "", stem)
    stem = re.sub(r"\s+", " ", stem).strip(" -_")
    return stem or path.stem


def extract_text(pdf_path: Path, max_pages: int) -> str:
    try:
        reader = PdfReader(str(pdf_path))
    except Exception:
        return ""
    parts: List[str] = []
    for idx, page in enumerate(reader.pages):
        if idx >= max_pages:
            break
        try:
            parts.append(page.extract_text() or "")
        except Exception:
            continue
    return "\n".join(parts)


def extract_mentions(text: str, limit: int) -> List[str]:
    mentions: List[str] = []
    for match in FIGURE_RE.finditer(text):
        mentions.append(f"Figure {match.group(1)}")
    for match in TABLE_RE.finditer(text):
        mentions.append(f"Table {match.group(1)}")
    deduped: List[str] = []
    seen = set()
    for item in mentions:
        if item in seen:
            continue
        seen.add(item)
        deduped.append(item)
        if len(deduped) >= limit:
            break
    return deduped


def choose_books(books_dir: Path) -> Iterable[Path]:
    dirs = [d for d in books_dir.iterdir() if d.is_dir()]
    names = {d.name for d in dirs}
    for path in sorted(dirs):
        name = path.name
        if name.startswith("ScienceDirect_articles_"):
            continue
        if name.endswith("-1") and name[:-2] in names:
            continue
        yield path


def get_isbn(slug: str) -> str:
    digest = int(hashlib.sha1(slug.encode("utf-8")).hexdigest()[:12], 16)
    return f"978-{digest % 10**12:012d}"


def get_rpc_project_id(slug: str) -> str:
    cleaned = re.sub(r"[^A-Z0-9]+", "", slug.upper())
    core = cleaned[:20] or "BOOK"
    return f"SIM-{core}-001"


def connect_db(conn_str: str) -> psycopg.Connection:
    return psycopg.connect(
        conn_str,
        connect_timeout=10,
        keepalives=1,
        keepalives_idle=30,
        keepalives_interval=10,
        keepalives_count=5,
    )


def insert_scenario(cur, name: str, description: str, metadata: dict) -> str:
    cur.execute(
        """
        insert into sim.sim_scenarios
            (name, description, status, time_mode, start_at, metadata)
        values
            (%s, %s, 'ready', 'realtime', now(), %s)
        returning id
        """,
        (name, description, Json(metadata)),
    )
    return cur.fetchone()[0]


def insert_project(
    cur,
    scenario_id: str,
    project_title: str,
    division: str,
    tier: str,
    rpc_project_id: str,
    isbn: str,
    permission_deadline: dt.date,
    publication_date: dt.date,
    permission_budget: float,
    max_cost_per_item: float,
) -> str:
    cur.execute(
        """
        insert into sim.sim_projects
            (scenario_id, rpc_project_id, project_title, isbn, division, tier,
             submission_route, permission_deadline, publication_date,
             permission_budget, max_cost_per_item, currency,
             cs_name, cs_email, cds_name, cds_email, status)
        values
            (%s, %s, %s, %s, %s, %s,
             'RPC', %s, %s,
             %s, %s, 'USD',
             'Auto CS', 'auto-cs@example.test',
             'Auto CDS', 'auto-cds@example.test',
             'new')
        returning id
        """,
        (
            scenario_id,
            rpc_project_id,
            project_title,
            isbn,
            division,
            tier,
            permission_deadline,
            publication_date,
            permission_budget,
            max_cost_per_item,
        ),
    )
    return cur.fetchone()[0]


def insert_rightsholder(
    cur,
    scenario_id: str,
    name: str,
    holder_type: str,
    contact_email: Optional[str],
    portal_url: Optional[str],
) -> str:
    cur.execute(
        """
        insert into sim.sim_rightsholders
            (scenario_id, name, type, contact_email, portal_url)
        values
            (%s, %s, %s, %s, %s)
        returning id
        """,
        (scenario_id, name, holder_type, contact_email, portal_url),
    )
    return cur.fetchone()[0]


def insert_chapter(
    cur,
    scenario_id: str,
    project_id: str,
    chapter_number: int,
    chapter_title: str,
    author_name: str,
    author_email: str,
) -> str:
    cur.execute(
        """
        insert into sim.sim_chapters
            (scenario_id, project_id, chapter_number, chapter_title,
             author_name, author_email, status)
        values
            (%s, %s, %s, %s, %s, %s, 'in_progress')
        returning id
        """,
        (
            scenario_id,
            project_id,
            chapter_number,
            chapter_title,
            author_name,
            author_email,
        ),
    )
    return cur.fetchone()[0]


def insert_rights_item(
    cur,
    scenario_id: str,
    project_id: str,
    chapter_id: str,
    rightsholder_id: str,
    item_id: str,
    caption: str,
    source_info: str,
    rightsholder_name: str,
    created_type: str,
    mode_of_contact: str,
    fee_amount: Optional[float],
    fee_currency: Optional[str],
) -> None:
    cur.execute(
        """
        insert into sim.sim_rights_items
            (scenario_id, project_id, chapter_id, rightsholder_id, item_id,
             caption, source_info, rightsholder_name, created_type,
             mode_of_contact, permission_required, notification_required,
             fee_amount, fee_currency)
        values
            (%s, %s, %s, %s, %s,
             %s, %s, %s, %s,
             %s, true, false,
             %s, %s)
        """,
        (
            scenario_id,
            project_id,
            chapter_id,
            rightsholder_id,
            item_id,
            caption,
            source_info,
            rightsholder_name,
            created_type,
            mode_of_contact,
            fee_amount,
            fee_currency,
        ),
    )


def insert_document(
    cur,
    scenario_id: str,
    project_id: str,
    doc_type: str,
    filename: str,
    storage_key: str,
    content_type: str,
) -> None:
    cur.execute(
        """
        insert into sim.sim_documents
            (scenario_id, project_id, doc_type, filename, storage_key, content_type, size_bytes)
        values
            (%s, %s, %s, %s, %s, %s, 0)
        """,
        (scenario_id, project_id, doc_type, filename, storage_key, content_type),
    )


def insert_mailbox(cur, scenario_id: str, address: str, role: str, display_name: str) -> None:
    cur.execute(
        """
        insert into sim.sim_mailboxes
            (scenario_id, address, role, display_name)
        values
            (%s, %s, %s, %s)
        """,
        (scenario_id, address, role, display_name),
    )


def insert_event(cur, scenario_id: str, event_type: str, payload: dict) -> None:
    cur.execute(
        """
        insert into sim.sim_events
            (scenario_id, event_type, payload, scheduled_at, status)
        values
            (%s, %s, %s, now(), 'scheduled')
        """,
        (scenario_id, event_type, Json(payload)),
    )


def insert_clock(cur, scenario_id: str) -> None:
    cur.execute(
        """
        insert into sim.sim_clock
            (scenario_id, clock_time, speed, paused)
        values
            (%s, now(), 1.0, false)
        """,
        (scenario_id,),
    )


def build_chapter_payloads(
    pdf_paths: List[Path], max_pages: int, max_items: int
) -> List[dict]:
    used_numbers = set()
    chapter_records = []
    for pdf_path in pdf_paths:
        if "chapter" not in pdf_path.name.lower():
            continue
        chapter_records.append((extract_chapter_number(pdf_path.name), pdf_path))
    chapter_records.sort(key=lambda item: (item[0] is None, item[0] or 0, item[1].name))

    payloads = []
    next_fallback = 1
    for number, pdf_path in chapter_records:
        if number is None or number in used_numbers:
            while next_fallback in used_numbers:
                next_fallback += 1
            number = next_fallback
            next_fallback += 1
        used_numbers.add(number)

        chapter_title = safe_truncate(derive_chapter_title(pdf_path), 500)
        author_name = safe_truncate(f"Author {number}", 255)
        author_email = safe_truncate(f"author{number}@example.test", 255)

        text = extract_text(pdf_path, max_pages)
        mentions = extract_mentions(text, max_items)
        if not mentions:
            mentions = ["Figure 1"]

        payloads.append(
            {
                "number": number,
                "title": chapter_title,
                "author_name": author_name,
                "author_email": author_email,
                "pdf_name": pdf_path.name,
                "mentions": mentions,
            }
        )

    return payloads


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--books-dir", required=True)
    parser.add_argument("--conn", default=os.getenv("SIM_DB_URL") or os.getenv("DATABASE_URL"))
    parser.add_argument("--max-pages", type=int, default=8)
    parser.add_argument("--max-items-per-chapter", type=int, default=12)
    args = parser.parse_args()

    if not args.conn:
        print("Missing --conn or SIM_DB_URL/DATABASE_URL.", file=sys.stderr)
        return 2

    books_dir = Path(args.books_dir).expanduser()
    if not books_dir.exists():
        print(f"Books directory not found: {books_dir}", file=sys.stderr)
        return 2

    created = 0
    skipped = 0

    for book_dir in choose_books(books_dir):
        pdf_paths = sorted(book_dir.glob("*.pdf"))
        if not pdf_paths:
            continue

        raw_name = book_dir.name
        slug = slugify(raw_name)
        scenario_name = safe_truncate(build_scenario_name(slug), 255)

        with connect_db(args.conn) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "select id from sim.sim_scenarios where name = %s",
                    (scenario_name,),
                )
                existing = cur.fetchone()
        if existing:
            skipped += 1
            continue

        title = title_from_dirname(raw_name)
        division, tier = BOOK_DEFAULTS.get(raw_name, ("Science & Technology", "Tier2"))
        created_type = CREATED_TYPE_BY_TIER.get(tier, "author_log")

        permission_deadline = dt.date.today() + dt.timedelta(days=120)
        publication_date = dt.date.today() + dt.timedelta(days=180)
        permission_budget = BUDGET_BY_TIER.get(tier, 2500)
        max_cost_per_item = 150.0 if division == "Health Sciences" else 200.0

        isbn = safe_truncate(get_isbn(slug), 20)
        rpc_project_id = safe_truncate(get_rpc_project_id(slug), 50)

        description = safe_truncate(f"Seeded from PDFs in {book_dir}", None)
        metadata = {
            "source": "pdf",
            "book_dir": str(book_dir),
            "pdf_count": len(pdf_paths),
        }

        chapter_payloads = build_chapter_payloads(
            pdf_paths, args.max_pages, args.max_items_per_chapter
        )

        for attempt in range(2):
            try:
                with connect_db(args.conn) as conn:
                    with conn.transaction():
                        with conn.cursor() as cur:
                            scenario_id = insert_scenario(
                                cur, scenario_name, description, metadata
                            )

                            project_id = insert_project(
                                cur,
                                scenario_id,
                                safe_truncate(title, 500),
                                safe_truncate(division, 50),
                                safe_truncate(tier, 20),
                                rpc_project_id,
                                isbn,
                                permission_deadline,
                                publication_date,
                                permission_budget,
                                max_cost_per_item,
                            )

                            rightsholder_primary = insert_rightsholder(
                                cur,
                                scenario_id,
                                safe_truncate(f"{title} Permissions Desk", 255),
                                "publisher",
                                safe_truncate(f"permissions@{slug}.example.test", 255),
                                None,
                            )
                            rightsholder_secondary = insert_rightsholder(
                                cur,
                                scenario_id,
                                "Unknown Rightsholder",
                                "institution",
                                "rights@unknown.example.test",
                                None,
                            )

                            for chapter in chapter_payloads:
                                chapter_id = insert_chapter(
                                    cur,
                                    scenario_id,
                                    project_id,
                                    chapter["number"],
                                    chapter["title"],
                                    chapter["author_name"],
                                    chapter["author_email"],
                                )

                                for idx, mention in enumerate(chapter["mentions"], start=1):
                                    rightsholder_id = (
                                        rightsholder_primary
                                        if idx % 2 == 0
                                        else rightsholder_secondary
                                    )
                                    rightsholder_name = (
                                        f"{title} Permissions Desk"
                                        if idx % 2 == 0
                                        else "Unknown Rightsholder"
                                    )
                                    mode = ["email", "rightslink", "portal"][idx % 3]
                                    fee_amount = None
                                    fee_currency = None
                                    if mode == "rightslink" and tier not in {"Tier0", "RuleOf10"}:
                                        fee_amount = 50 + (idx % 5) * 25
                                        fee_currency = "USD"

                                    insert_rights_item(
                                        cur,
                                        scenario_id,
                                        project_id,
                                        chapter_id,
                                        rightsholder_id,
                                        safe_truncate(f"ITEM-{chapter['number']}-{idx:02d}", 50),
                                        f"{mention} from {chapter['title']}",
                                        f"PDF: {chapter['pdf_name']}",
                                        safe_truncate(rightsholder_name, 255),
                                        safe_truncate(created_type, 50),
                                        safe_truncate(mode, 50),
                                        fee_amount,
                                        fee_currency,
                                    )

                            author_display = "Author 1"
                            edition = "1st Ed"
                            docs = [
                                (
                                    "permission_log",
                                    f"{isbn}_RPC-PermLog.xlsx",
                                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                                ),
                                (
                                    "cost_sheet",
                                    f"{isbn}_Cost Sheet.xlsx",
                                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                                ),
                                (
                                    "analysis_report",
                                    f"Analysis Report - {author_display}: {title}, {isbn}",
                                    "application/pdf",
                                ),
                                (
                                    "wsr_report",
                                    f"Weekly Status Report - {title}, {edition}, {isbn}",
                                    "application/pdf",
                                ),
                                (
                                    "credit_line_change",
                                    f"Credit Line Change - {title}, {isbn}",
                                    "application/pdf",
                                ),
                            ]
                            for doc_type, filename, content_type in docs:
                                filename = safe_truncate(filename, 255)
                                storage_key = safe_truncate(
                                    f"sim/{scenario_name}/{filename}", 500
                                )
                                insert_document(
                                    cur,
                                    scenario_id,
                                    project_id,
                                    safe_truncate(doc_type, 50),
                                    filename,
                                    storage_key,
                                    safe_truncate(content_type, 100),
                                )

                            insert_mailbox(
                                cur,
                                scenario_id,
                                safe_truncate(f"cs+{slug}@example.test", 255),
                                "cs",
                                "Copyright Specialist",
                            )
                            insert_mailbox(
                                cur,
                                scenario_id,
                                safe_truncate(f"cds+{slug}@example.test", 255),
                                "cds",
                                "Content Development Specialist",
                            )
                            insert_mailbox(
                                cur,
                                scenario_id,
                                safe_truncate(f"rightsholder+{slug}@example.test", 255),
                                "rightsholder",
                                "Rightsholder",
                            )

                            payload = {
                                "rpc_project_id": rpc_project_id,
                                "project_title": title,
                                "division": division,
                                "tier": tier,
                                "isbn": isbn,
                            }
                            insert_event(cur, scenario_id, "ProjectCreatedOrUpdated", payload)
                            if tier in {"Tier1", "Tier2", "Tier4"}:
                                insert_event(cur, scenario_id, "PermissionLogUploaded", payload)
                            if tier == "Tier3":
                                insert_event(cur, scenario_id, "ManuscriptReceived", payload)

                            insert_clock(cur, scenario_id)
                break
            except psycopg.OperationalError as exc:
                if attempt >= 1:
                    raise
                print(f"Retrying {raw_name} after connection error: {exc}", file=sys.stderr)
                time.sleep(2)

        created += 1

    print(f"Created scenarios: {created}")
    print(f"Skipped existing: {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
