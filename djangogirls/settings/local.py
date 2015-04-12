from .base import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'), )

SECRET_KEY = '9y@eewrbp$tuk6^wfxkm4=t@_#6awnqjd-u59w8*wpwf2bc__v'

DEBUG = True

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
