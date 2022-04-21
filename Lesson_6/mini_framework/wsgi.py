from pprint import pprint
import os
import sys

from urls import url_parcer, default_urls
from page_controller import page_controller

from variables import RESPONSE_200, RESPONSE_404, DefaultTemplatesPath
from request import RequestWSGI
from logger import LoggerWsgi

# Инициализация логгера
logger = LoggerWsgi()

class WsgiMiniFramework:
	""" WSGI server run. """

	def __init__(self, templates_path=DefaultTemplatesPath, urls=default_urls):
		self.templates_path = templates_path
		self.urls = urls

		# try:
		# 	self.view = urls.get('view')
		# 	print(urls)
		# 	print(self.view, '---' * 10, 'user_view')
		# except:
		# 	pass

	def __call__(self, environ, start_response):

		pprint(environ)
		logger.get_logger(message=f"METHOD: {environ['REQUEST_METHOD']}, URL: {environ['PATH_INFO']}")
		request = RequestWSGI(environ)
		print(request, '----- WSGI request -----')

		# request_method = environ['REQUEST_METHOD']
		request_method = request.method
		# отапрвляем 'PATH_INFO' на разбор для пполученя унифицированного URL вида: /about/ и
		# дополнительных параметров
		current_url, message_from_url = url_parcer(environ.get('PATH_INFO'))
		# Получаем HTML страницу соответствующую URL (далее реализуем еще запрос по Методу)
		page = None
		response_code = RESPONSE_200
		try:
			page, response_code = page_controller(current_url, request, self.templates_path, self.urls)
		except:
			pass
		print('PAGE: ', page)

		start_response(response_code, [('Content-Type', 'text/html; charset=utf-8')])
		print(start_response)

		return [bytes(page, encoding='utf-8')] if page \
			else [bytes(f'WSGI Framework Start Page \n <br> {environ}', encoding='utf-8')]
