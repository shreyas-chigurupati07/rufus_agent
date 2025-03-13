import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from rufusAgent.scraper import RufusScraper

app = FastAPI()

# Dummy API Key for testing (Store in ENV in production)
API_KEY = os.getenv("RUFUS_API_KEY", "test123")

class ScrapeRequest(BaseModel):
    url: str
    max_depth: int = 2

@app.post("/scrape/")
async def scrape(request: ScrapeRequest, x_api_key: str = Header(None)):
    """Secure API Endpoint to scrape a website with API Key authentication."""
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    scraper = RufusScraper(request.url, request.max_depth)
    data = scraper.run()
    scraper.save_output()
    return {"status": "success", "data": data}