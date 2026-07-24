# 00 - Overview

This vault is a personal knowledge base for **production-grade backend engineering and AI engineering mastery**. It covers the full stack of concerns a senior backend/platform engineer faces: from how packets move across the internet, through runtimes, architecture, databases, and distributed systems, to operating, securing, and observing systems in production — and finally to building LLM-powered, agentic backends.

The goal is depth over breadth: every topic is meant to become a self-contained, reference-quality note you can return to when designing, debugging, or interviewing.

---

## How to Use This Vault

The vault is built around three simple moving parts:

1. **`00 - Index.md` (Map of Content)** — the single source of truth. It contains 9 sections (`## 📂 01 - ...` through `## 📂 09 - ...`), and every topic in the vault is listed exactly once as a `[[Topic Name]]` wiki-link under its folder's section.
2. **The 9 numbered folders** — each `## 📂` section in the Index corresponds to one numbered folder on disk, and each `[[Topic Name]]` link corresponds to exactly one `.md` file inside that folder.
3. **Backlinks** — every topic file ends with (or starts with, as a placeholder) a `[[00 - Index]]` link back to the Index, so you can always navigate topic → Index → any other topic without using the file explorer.

Typical workflow:

- Start at `00 - Index.md`, pick a section, and click a topic link.
- In Obsidian, use the **backlinks pane** and **graph view** to see how topics connect — the Index acts as the central hub.
- To add a topic: edit `00 - Index.md` only, then run `python3 sync-vault.py`. The script creates any missing folders/files and never overwrites existing content.
- Fill in placeholders using the **Content Template** below.

---

## Suggested Reading Order

The folders are numbered in a deliberate bottom-up progression. Recommended path:

1. **01 - Protocols and Core Infrastructure** — Everything you build ultimately travels over TCP/IP, HTTP, and DNS. Start here so later topics (load balancing, SSE, gateways) have solid ground.
2. **02 - Advanced Runtimes and Frameworks** — Once you know how the network works, learn how code actually executes: processes, the event loop, containers, and the framework (NestJS) used throughout the vault.
3. **03 - Modern Software Architecture and Monorepos** — With mechanics in place, study how to *structure* systems: SOLID, DDD, Clean/Hexagonal Architecture. These design principles inform every decision in later folders.
4. **04 - Advanced Databases and Caching** — The data layer comes next, because replication, sharding, and the CAP theorem here are the direct bridge into distributed systems.
5. **05 - Distributed Systems and Event-Driven Architecture** — Builds immediately on 04: CAP/PACELC leads into consensus, sagas, Kafka, and CQRS. Doing these back-to-back keeps the mental model continuous.
6. **06 - API Engineering, Security, and Observability** — The "front door and instrumentation" of everything built in 01–05: how systems are exposed, secured, and made measurable.
7. **08 - Testing, Resilience, and DevOps Practices** — Harden what you can now build: testing strategies, circuit breakers, CI/CD, and IaC turn designs into production-grade systems. (Read before 09 so global infrastructure is discussed with failover/DR vocabulary already in place.)
8. **09 - Storage, CDN, and Global Infrastructure** — Extends hardened systems to planetary scale: object storage, edge caching, multi-region failover, data residency.
9. **07 - AI Engineering, LLM Automation, and MCP** — Deliberately last. Nearly every AI topic builds on earlier folders: SSE streaming (01), async runtimes (02), architecture patterns (03), vector databases and semantic caching (04), event-driven pipelines (05), gateways and observability (06), and resilience/fallback strategies (08). With those foundations, this folder becomes application rather than new theory.

Within each folder, reading top-to-bottom in Index order works well — foundational topics are listed before their dependents.

---

## Conventions

These rules are what keep the Index, the folders, and the sync script in agreement. Follow them exactly:

1. **Index-driven topics** — Every topic is a `[[Topic Name]]` wiki-link inside its folder's section in `00 - Index.md`. If a topic is not in the Index, it does not officially exist in the vault.
2. **One file per topic** — Every topic gets exactly one `.md` file. Filename = the topic's link text + `.md`, placed inside the matching numbered folder.
   - Example: `[[Redis Advanced - Pub-Sub, Streams, Lua Scripting, and Clustering]]` under `## 📂 04 - Advanced Databases and Caching` lives at `04 - Advanced Databases and Caching/Redis Advanced - Pub-Sub, Streams, Lua Scripting, and Clustering.md`.
3. **Filename-safe topic names** — Topic names must never contain Windows-forbidden characters: `\ / : * ? " < > |`
   - Use ` - ` instead of `:` (e.g., "DNS Architecture - Resolution..." not "DNS Architecture: Resolution...").
   - Use `-` instead of `/` (e.g., "TCP-IP" not "TCP/IP", "I-O" not "I/O", "CI-CD" not "CI/CD").
4. **Placeholder format** — Every placeholder file starts with `# Topic Name` (H1 matching the filename), followed by a blank line, followed by `[[00 - Index]]`. Nothing else.
5. **Sync workflow** — Additions/changes to the topic list are made by editing `00 - Index.md` only, then running `python3 sync-vault.py`. The script creates missing folders/files and never overwrites existing files. Never manually create, rename, or delete topic files. If the script prints "orphan file" warnings (a file on disk with no matching Index entry), report them and confirm before resolving.

---

## Content Template

When filling in a topic file, replace the placeholder body (keeping the H1 title and the `[[00 - Index]]` backlink at the very top) with this structure:

```markdown
# Topic Name

[[00 - Index]]

> [!question] The Problem (Why This Exists)
> The root problem that existed before this technology/pattern was invented.
> Root cause first, solution second, beginner-friendly language.

> [!abstract] TL;DR
> A 2–4 sentence summary of the entire note.

## 📖 Definition
A plain-language analogy first, then the formal definition (2–4 sentences).

## 🎯 Why It Matters
Where this shows up in production systems; what breaks or improves when you
understand it; when to reach for it and when not to.

## 🧠 Core Concepts
- Key idea 1 — short explanation (explain every technical term inline at
  first use — the reader is a beginner)
- Key idea 2 — short explanation
- Key idea 3 — short explanation
(Add subsections, tables, or code blocks as the topic demands.)

## 💻 Example / Code Walkthrough
A Mermaid diagram and/or a real, working, commented code example — each
important line explained.

> [!balance] Trade-offs (المكسب والخسارة)
> No silver bullet: for every design decision, state what is gained and
> what is given up or paid for.

> [!warning] Common Pitfalls
> Beginner-level mistakes and how to avoid them.

> [!todo] Prerequisites
> What should be understood before this topic; link foundational vault
> topics where applicable.

## 🔗 Related Topics
- [[Other Topic in This Vault]] — how it connects
- [[Another Topic]] — how it connects

## 📚 References
- Primary sources, official docs, papers, talks.
```

---

## Reusable Prompt - Auto-Fill Topic Files

Copy-paste this prompt whenever you want the next placeholder filled. It fills **one file at a time**; run it again for each subsequent topic. Add new topics to `00 - Index.md` first and run `python sync-vault.py` so the placeholders exist.

```text
You are the Knowledge-Base Maintainer of this Obsidian vault. Fill in the next
remaining topic file — ONE file only.

1. Run `python list-remaining-topics.py --next 1` (use `python3` if that's what
   works on your machine) and fill ONLY the placeholder file it returns.
   Never re-fill a topic that already has content.
2. Keep the existing `# Title` H1 and the `[[00 - Index]]` backlink at the
   very top of the file.
3. Follow the "Content Template" in `00 - Overview.md` EXACTLY, in this order:
   > [!question] The Problem (Why This Exists) — the root problem/limitation
     that existed before this concept; root cause first, solution second;
     real history where applicable.
   > [!abstract] TL;DR — 2–4 sentences summarizing the whole note.
   ## 📖 Definition — a plain-language everyday analogy first, then the
     formal definition.
   ## 🎯 Why It Matters
   ## 🧠 Core Concepts — explain EVERY technical term inline at first use
     (the reader is a beginner programmer); short sentences, one new concept
     per sentence.
   ## 💻 Example / Code Walkthrough — a Mermaid diagram plus a real, complete,
     working, commented code example (prefer NestJS/Angular); include install
     commands and a short "how to verify it works" note.
   > [!balance] Trade-offs (المكسب والخسارة) — for EACH major design decision:
     concretely what is gained vs. what is paid; specific to this topic,
     never generic.
   > [!warning] Common Pitfalls — beginner-level mistakes, not advanced edge
     cases.
   > [!todo] Prerequisites — hard prerequisites vs. optional companion
     reading; use exact [[Wiki-Link]] names from `00 - Index.md`.
   ## 🔗 Related Topics — exact [[Wiki-Link]] names from `00 - Index.md` so
     Obsidian resolves them.
   ## 📚 References
4. Audience: beginner programmer with an Angular/NestJS background. Never
   assume prior knowledge of any acronym or concept.
5. Flag any time-sensitive numeric claims (rate limits, benchmarks,
   version-specific behavior) with "verify current limits before relying on
   this in production."
6. Do NOT create, rename, or delete any file. Do NOT touch `00 - Index.md`
   or `sync-vault.py`.
7. When done, run `python list-remaining-topics.py --count` and report the
   new remaining count.
```

---

[[00 - Index]]
