# Contributing

The companion should support rigorous discussion of moral philosophy **without spoiling subsequent episodes**.

## Workflow

1. Begin with a canonical `notes/episodes/season-XX/sXXeYY.md` record using `templates/episode-template.md`, with a strict viewing boundary. Put blackboard and scene observations separately in `notes/episode-observations/`.
2. Summarize only events occurring through that episode.
3. Classify every philosophical connection:
   - **Explicit reference:** truly named or shown; record episode evidence and a timestamp if feasible.
   - **Interpretive connection:** editorial reading that does not claim the writers' intent.
   - **External context:** independently sourced philosophical, historical, or production background.
4. Prefer primary philosophical texts and academic reference works. Record relevant sections, editions, and translations.
5. Write original prose; avoid extensive transcript quotation or unlicensed images.
6. Maintain characters, philosophers, concepts and works as linked canonical `notes/` records; keep source investigations in `research/`, not in duplicate records. Publish to `docs/` only after review and update navigation without leaking later content.
7. Run `python scripts/check_notes.py` and `python scripts/check_site.py`, then check semantics, keyboard navigation, mobile layout, source links, and episode boundaries.

## Spoilers

Future-episode developments are prohibited on earlier pages, including collapsed content, title tags, filenames, alt text, metadata, labels, and page previews. Later retrospective essays, if written, must have separate clearly labeled viewing boundaries.

The maintainer has not completed the final season. Do not introduce whole-series spoilers into issue titles, pull request summaries, research files, or public proposals.

## Repository practices

Keep `docs/` standalone static HTML/CSS, with relative links suitable for GitHub Pages under a project path. Mark outlines as unfinished. Run `python scripts/check_site.py` before proposing changes. Research outside `docs/` remains public on GitHub.

No code or content license is declared at this point; do not assume unlicensed material can be reused elsewhere.
