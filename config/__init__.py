import os


# app
ROOT = os.path.abspath('..')
API_TOKEN = os.environ.get('API_TOKEN')

# logger
LOG_LVL = 10
LOG_FMT = '[%(asctime)s] @%(name)s  %(levelname)s in %(module)s: %(message)s'
