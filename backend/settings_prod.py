from backend.settings import *

import dj_database_url

DATABASES['default'] =  dj_database_url.config()

DEBUG = False
TEMPLATE_DEBUG = False
