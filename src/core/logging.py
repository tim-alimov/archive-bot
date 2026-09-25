import logging

from src.core.settings import settings


def setup_logging() -> None:
    log_level = settings.log_level if not settings.debug else "DEBUG"
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S%z"
    )
