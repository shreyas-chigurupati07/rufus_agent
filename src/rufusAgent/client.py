import requests
import os

class RufusClient:
    def __init__(self, api_key=None, base_url="http://127.0.0.1:8000"):
        self.api_key = api_key or os.getenv("RUFUS_API_KEY")
        self.base_url = base_url

    def scrape(self, url, max_depth=2):
        """Send a scraping request to the Rufus API."""
        headers = {"x-api-key": self.api_key, "Content-Type": "application/json"}
        data = {"url": url, "max_depth": max_depth}
        response = requests.post(f"{self.base_url}/scrape/", json=data, headers=headers)

        if response.status_code == 200:
            return response.json()["data"]
        else:
            raise Exception(f"Error: {response.json()}")

# Example usage
if __name__ == "__main__":
    client = RufusClient(api_key="test123")
    website = input("Enter the website URL to scrape: ")  # Allow user input
    data = client.scrape(website)
    print(data)