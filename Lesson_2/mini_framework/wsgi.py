from pprint import pprint
from mini_framework.urls import url_parcer
from mini_framework.page_controller import page_controller
from mini_framework.variables import RESPONSE_200, RESPONSE_404
from mini_framework.request import RequestWSGI
from mini_framework.respose import ResponseWSGI


class WsgiMiniFramework:
	""" WSGI server run. """

	def __call__(self, environ, start_response):

		pprint(environ)
		print('METHOD: ', environ['REQUEST_METHOD'], ', URL: ', environ['PATH_INFO'], sep='')
		# print(environ.get('PATH_INFO'))

		request_wsgi = RequestWSGI(environ)
		response_wsgi = ResponseWSGI()
		# request_method = environ['REQUEST_METHOD']
		request_method = request_wsgi.method
		# отапрвляем 'PATH_INFO' на разбор для пполученя унифицированного URL вида: /about/ и
		# дополнительных параметров
		current_url, message_from_url = url_parcer(environ.get('PATH_INFO'))
		# Получаем HTML страницу соответствующую URL (далее реализуем еще запрос по Методу)
		page = None
		# response_code = RESPONSE_200
		try:
			page, response_code = page_controller(current_url, request_method)
		except:
			pass
		print(response_wsgi.status_code)
		print('response_wsgi.body: ', response_wsgi.body, 'response_wsgi.headers: ', response_wsgi.headers)
		print('PAGE: ', page)

		# start_response(response_code, [('Content-Type', 'text/html; charset=utf-8')])
		start_response(response_wsgi.status_code, response_wsgi.headers)
		# print(start_response)

		return [bytes(page, encoding='utf-8')] if page \
			else [bytes(f'WSGI Framework Start Page \n <br> {environ}', encoding='utf-8')]

