import requests
from bs4 import BeautifulSoup

def scrape_static_page(url):
    """Simple web scraper for static pages."""
    try:
        response = requests.get(url, headers={"User-Agent": "RufusBot/1.0"})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text(strip=True)
    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        return None