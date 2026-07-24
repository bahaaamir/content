#!/usr/bin/env python3
"""
list-remaining-topics.py
-------------------------
Scans all topic folders and reports which topic files are still empty
placeholders (just the header + backlink) versus which ones already have
real content written in them.

USAGE:
  python3 list-remaining-topics.py            # list all remaining (empty) topics
  python3 list-remaining-topics.py --count     # just print how many are left
  python3 list-remaining-topics.py --next 5    # print the next 5 remaining topics

A file is considered "still empty" if, after stripping whitespace, its
content is exactly:
    # Topic Name

    [[00 - Index]]
(i.e. nothing has been added beyond the original placeholder template).
Anything else (even one extra line) counts as "filled".
"""
import os
import re
import sys

FORBIDDEN_DIRS = {".git", "__pycache__"}


def is_placeholder(filepath, topic_name):
    with open(filepath, encoding="utf-8") as f:
        content = f.read().strip()
    expected = f"# {topic_name}\n\n[[00 - Index]]".strip()
    return content == expected


def find_topic_files():
    remaining = []
    filled = []
    for entry in sorted(os.listdir(".")):
        if not os.path.isdir(entry) or entry in FORBIDDEN_DIRS or entry.startswith("."):
            continue
        if not re.match(r"^\d\d - ", entry):
            continue  # not one of our numbered topic folders
        for fname in sorted(os.listdir(entry)):
            if not fname.endswith(".md"):
                continue
            topic_name = fname[:-3]
            filepath = os.path.join(entry, fname)
            if is_placeholder(filepath, topic_name):
                remaining.append(filepath)
            else:
                filled.append(filepath)
    return remaining, filled


def main():
    remaining, filled = find_topic_files()

    if "--count" in sys.argv:
        print(f"Remaining: {len(remaining)}")
        print(f"Filled:    {len(filled)}")
        return

    if "--next" in sys.argv:
        idx = sys.argv.index("--next")
        n = int(sys.argv[idx + 1]) if idx + 1 < len(sys.argv) else 1
        for path in remaining[:n]:
            print(path)
        return

    print(f"--- {len(filled)} filled / {len(remaining)} remaining ---\n")
    for path in remaining:
        print(path)


if __name__ == "__main__":
    main()
