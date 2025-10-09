"""Logging utilities for GymApp."""
import logging

LOGGER_NAME = "gymapp"


def get_logger(name: str | None = None) -> logging.Logger:
    """Return a configured logger instance."""
    logger_name = name or LOGGER_NAME
    logger = logging.getLogger(logger_name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger
