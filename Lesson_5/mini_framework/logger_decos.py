import inspect
import time
import sys
import os
import traceback


class Logger_decos:

	def __call__(self, *args, **kwargs):
		def console_logger(*args, **kwargs):
			frame = inspect.stack()[1]
			module = inspect.getmodule(frame[0])
			module1 = inspect.stack()[1][3]
			func_name = traceback.format_stack()[0].strip().split()[-1]
			module_name = module.__name__
			file_name = module.__file__.split('/')[-1]
			current_time = time.strftime("%H.%M.%S", time.localtime())
			logging_message = f'debud _ {module_name} _ {file_name} _ {current_time} _ {module1} _ {func_name}'
			print(logging_message)
		return console_logger

if __name__ == '__main__':
	@Logger_decos()
	def test_logger_decos():
		return 'test_logger_decos'

	test = test_logger_decos()
	# print(test)
