import pytest
from src.rufusAgent.scraper import RufusScraper

def test_scraper_init():
    """Test if the scraper initializes correctly."""
    scraper = RufusScraper("https://example.com")
    assert scraper.base_url == "https://example.com"
    assert isinstance(scraper.visited_urls, set)

def test_scraper_fetch():
    """Test if fetch_content retrieves valid HTML."""
    scraper = RufusScraper("https://example.com")
    content = scraper.fetch_content("https://www.wikipedia.org/")
    assert content is not None
    assert "<html" in content.lower()

def test_save_output(tmp_path):
    """Test if output is correctly saved as JSON."""
    scraper = RufusScraper("https://example.com")
    scraper.output_data = {"https://example.com": "Test Content"}
    filepath = tmp_path / "output.json"
    scraper.save_output(filepath)
    assert filepath.exists()