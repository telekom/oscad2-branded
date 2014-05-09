import os
from pyramid.paster import get_app, setup_logging

conf_file = os.path.join(os.path.dirname(__file__), 'telekom.ini')

setup_logging(conf_file)
application = get_app(conf_file)
