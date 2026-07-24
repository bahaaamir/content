#!/usr/bin/env python3
"""
sync-vault.py
-------------
Keeps this Obsidian vault's folder/file structure in sync with `00 - Index.md`.

HOW TO USE (whenever you add a new topic or a new folder to the Index):
  1. Add a new `[[Topic Name]]` bullet under the relevant `## 📂 NN - Folder Name`
     heading in `00 - Index.md` (or add a whole new `## 📂` heading for a new folder).
  2. Run:  python3 sync-vault.py
  3. It will:
       - create any missing folders
       - create a placeholder .md file ONLY for topics that don't have one yet
       - NEVER touch or overwrite a file that already exists (so your written
         content is always safe, even if you fill files in and re-run this)
       - warn you about "orphan" files: files on disk whose topic no longer
         appears in the Index (e.g. you renamed or removed a topic), so you
         can decide whether to rename/delete them manually.

CONVENTIONS ENFORCED (keep these in mind if you edit the Index by hand):
  - Topic names must not contain: \\ / : * ? " < > |  (Windows filename rules)
  - Use " - " instead of ":" for sub-titles, e.g. "DNS Architecture - Resolution..."
  - Use "-" instead of "/" e.g. "CI-CD" not "CI/CD"
  - Every placeholder file's first line is `# Topic Name`, followed by a
    blank line and a backlink `[[00 - Index]]`
"""
import re
import os

INDEX_FILE = "00 - Index.md"
FORBIDDEN = set('\\/:*?"<>|')


def sanitize_check(name, kind):
    bad = FORBIDDEN & set(name)
    if bad:
        raise ValueError(f"{kind} '{name}' contains forbidden character(s): {bad}")
    if name.endswith((".", " ")):
        raise ValueError(f"{kind} '{name}' has a trailing dot/space (invalid on Windows)")


def parse_index(path):
    with open(path, encoding="utf-8") as f:
        content = f.read()
    folder_pattern = re.compile(r"^## 📂 (.+)$", re.MULTILINE)
    matches = list(folder_pattern.finditer(content))
    sections = []
    for i, m in enumerate(matches):
        folder_name = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        body = content[start:end]
        topics = re.findall(r"\[\[(.+?)\]\]", body)
        sections.append((folder_name, topics))
    return sections


def main():
    sections = parse_index(INDEX_FILE)

    created_folders = 0
    created_files = 0
    skipped_existing = 0
    expected_paths = set()

    for folder_name, topics in sections:
        sanitize_check(folder_name, "Folder")
        if not os.path.isdir(folder_name):
            os.makedirs(folder_name, exist_ok=True)
            created_folders += 1
            print(f"[+ folder] {folder_name}")

        for topic in topics:
            sanitize_check(topic, "Topic")
            filepath = os.path.join(folder_name, f"{topic}.md")
            expected_paths.add(os.path.normpath(filepath))

            if os.path.exists(filepath):
                skipped_existing += 1
                continue

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# {topic}\n\n[[00 - Index]]\n")
            created_files += 1
            print(f"[+ file]   {filepath}")

    # Detect orphan files: .md files on disk (inside known folders) not in the Index anymore
    orphans = []
    known_folders = {folder_name for folder_name, _ in sections}
    for folder_name in known_folders:
        if not os.path.isdir(folder_name):
            continue
        for fname in os.listdir(folder_name):
            if not fname.endswith(".md"):
                continue
            full = os.path.normpath(os.path.join(folder_name, fname))
            if full not in expected_paths:
                orphans.append(full)

    print("\n--- Sync summary ---")
    print(f"Folders created:   {created_folders}")
    print(f"Files created:     {created_files}")
    print(f"Files already existed (untouched): {skipped_existing}")
    if orphans:
        print(f"\n⚠ Orphan files (on disk but no longer in the Index) — review manually:")
        for o in orphans:
            print(f"   {o}")
    print("\nDone. Existing content was never overwritten.")


if __name__ == "__main__":
    main()
