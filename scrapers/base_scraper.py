import logging

import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from config import settings

logger = logging.getLogger(__name__)

class BaseScraper:
    """
    A base class for web scraping that provides common functionality
    for different types of web scrapers.

    Key Design Principles:
    1. Provide common HTTP request methods
    2. Handle basic error scenarios
    3. Implement politeness in web scraping (rate limiting, user-agent)
    """

    def __init__(self):
        self.headers = {
            'User-Agent': settings.SETTINGS['scraper']['user_agent'],
            'Accept-Language': 'en-US,en;q=0.5'
        }
        self.timeout = settings.SETTINGS["scraper"]["timeout"]
        self.retry_strategy = Retry(
            total=settings.SETTINGS["scraper"]["retry_strategy"]["max_retries"],
            backoff_factor=settings.SETTINGS["scraper"]["retry_strategy"]["backoff_factor"],
            status_forcelist=settings.SETTINGS["scraper"]["retry_strategy"]["status_forcelist"]
        )
        self.session = requests.Session()
        self.session.mount('https://', HTTPAdapter(max_retries=self.retry_strategy))

    def fetch(self, url: str):
        """Fetch HTML content from a URL"""
        try:
            response = self.session.get(
                url,
                headers=self.headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.text

        except requests.RequestException as e:
            logger.error(f"Error fetching {url}: {str(e)}")
            return None

    def parse(self, html: str):
        """Parse HTML content using BeautifulSoup.
        To be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement the parse method.")

    def scrape(self):
        """General method to fetch and parse content.
        To be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement the scrape method.")