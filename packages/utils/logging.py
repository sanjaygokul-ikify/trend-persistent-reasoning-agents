import logging

def configure_logging(level=logging.INFO):
    logging.basicConfig(level=level)
    return logging.getLogger(__name__)