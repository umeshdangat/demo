from logging.handlers import RotatingFileHandler
from datetime import datetime
import os

def test(maxBytes,backupCount,encoding):
	pid = os.getpid()
	filename = datetime.now().strftime('%y_%m_%d_%T.%f_'+ str(pid)) + '_analysis.log'
	return RotatingFileHandler(filename,maxBytes=maxBytes,backupCount=backupCount,encoding=encoding)

	
	
