# Canonical companion notes

This is the **authoritative Markdown knowledge base** for the spoiler-conscious *The Good Place Companion*. The `docs/` directory is a separately edited static presentation layer; changes under `notes/` are not automatically published there.

Start at [the notes index](INDEX.md) and the [Season 1 viewing notes](episodes/season-01/README.md).

| Directory | Responsibility |
| --- | --- |
| `episodes/` | Episode-specific summaries, philosophy, character developments, questions and evidence links |
| `people/characters/` | Introductory, spoiler-bounded character profiles |
| `people/philosophers/` | Intellectual biographies and scholarship |
| `concepts/` | Independent explanations of theories |
| `works/` | Bibliographic descriptions of primary works |
| `episode-observations/` | Observed scenes, blackboards and outstanding checks |
| `discussion-questions/` | Optional cross-episode questions |

`research/` holds source investigations and verification evidence—not competing canonical articles.

## Conventions

Files contain GitHub-flavored Markdown and small YAML front matter. Record IDs are stable lowercase slugs (episodes use `s01e01`, etc.). A record has `id`, `type`, `status` and, where plot might be discussed, `spoiler_limit`. Episode metadata also contains `season`, `episode`, `characters` and `concepts`. Link records by relative Markdown paths; use the slugs in front matter to support future scripts and agents.

Statuses: `draft`, `reviewed`, `verified`, `published`. An article may be well researched while an individual attribution remains **unverified**; never confuse status of the file and of a particular piece of evidence.

## Spoiler and evidence rules

**Maximum present viewing boundary: S01E10.** Earlier episode notes may discuss only events through that episode. The repository is public even outside `docs/`. Character articles contain only introductory knowledge; later developments belong in individually bounded episode files. Label explicit in-episode evidence, interpretive comparisons, and external historical context distinctly. No guessed timestamps or extended transcript reproductions.

Check Markdown links and metadata with `python scripts/check_notes.py`, and HTML separately with `python scripts/check_site.py`.
