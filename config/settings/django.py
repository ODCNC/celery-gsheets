import os
from pathlib import Path

import sentry_sdk
from decouple import config
from django.utils.translation import gettext_lazy as _
from kombu.serialization import register
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.redis import RedisIntegration

BASE_DIR = Path(__file__).resolve().parent.parent.parent


SECRET_KEY = config('SECRET_KEY', default='px5cul(5fy1qgi)udomu(46zv_s10(j&7edwk+2hln2ps-tjto')

ALLOWED_HOSTS = []

DEBUG = config('DEBUG', False)

# Application definition

INSTALLED_APPS = [
    'celery_gsheets',
]

MIDDLEWARE = [
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
]

LANGUAGE_CODE = 'ko-KR'

LANGUAGES = [
    ('ko', _('Korean')),
    ('ja', _('Japanese')),
]

LOCALE_PATHS = (os.path.join(BASE_DIR, 'config', 'locale'),)

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Cellery:

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


# Sentry.io

sentry_sdk.init(
    dsn=config('SENTRY_DSN'),
    integrations=[DjangoIntegration(), RedisIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True,
)
