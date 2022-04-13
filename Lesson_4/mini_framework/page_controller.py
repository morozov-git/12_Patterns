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


def page_controller(current_url, request, templates_path=DefaultTemplatesPath,
					urls=default_urls) -> object:
	""" Function get URL, REQUEST_METHOD and return Page. """
	print(templates_path, '---- our Templates path -----')

	# # path = join(BASE_DIR, templates_path)
	# print(path)
	try:
		page = urls[current_url]
		page_path = page.get('path')
		page_name = page.get('name')
		page_template = page.get('template_name')
		context = None
		page_html = render_template(page_template, page_name=page_name, templates_path=templates_path, context=context)
		try:
			print('---------- try get view -------------')
			page_view = page.get('view')
			print(page_view, '--------- page_view ---------')
			page_view_run = page_view.run(page, templates_path, request)
			print(page_view_run, '--------- page_view.run ---------')
			return page_view_run, RESPONSE_200
		except:
			return page_html + 'page _ doesnt have view', RESPONSE_200
			# return 'page _doesnt have view', RESPONSE_200
	except KeyError:
		return render_template('page_not_found.html', page_name='page_not_found',
							   templates_path=templates_path), RESPONSE_404


def render_template(template_name, templates_path=DefaultTemplatesPath, *args, **kwargs):
	""" Загрузка HTML страницы из шаблонов и подстановка параметров. """

	print(template_name, templates_path, args, kwargs, '-----------render-----------')
	# Загружаем шаблоны
	env = Environment(
		loader=FileSystemLoader(templates_path),
		autoescape=select_autoescape(['html', 'xml'])
	)
	# Получаем итоговый шаблон
	template = env.get_template(template_name)
	print(template, '----------- template -- render-----------')
	# Возвращаем шаблон с подставленными полями
	# print(template.render(*args, **kwargs), '----------- template -- render 2222 -----------')
	return template.render(kwargs)


if __name__ == '__main__':
	# Пример
	context = {
		'page_name': 'Index - test __main__',
		'text': 'test text'
	}
	test_html = render_template(f'index.html', context=context)
	# test_html = render_template(f'index.html', page_name='Index', context=context)
	print(test_html, '-------------- test_html -------------')
	# test_page = page_controller('/')
	# print(test_page)
# test_wrong_page = page_controller('sfsdf')
# print(test_wrong_page)
# test_page = page_controller('/about/')
# print(test_page)
