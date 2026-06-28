# Runestone Academy Blog

Source for <https://blog.runestone.academy>, built with [Hugo](https://gohugo.io/).
(Migrated from Tinkerer/Sphinx in 2026 — see `migrate.py` for the one-time RST→Markdown conversion.)

## Prerequisites

```bash
brew install hugo   # the extended edition (for Sass); v0.163+
```

## Writing

- **Blog posts** live under `content/posts/<year>/<mm-dd-slug>/index.md` as
  [leaf bundles](https://gohugo.io/content-management/page-bundles/): the Markdown
  file plus any images it references, side by side. Front matter:

  ```yaml
  ---
  title: "My Post Title"
  date: "2026-07-01"
  slug: "my_post_title"        # becomes /2026/07/01/my_post_title.html
  categories: ["Announce"]      # optional
  author: ["Guest Name"]        # optional; defaults to the site author
  ---
  ```

  Reference co-located images with an absolute bundle path, e.g.
  `![alt](/2026/07/01/my_post_title/diagram.png)` (uglyURLs put the page at
  `…/my_post_title.html` and its assets under `…/my_post_title/`).

- **Standalone pages** live under `content/pages/<slug>/index.md` and publish to
  `/pages/<slug>.html`. Add `redirect: "https://…"` to make a page an external redirect.

## Preview

```bash
hugo server      # http://localhost:1313
```

## Deploy

```bash
./deploy.sh      # hugo --minify, copy rss.xml→rss.html, rsync to bnmnetp
```

Hugo emits `sitemap.xml`, the RSS feed, and the client-side search index
(`/index.json`, used by `/search.html`) automatically.

## Layout / theme

- `layouts/` — templates (`_default/baseof.html`, `posts/single.html`,
  `pages/single.html`, `index.html`, taxonomy templates, `partials/` incl. the
  sidebar widgets and `postmeta`).
- `static/css/` — the ported theme CSS (`modern5.css` + base + `site.css`) and fonts.
- `static/_static/` — logos and shared images (preserves the old `/_static/…` URLs).
- `hugo.toml` — config. URLs are preserved from the old site (`uglyURLs`, date-based
  `permalinks`). Drop a GA4 id into `googleAnalytics` to re-enable analytics.
