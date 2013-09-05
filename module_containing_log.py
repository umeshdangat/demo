import logging_setup
import logging 
from logging_setup import setup_logging

def test_log():
	setup_logging()
	logger = logging.getLogger(__name__)
	logger.info('Hello message')