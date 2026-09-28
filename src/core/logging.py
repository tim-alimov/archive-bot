import logging


def setup_logging(log_level, debug: bool = False) -> None:
    log_level = log_level if not debug else "DEBUG"
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S%z",
    )
