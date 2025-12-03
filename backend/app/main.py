from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from app.api.routes import router
from app.scraper.run_scraper import run_scraper_job
import os

app = FastAPI()

# dev: add api routes
app.include_router(router)

# dev: simple background job
scheduler = BackgroundScheduler()
interval_minutes = int(os.getenv("SCRAPE_INTERVAL_MINUTES", 5))
scheduler.add_job(run_scraper_job, "interval", minutes=interval_minutes)
scheduler.start()

@app.on_event("startup")
def startup_event():
    # dev: run once at startup
    run_scraper_job()

@app.get("/")
def home():
    return {"msg": "backend running"}
