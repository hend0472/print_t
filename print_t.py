import datetime
import time
import re
import logging
import os
import sys
from colorama import init
init()
# FOR WHATEVER REASON, COMPUTER UPDATED AND THIS STOPPED WORKING WITHOUT COLORAMA INIT

def start_logging(file_name):
	if os.path.isfile(file_name):
		os.remove(file_name)
	logging.basicConfig(level=logging.INFO, filename=file_name, filemode='a+',
						format='%(asctime)-15s %(levelname) -8s %(message)s')
	logging.getLogger('requests').setLevel(logging.WARNING)
	logging.getLogger('urllib3').setLevel(logging.WARNING)
	logging.info(str(file_name) + ' LOGGING STARTED')


class bcolors:
	"""Sets color codes for text printing"""
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	FAILRED = '\u001b[31;1m'
	WARNING = '\033[93m'
	WHITET = '\033[97m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	REDBACK = "\033[41m"
	GREENBACK = '\033[42m'
	YELLOWT = '\033[33m'


def print_t(message, type_m='none'):
	"""Just an improvement on regular print, makes it easier to track what's going on with color and timestamp"""
	# message = re.sub(' +',' ', str(message))
	if str(type_m).lower() == 'hard fail':
		print('[' + str(datetime.datetime.now()) + '] ' + bcolors.REDBACK + bcolors.YELLOWT + str(message).rstrip() +
			bcolors.ENDC)
		logging.critical(message)
	elif str(type_m).lower() == 'hard pass':
		print('[' + str(datetime.datetime.now()) + '] ' + bcolors.GREENBACK + bcolors.WHITET + str(message).rstrip() +
			bcolors.ENDC)
		logging.info(message)
	elif str(type_m).lower() == 'pass':
		print('[' + str(datetime.datetime.now()) + '] ' + bcolors.OKGREEN + str(message).rstrip() + bcolors.ENDC)
		logging.info(message)
	elif str(type_m).lower() == 'blue':
		print('[' + str(datetime.datetime.now()) + '] ' + bcolors.OKBLUE + str(message).rstrip() + bcolors.ENDC)
		logging.info(message)
	elif str(type_m).lower() == 'warn':
		print('[' + str(datetime.datetime.now()) + '] ' + bcolors.WARNING + str(message).rstrip() + bcolors.ENDC)
		logging.warn(message)
	elif str(type_m).lower() == 'none':
		print('[' + str(datetime.datetime.now()) + '] ' + str(message).rstrip())
		logging.info(message)
	elif str(type_m).lower() == 'fail':
		print('[' + str(datetime.datetime.now()) + '] ' + bcolors.FAILRED + str(message).rstrip() + bcolors.ENDC)
		logging.error(message)

