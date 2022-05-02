import ast
import json
from urllib.parse import parse_qs

from webob import Request


class RequestWSGI:
	""" Класс Request, раздирает запрос и отдает объект Request. """

	def __init__(self, environ):
		request = Request(environ)
		self.method = request.method
		self.path = request.path
		self.query_string = request.query_string
		self.headers = request.headers
		self.content_length = request.content_length
		request_wsgi_data = environ['wsgi.input'].read(self.content_length)
		self.wsgi_input_data = parse_qs(request_wsgi_data.decode(encoding="UTF-8"))
		print(self.wsgi_input_data, '---------------- self.wsgi_input_data -----------')
		# print(request.body, '---------------- request.body -----------')
		print(self.method, self.path, self.query_string, self.headers, '---- data from RequestWSGI() ----')

	def __call__(self):
		return self
