import inspect
import time
import sys
import os
from variables import LOGGER_ON, DefaultLoggingPath, Conosole_Log, File_Log
import logging

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)



class Logger_Wsgi:

	def __init__(self, message='message', logging_level='debug'):
		self.message = message
		self.logging_level = logging_level
		self.logger_on = LOGGER_ON
		self.console_log = Conosole_Log
		self.file_log = File_Log
		self.log_path = DefaultLoggingPath
		frame = inspect.stack()[1]
		module = inspect.getmodule(frame[0])
		self.module_name = module.__name__
		self.file_name = module.__file__.split('/')[-1]
		self.current_time = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
		self.current_day = self.current_time[:-9:]

	def get_logger(self):
		logging_meesage = f'test'
		pass




# current_day = time.strftime("%Y-%m-%d--", time.localtime())
# current_time = time.strftime("%Y-%m-%d-%H.%M.%S -- ", time.localtime())
# with open(f'Logging/{current_day}logger.txt', 'a', encoding='utf-8') as log_file:
# 	log_file.write(f"{current_time} Message\n"
# 						f" 	Email: {''.join(input_message['email'])},\n"
# 						f" 	Title: {''.join(input_message['title'])},\n"
# 						f"	Text: {''.join(input_message['text'])}. \n")


if __name__ == '__main__':

	logger = Logger_Wsgi()
	print(logger.current_time, logger.current_day, logger.filename, logger.module)
	print(logger.module)
	print(logger.filename)