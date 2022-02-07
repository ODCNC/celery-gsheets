from config.settings.django import *
from kombu import Exchange, Queue


def queue(project_name):
    return Queue(project_name, Exchange(project_name), routing_key=project_name)

INSTALLED_APPS += [
    'django_celery_beat',
]


# Celery

CELERY_ACKS_LATE = True
CELERY_ENABLE_UTC = False
CELERY_IMPORTS = ("celery_gsheets.tasks", )
CELERYD_PREFETCH_MULTIPLIER = 1
CELERY_TIMEZONE = 'Asia/Seoul'
CELERY_QUEUES = [
    config('CELERY_PROJECT_NAME', cast=queue, default='gsheets'),
]

# Celery Gsheets

GSHEETS_BROKER_URL = config('GSHEETS_BROKER_URL')
GSHEETS_RESULT_BACKEND = config('GSHEETS_RESULT_BACKEND', 'redis://localhost:6379/0')
