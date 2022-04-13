from decouple import config
from kombu import Exchange, Queue


def queue(project_name):
    return Queue(project_name, Exchange(project_name), routing_key=project_name)


# Celery

GSHEETS_ACKS_LATE = True
GSHEETS_ENABLE_UTC = False
CELERYD_PREFETCH_MULTIPLIER = 1
GSHEETS_TIMEZONE = 'Asia/Seoul'
GSHEETS_QUEUES = [
    config('GSHEETS_PROJECT_NAME', cast=queue, default='gsheets'),
]

# Celery Gsheets

GSHEETS_BROKER_URL = config('GSHEETS_BROKER_URL')
GSHEETS_RESULT_BACKEND = config('GSHEETS_RESULT_BACKEND', 'redis://localhost:6379/0')
