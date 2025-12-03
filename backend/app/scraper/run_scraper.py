import os
import feedparser
from app.db.db import get_db
from datetime import datetime

RSS_URL = "https://www.bloomberg.com/feed/podcast/technology.xml"

def run_scraper_job():
    print("dev: rss scraper started")
    if os.getenv("FETCH_ENABLED", "false").lower() != "true":
        return

    feed = feedparser.parse(RSS_URL)
    conn = get_db()
    cur = conn.cursor()

    for entry in feed.entries[:5]:  # dev: first 5 articles for testing
        title = entry.title
        link = entry.link
        published_at = datetime(*entry.published_parsed[:6])
        category = "economy"  # dev: since RSS is economy-focused
        content = entry.summary

        # dev: skip if already in db
        cur.execute("SELECT 1 FROM news WHERE url=%s", (link,))
        if cur.fetchone():
            continue

        cur.execute(
            "INSERT INTO news (title, content, category, url, published_at) VALUES (%s,%s,%s,%s,%s)",
            (title, content, category, link, published_at)
        )
        print(f"dev: inserted -> {title[:30]}...")  # dev: short preview

    conn.commit()
    cur.close()
    conn.close()
