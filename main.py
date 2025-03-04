"""
Main entry point for the Content-Scraper project.
This script initializes configuration, logging, and runs the scraper workflow.
"""

import logging
from config import settings, logging_config
from processors import text_cleaner
from scrapers import reddit_scraper
from storage import sql_database
logging_config.setup_logging()
logger = logging.getLogger(__name__)

def run_scrapers():
    logger.info("Starting scrapers...")

    reddit = reddit_scraper.RedditScraper()
    reddit_data = reddit.scrape()
    logger.info(f"Scraped {len(reddit_data)} posts from Reddit")

    all_data = reddit_data
    # Process the data using text_cleaner (a simple example)
    cleaned_data = [text_cleaner.clean_text(item) for item in all_data]

    for data in cleaned_data:
        print(data)
        # sql_database.save_data(data)

    logger.info("Scraping and processing complete.")


if __name__ == '__main__':
    run_scrapers()

