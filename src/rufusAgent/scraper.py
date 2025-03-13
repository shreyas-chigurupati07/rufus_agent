import requests
from bs4 import BeautifulSoup
import json
import os
import time
import sys
from urllib.parse import urljoin

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from src.rufusAgent.utils import clean_text

class RufusScraper:
    def __init__(self, base_url, max_depth=2):
        self.base_url = base_url
        self.visited_urls = set()
        self.max_depth = max_depth
        self.output_data = {}

    def fetch_content(self, url):
        """Fetch content from a URL with error handling."""
        try:
            headers = {"User-Agent": "RufusBot/1.0"}
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def parse_page(self, url, depth=0):
        """Recursively parse a webpage and extract relevant data."""
        if depth > self.max_depth or url in self.visited_urls:
            return
        
        self.visited_urls.add(url)
        html_content = self.fetch_content(url)
        if not html_content:
            return
        
        soup = BeautifulSoup(html_content, "html.parser")
        
        text = clean_text(soup.get_text(strip=True))
        
        self.output_data[url] = text[:5000]  # Store only relevant text, truncating long pages

        for link in soup.find_all("a", href=True):
            next_url = urljoin(url, link["href"])
            if self.base_url in next_url:
                self.parse_page(next_url, depth + 1)
                
    def run(self):
        """Start the scraping process."""
        print(f"Starting crawl for {self.base_url}")
        self.parse_page(self.base_url)
        return self.output_data

    def save_output(self, output_path="data/rufusAgent/output.json"):
        """Save extracted data to a JSON file."""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(self.output_data, f, indent=4)

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    scraper = RufusScraper(url)
    scraped_data = scraper.run()
    scraper.save_output()
    print(f"Scraping complete! Data saved to data/rufusAgent/output.json")