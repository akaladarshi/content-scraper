"""
Configuration settings for Content-Scraper.
You can modify these values or load them from an external YAML file.
"""

# Example settings for web scraping and storage
SETTINGS = {
    "scraper": {
        "user_agent": "ContentScraperBot/1.0",
        "timeout": 10,
        "reddit_url": "https://www.reddit.com/r/interview/",
        "medium_url": "https://medium.com/tag/interview-preparation",
        "leetcode_url": "https://leetcode.com/problemset/all/",
        "retry_strategy": {
            "max_retries": 3,
            "backoff_factor": 0.5,
            "status_forcelist": [429, 500, 502, 503, 504]
        }
    },
    "database": {
        "connection_string": "sqlite:///content_scraper.db"  # Using SQLite for simplicity
    },
    "logging": {
        "level": "INFO"
    }
}
