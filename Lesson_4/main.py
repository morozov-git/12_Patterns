from mini_framework.wsgi import WsgiMiniFramework
from settings import templates_path, URLS

project = WsgiMiniFramework(templates_path, URLS)
