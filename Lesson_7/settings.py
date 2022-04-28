import sys
import os
from my_urls import my_urls

dir_path = os.path.dirname(os.path.realpath(__file__))

# URLS
URLS = my_urls

# TEMPLATES SETTINGS
TEMPLATES_FOLDER = 'Templates'
templates_path = os.path.join(sys.path[0], TEMPLATES_FOLDER)
