# The Good Place Companion

An independent, unofficial, spoiler-conscious companion to *The Good Place*, combining original episode recaps, moral philosophy, scholarly references, trivia, and discussion questions.

- **Repository:** https://github.com/ValRCS/the-good-place-companion
- **Intended website:** https://valrcs.github.io/the-good-place-companion/

**Status (2026-11-23):** Season 1 episodes 1–6 have complete public HTML companion articles; episodes 7–9 have canonical research notes only. Seasons 2–4 remain spoiler-free placeholders. GitHub Pages deployment must still be checked separately from the source files.

## The essential rule

An episode page must not reveal anything after its stated episode boundary—not in its recap, metadata, images, hidden content, link names, or navigation. The companion is designed for both a first-time viewer and a returning viewer who has not completed the final season.

## Layout

| Path | Role |
| --- | --- |
| `docs/` | GitHub Pages-ready public static site (HTML/CSS) |
| `docs/seasons/` | Season indexes and episode-by-episode notes |
| `docs/philosophy/` | Standalone spoiler-neutral philosophical reading library |
| `docs/trivia/` | Source-checked cultural, visual, and production notes |
| `docs/guide/` | Spoiler policy and editorial standards |
| `research/` | Source bibliography, investigations, and verification, not duplicate canonical articles |
| `notes/` | Canonical Markdown: episodes, characters, philosophers, concepts, works, observations |
| `templates/` | Reusable Markdown authoring templates |
| `scripts/check_site.py` | Static HTML internal-link and basic accessibility checks |

**Important:** Only `docs/` is served by GitHub Pages, but files elsewhere in this *public repository are still publicly accessible on GitHub*. Do not store private notes or future-season spoilers here.

## Preview

No Node.js, framework, or build step is required:

```bash
python -m http.server 8000 --directory docs
```

Open http://localhost:8000/ to preview. All internal links are relative, so pages work at the project URL.

Run the checker:

```bash
python scripts/check_site.py
```

## Enable GitHub Pages

Go to repository **Settings → Pages → Build and deployment**, select **Deploy from a branch**, then choose branch `main` and folder `/docs`. Save the settings and use GitHub's Pages status to confirm deployment. The code commit alone does not enable deployment.

## Add an episode

1. Draft the canonical Markdown record under `notes/episodes/season-XX/` using `templates/episode-template.md`; keep scene evidence separately in `notes/episode-observations/`.
2. Verify explicit names, quotations, and references in the episode; distinguish these from editorial interpretations.
3. Once the notes have been reviewed and reference uncertainties explicitly identified, add the edited HTML page to `docs/seasons/season-XX/episode-YY.html`.
4. Add a spoiler-neutral link to the season index without exposing later episode details.
5. Run `python scripts/check_notes.py` and `python scripts/check_site.py`; review each page's spoiler boundary and scholarly sources.

See [CONTRIBUTING.md](CONTRIBUTING.md), [spoiler policy](docs/guide/spoilers.html), and [editorial standards](docs/guide/editorial.html).

## Independence and rights

This is an unofficial educational and critical-commentary project. *The Good Place* and related marks and characters belong to their respective rights holders. Prefer original summaries and analysis to reproduced dialogue or images. No blanket reuse license for the repository has yet been selected.

## First nine episodes: research corpus

Start with the [Markdown notes index](notes/INDEX.md) or [Season 1 episode index](notes/episodes/season-01/README.md). The notes are the canonical research source; the GitHub Pages site remains a separate curated publication. **Maximum current narrative boundary in research notes: S01E09.** Published HTML episode companions extend through **S01E06** only; episode notes E07–E09 remain research notes on the public repository. Some scene-level timestamps and on-screen reference details for S01E01–S01E06 still await direct verification.
