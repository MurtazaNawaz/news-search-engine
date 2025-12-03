from fastapi import APIRouter
from app.db.db import get_db

router = APIRouter()

@router.get("/news/latest")
def get_latest_news():
    # dev: get few latest itms
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, title, category, published_at FROM news ORDER BY published_at DESC LIMIT 10")
    rows = cur.fetchall()
    conn.close()

    data = []
    for r in rows:
        data.append({
            "id": r[0],
            "title": r[1],
            "category": r[2],
            "published_at": r[3]
        })
    return {"items": data}


@router.get("/search")
def search_news(q: str):
    # dev: very basic like search
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, title, category FROM news WHERE content ILIKE %s LIMIT 20", (f"%{q}%",))
    rows = cur.fetchall()
    conn.close()

    data = []
    for r in rows:
        data.append({
            "id": r[0],
            "title": r[1],
            "category": r[2]
        })
    return {"items": data}
