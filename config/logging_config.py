import logging

from config import settings


def setup_logging():
    """Setup logging configuration based on settings."""
    logging_level = getattr(logging, settings.SETTINGS.get("logging", {}).get("level", "INFO"))

    logging.basicConfig(
        level=logging_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
