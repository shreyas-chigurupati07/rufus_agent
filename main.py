from src.rufusAgent.scraper import fetch_js_page
from src.rufusAgent.processor import DataProcessor
from src.rufusAgent.utils import fetch_with_retry
import logging

logging.basicConfig(level=logging.INFO)

def rufus_scrape(url, extract_type="faq"):
    """Main function to scrape, extract, and save data."""
    logging.info(f"Scraping website: {url}")

    # Fetch content (Try Playwright first, fallback to requests)
    html_content = fetch_js_page(url) or fetch_with_retry(url)
    if not html_content:
        logging.error("Failed to fetch website content.")
        return

    processor = DataProcessor(html_content)
    
    if extract_type == "faq":
        extracted_data = processor.extract_faqs()
    else:
        extracted_data = [{"message": "No valid extraction type specified"}]

    processor.save_to_json(extracted_data)
    processor.save_to_csv(extracted_data)

# Example Usage
if __name__ == "__main__":
    rufus_scrape("https://mitadmissions.org/help/faq/", extract_type="faq")
