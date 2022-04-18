import time
from mini_framework.request import RequestWSGI
from mini_framework.respose import ResponseWSGI
from mini_framework.variables import RESPONSE_200, RESPONSE_404
from mini_framework.page_controller import page_controller, render_template
from mini_framework.logger import LoggerWsgi
from mini_framework.logger_decos import Logger_decos

logger = LoggerWsgi()

@Logger_decos()
class Index:
	# print('---- my view ----')

	def run(self, page, path, request):
		print(page, path, request, '-------- Index.run() args --------')
		context = {
			'page_name': 'Index - my view',
			'text': 'test text'
		}
		# print(self, context, page, path, page['template_name'], '------------ my view ----------')
		html_render = render_template(templates_path=path, template_name=page['template_name'], context=context)
		logger.get_logger(message=f"{html_render}", file_log=False)
		# print(html_render, '------------ my view ----------')
		return html_render

@Logger_decos()
class About:

	def run(self, page, path, request):
		# print(page, path, '-------- About.run() args --------')
		context = {
			'page_name': 'About - my view',
			'text': 'test text'
		}
		# print(self, context, page, path, page['template_name'], '------------ my view ----------')
		html_render = render_template(templates_path=path, template_name=page['template_name'], context=context)
		# print(html_render, '------------ my view ----------')
		return html_render

@Logger_decos()
class Contacts:

	def run(self, page, path, request):
		self.context = {
			'page_name': 'Contact - my view',
			'text': 'test text',
			'message': None
		}

		logger.get_logger(message=f"{page, path, request}", file_log=False)
		try:
			if request.method == 'POST':
				Contacts.post_request(self, request)
		except:
			pass

		# print(self, context, page, path, page['template_name'], '------------ my view ----------')
		html_render = render_template(templates_path=path, template_name=page['template_name'], context=self.context)
		# print(html_render, '------------ my view ----------')
		return html_render

	def post_request(self, request):

		self.context.update({'message': 'Ваше сообщение успешно отправлено'})
		# print(request.wsgi_input_data)
		input_message = request.wsgi_input_data
		# print(input_message)
		logger.get_logger(message=f"{input_message}")
		current_time = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
		current_day = current_time[:-9:]
		with open(f'messages/{current_day}--messages.txt', 'a', encoding='utf-8') as messages_file:
			messages_file.write(f"{current_time} -- Message\n"
								f" 	Email: {''.join(input_message['email'])},\n"
								f" 	Title: {''.join(input_message['title'])},\n"
								f"	Text: {''.join(input_message['text'])}. \n")


if __name__ == '__main__':
	# test_view = Index()
	# print(test_view.run({'template_name': 'index.html'}, 'Templates', request=None))

	# test_view = Contacts()
	# print(test_view.run({'template_name': 'contacts.html'}, 'Templates'))

	a = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
	print(a)
	a = time.strftime("%Y-%m-%d--", time.localtime())
	print(a)
	# input_message = {'email': ['saS'], 'title': ['adsa'], 'text': ['ASDAS']}
	# current_day = time.strftime("%Y-%m-%d--", time.localtime())
	# current_time = time.strftime("%Y-%m-%d-%H.%M.%S -- ", time.localtime())
	# with open(f'messages/{current_day}messages.txt', 'a', encoding='utf-8') as messages_file:
	# 			messages_file.write(f"{current_time} Message\n"
	# 								f" Email: {''.join(input_message['email'])},\n"
	# 								f" Title: {''.join(input_message['title'])}, \n"
	# 								f" Text: {''.join(input_message['text'])}.\n")

	test_view_contacts = Contacts()
	print(test_view_contacts.run({'template_name': 'contacts.html'}, 'Templates', request=None))
