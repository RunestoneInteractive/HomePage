#!/bin/bash
set -euo pipefail

# Build the static site with Hugo and publish it to the web server.
# (Replaces the old Tinkerer/Sphinx `tinker --build` + make_sitemap.py flow.)

# Build into ./public
hugo --minify --gc

# Tinkerer served the RSS feed at /rss.html; Hugo writes /rss.xml. Copy it so
# existing subscribers (who saved the rss.html URL) keep working.
cp public/rss.xml public/rss.html

# Publish. Hugo already emits sitemap.xml, so make_sitemap.py is no longer needed.
# (Add --delete to also purge stale Tinkerer files left on the server; omitted
#  here to match the original deploy and avoid removing anything unexpected.)
rsync -avz -e 'ssh -i /Users/bmiller/.ssh/id_rsa' public/ bnmnetp:/var/www/runestone/html/
