from jinja2 import Environment, FileSystemLoader, select_autoescape
from os.path import join
import sys
import os
sys.path
# print(sys.path)
# dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)
# sys.path[0] = dir_path
# print(sys.path)

from urls import default_urls
from variables import RESPONSE_200, RESPONSE_404, DefaultTemplatesPath, BASE_DIR


def page_controller(current_url, request_method='GET', templates_path=DefaultTemplatesPath, urls=default_urls) -> object:
	""" Function get URL, REQUEST_METHOD and return Page. """
	print(templates_path, '---- our Templates path -----')

	# # path = join(BASE_DIR, templates_path)
	# print(path)
	try:
		page = urls[current_url]
		page_path = page.get('path')
		page_name = page.get('name')
		page_template = page.get('template_name')
		page_html = render(page_template, page_name=page_name, templates_path=templates_path) # page_html = render(page_template, page_name=page_name, template_path=template_path)
		return page_html, RESPONSE_200
	except KeyError:
		return render('page_not_found.html', page_name='page_not_found', templates_path=templates_path), RESPONSE_404




def render(template_name, templates_path=DefaultTemplatesPath, **kwargs):
	""" Загрузка HTML страницы из шаблонов и подстановка параметров. """

	# Загружаем шаблоны
	env = Environment(
		loader=FileSystemLoader(templates_path),
		autoescape=select_autoescape(['html', 'xml'])
	)
	# Получаем итоговый шаблон
	template = env.get_template(template_name)
	# Возвращаем шаблон с подставленными полями
	return template.render(**kwargs)


if __name__ == '__main__':
	# Пример
	test_html = render(f'index.html', page_name='Index')
	print(test_html)
	test_page = page_controller('/')
	print(test_page)
	# test_wrong_page = page_controller('sfsdf')
	# print(test_wrong_page)
	# test_page = page_controller('/about/')
	# print(test_page)
