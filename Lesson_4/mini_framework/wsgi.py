from pprint import pprint
import os
import sys
# sys.path
# path = os.path.dirname(__file__)
# print(path)
# sys.path.append('./')
# sys.path.append('.../')
# sys.path.append(os.path.join(sys.path[0], '../'))
# print(sys.path)
# dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)
# sys.path[0] = dir_path
# print(sys.path)
# sys.path.insert(0, os.path.split(dir_path)[0])
from urls import url_parcer, default_urls
from page_controller import page_controller

from variables import RESPONSE_200, RESPONSE_404, DefaultTemplatesPath
from request import RequestWSGI


class WsgiMiniFramework:
	""" WSGI server run. """

	def __init__(self, templates_path=DefaultTemplatesPath, urls=default_urls):
		self.templates_path = templates_path
		self.urls = urls

	def __call__(self, environ, start_response):

		pprint(environ)
		print('METHOD: ', environ['REQUEST_METHOD'], ', URL: ', environ['PATH_INFO'], sep='')
		# print(environ.get('PATH_INFO'))

		request = RequestWSGI(environ)

		# request_method = environ['REQUEST_METHOD']
		request_method = request.method
		# отапрвляем 'PATH_INFO' на разбор для пполученя унифицированного URL вида: /about/ и
		# дополнительных параметров
		current_url, message_from_url = url_parcer(environ.get('PATH_INFO'))
		# Получаем HTML страницу соответствующую URL (далее реализуем еще запрос по Методу)
		page = None
		response_code = RESPONSE_200
		try:
			page, response_code = page_controller(current_url, request_method, self.templates_path, self.urls)
		except:
			pass
		print('PAGE: ', page)

		start_response(response_code, [('Content-Type', 'text/html; charset=utf-8')])
		print(start_response)

		return [bytes(page, encoding='utf-8')] if page \
			else [bytes(f'WSGI Framework Start Page \n <br> {environ}', encoding='utf-8')]
