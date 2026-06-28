from pathlib import Path
import os

# /Users/bmiller/Runestone/RunestoneServer/books/csawesome/published/csawesome/MixedFreeResponse/RandomStringChooserParsonsB.html
# becomes /ns/books/published/
def path_to_url(p):
    parts = p.split("blog")
    return "https://blog.runestone.academy/" + parts[-1].replace("/html/","")


home = os.environ["HOME"]

with open(Path(home, "Runestone/HomePage", "sitemap.xml"), "w") as sm:
    sm.write(
        """<?xml version="1.0" encoding="utf-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
    <url><loc>https://blog.runestone.academy</loc></url>
    <url><loc>https://blog.runestone.academy/index.html</loc></url>
"""
    )
    p = Path(home, "Runestone/HomePage/blog")
    for i in p.rglob("*.html"):
        if "build" in str(i) or "knowl" in str(i):
            continue
        elif "blog" in str(i):
            sm.write("<url><loc>" + path_to_url(str(i)) + "</loc></url>\n")
    sm.write("</urlset>")
