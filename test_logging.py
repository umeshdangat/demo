from datetime import datetime
from logging_setup import setup_logging
import logging.handlers

def test():
	setup_logging()
	logger = logging.getLogger(__name__)
	logger.info('first log message')

def filename():
	#name = datetime.now().strftime("%y_%m_%d_%T_Log")
	return handlers.RotatingFileHandler('sample.log',maxBytes=20,backupCount=2,encoding='utf-8')
	#return logging.FileHandler('sample.log')