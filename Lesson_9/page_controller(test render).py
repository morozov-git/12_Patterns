from jinja2 import Environment, FileSystemLoader, select_autoescape
from mini_framework.urls import my_urls
from mini_framework.variables import RESPONSE_200, RESPONSE_404, DefaultTemplatePath


def page_controller(current_url, request_method='GET', template_path=DefaultTemplatePath) -> object:
	""" Function get URL, REQUEST_METHOD and return Page. """

	try:
		page = my_urls[current_url]
		page_path = page.get('path')
		page_name = page.get('name')
		page_template = page.get('template_name')
		page_html = render(page_template, page_name=page_name, template_path=template_path)
		return page_html, RESPONSE_200
	except KeyError:
		return render('page_not_found.html', page_name='page_not_found', template_path=template_path), RESPONSE_404


# # print('page_controller() URL', '--', current_url)
# if current_url == '/':
# 	return [b'Hello world from a simple WSGI application!'
# 			b'  Index Page']
# elif current_url == '/about/':
# 	return [b'Hello world from a simple WSGI application!'
# 			b'  About Page']
# else:
# 	return  # [b'Hello world from a simple WSGI application! '


def render(template_name, template_path=DefaultTemplatePath, **kwargs):
	""" Загрузка HTML страницы из шаблонов и подстановка параметров. """

	# Загружаем шаблоны
	env = Environment(
		loader=FileSystemLoader(template_path),
		autoescape=select_autoescape(['html', 'xml'])
	)
	# Получаем итоговый шаблон
	template = env.get_template(template_name)
	# Возвращаем шаблон с подставленными полями
	return template.render(**kwargs)


if __name__ == '__main__':
	# Пример
	test_html = render(f'contacts.html', page_name='Index')
	print(test_html)
	test_page = page_controller('/contacts')
	print(test_page)
	# test_wrong_page = page_controller('sfsdf')
	# print(test_wrong_page)
	# test_page = page_controller('/about/')
	# print(test_page)
