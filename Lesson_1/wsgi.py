from pprint import pprint
from variables import *
from urls import url_parcer
from page_controller import page_controller


def main(environ, start_response):
	""" WSGI server run. """

	pprint(environ)
	print('METHOD: ', environ['REQUEST_METHOD'], ', URL: ', environ['PATH_INFO'], sep='')
	# print(environ.get('PATH_INFO'))
	request_method = environ['REQUEST_METHOD']
	# отапрвляем 'PATH_INFO' на разбор для пполученя унифицированного URL вида: /about/ и
	# дополнительных параметров
	current_url, message_from_url = url_parcer(environ.get('PATH_INFO'))
	# Получаем HTML страницу соответствующую URL (далее реализуем еще по Методу)
	page, response_code = page_controller(current_url, request_method)
	print('PAGE: ', page)

	start_response(response_code, [('Content-Type', 'text/html')])
	print(start_response)

	return [bytes(page, encoding='utf-8')] if page \
		else [bytes(f'WSGI Framework Start Page \n <br> {environ}', encoding='utf-8')]


""" Упрощенный вариант page_controller(). """
# def page_controller(current_url, request_method='GET'):
# 	""" Function get URL, REQUEST_METHOD and return Page. """
#
# 	# print('page_controller() URL', '--', current_url)
# 	if current_url == '/':
# 		return [b'Hello world from a simple WSGI application!'
# 				b'  Index Page']
# 	elif current_url == '/about/':
# 		return [b'Hello world from a simple WSGI application!'
# 				b'  About Page']
# 	else:
# 		return [b'Hello world from a simple WSGI application! '
# 				 b'Page Not Found']
