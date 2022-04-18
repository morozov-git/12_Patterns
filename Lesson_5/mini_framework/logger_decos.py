import inspect
import time
import sys
import os
import traceback


def logger_decos(func_to_log):
	def console_logger(*args, **kwargs):
		frame = inspect.stack()[1]
		module = inspect.getmodule(frame[0])
		module1 = inspect.stack()[1][3]
		func_name = traceback.format_stack()[0].strip().split()[-1]
		module_name = module.__name__
		file_name = module.__file__.split('/')[-1]
		current_time = time.strftime("%H.%M.%S", time.localtime())
		logging_message = f'\n\n debug _ {current_time} _ {module_name} _ {file_name}  _ {module1} _ {func_name} _ args: {args} _ kwargs: {kwargs}\n\n '
		print(logging_message)
		# print('---'*10, args, kwargs)
		res = func_to_log(*args, **kwargs)

		return res
	return console_logger



if __name__ == '__main__':

	@logger_decos
	def test_logger_decos(a, b, c):
		e = a+b+c
		print('test_logger_decos --- ', e)
		return e


	test = test_logger_decos(2, 3, 4)
	print(test)
