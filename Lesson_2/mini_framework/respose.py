from webob import Response
from mini_framework.variables import RESPONSE_200, RESPONSE_404


class ResponseWSGI:
	""" Класс Response. """

	def __init__(self, status_code=RESPONSE_200):
		self.response = Response()
		self.status_code = status_code
		self.headers = self.response.headers
		print(self.response, self.status_code, self.headers, '---- data from ResponseWSGI() ----')

	def __call__(self):
		return self.response
