import inspect
import time
import sys
import os
from variables import LOGGER_ON, DefaultLoggingPath, Conosole_Log, File_Log

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)


class LoggerWsgi:

	def __init__(self):
		self.logger_on = LOGGER_ON
		self.log_path = DefaultLoggingPath
		frame = inspect.stack()[1]
		module = inspect.getmodule(frame[0])
		self.module_name = module.__name__
		self.file_name = module.__file__.split('/')[-1]
		self.current_time = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
		self.current_day = self.current_time[:-9:]

	def get_logger(self, message=None, logging_level='DEBUG', console_log=Conosole_Log, file_log=File_Log):

		self.message = message
		self.logging_level = logging_level
		self.console_log = console_log
		self.file_log = file_log

		logging_message = f'{self.current_time}, ' \
						  f'{self.logging_level}, ' \
						  f'{self.file_name}, ' \
						  f'{self.module_name}, ' \
						  f'{self.message}\n'
		if self.logger_on:
			if self.console_log:
				print(logging_message)
			if self.file_log:
				self.file_save(logging_message)
		else:
			print('Logger_WSGI is OFF')

	def file_save(self, logging_message):
		try:
			with open(f'Logging/{self.current_day}-{self.logging_level}-logger.txt', 'a', encoding='utf-8') as log_file:
				log_file.write(logging_message)
		except:
			print(f'Logger_WSGI can not write to file: {self.current_day}-logger.txt')


if __name__ == '__main__':
	logger = LoggerWsgi()
	logger.get_logger(message='test logger', logging_level='info', console_log=False)
	logger.get_logger(message='test debug logger', logging_level='debug')
	print(logger.module_name)
	print(logger.file_name)
