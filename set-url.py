#!/usr/bin/env python3
"""Put your real address into the site's metadata.

Run it once, after you know your GitHub Pages address (or your own domain):

    python3 set-url.py https://YOUR-USERNAME.github.io/reem-portfolio
    python3 set-url.py https://reemalkhalaileh.com

It rewrites index.html, robots.txt and sitemap.xml in this folder.
Safe to run again later with a different address.
"""
import re
import sys
from pathlib import Path

FILES = ("index.html", "robots.txt", "sitemap.xml")
PATTERN = re.compile(r"https://(?:YOUR-DOMAIN|[A-Za-z0-9.-]+\.github\.io(?:/[A-Za-z0-9._-]+)?|[A-Za-z0-9-]+\.[A-Za-z]{2,}(?:\.[A-Za-z]{2,})?)(?=[/\"'>\s])")


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    url = sys.argv[1].rstrip("/")
    if not url.startswith("https://"):
        print("The address must start with https://")
        return 1

    here = Path(__file__).resolve().parent
    for name in FILES:
        path = here / name
        if not path.exists():
            print(f"  skipped {name} (not found)")
            continue
        text = path.read_text(encoding="utf-8")
        new_text, count = PATTERN.subn(url, text)
        if count:
            path.write_text(new_text, encoding="utf-8")
        print(f"  {name}: {count} address{'es' if count != 1 else ''} updated")

    print(f"\nDone. The site now points at {url}")
    print("Upload the changed files to your repository, and the link preview will use the real address.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
