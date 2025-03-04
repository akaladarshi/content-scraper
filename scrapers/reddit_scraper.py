import logging

from bs4 import BeautifulSoup

from config import settings
from scrapers.base_scraper import BaseScraper

logger = logging.getLogger(__name__)

class RedditScraper(BaseScraper):
    """Handles Reddit-specific scraping logic"""

    def scrape(self):
        url = settings.SETTINGS["scraper"]["reddit_url"]
        html = self.fetch(url)
        logger.info(f"Scraped {len(html)} posts from Reddit")
        if html:
            return self.parse(html)
        return []

    def parse(self, html_content: str):
        """Parse HTML content into structured data"""
        soup = BeautifulSoup(html_content, 'lxml')
        posts =[]

        try:
            post_elements = soup.find_all('div', {'data-testid': 'post-container'})
            for post in post_elements:
                post_data = {
                    'title': self._get_post_title(post),
                    'author': self._get_post_author(post),
                    'content': self._get_post_content(post),
                    'upvotes': self._get_post_upvotes(post),
                    'comments': self._get_comment_count(post),
                    'url': self._get_post_url(post)
                }
                posts.append(post_data)
        except Exception as e:
            logger.error(f"Error parsing Reddit posts: {e}")
        return posts

    def _get_post_title(self, post):
        title_element = post.find('h3', {'data-testid': 'post-title'})
        return title_element.text.strip() if title_element else ''

    def _get_post_content(self, post):
        content_element = post.find('div', {'data-testid': 'post-content'})
        return content_element.text.strip() if content_element else ''