from webob import Request


class RequestWSGI:
	""" Класс Request, раздбрает запрос и отдает объект Request. """

	def __init__(self, environ):
		request = Request(environ)
		self.method = request.method
		self.path = request.path
		self.query_string = request.query_string
		self.headers = request.headers
		print(self.method, self.path, self.query_string, self.headers, '---- data from RequestWSGI() ----')


