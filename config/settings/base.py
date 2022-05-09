from decouple import config
from kombu import Exchange, Queue


def queue(project_name):
    return Queue(project_name, Exchange(project_name), routing_key=project_name)


# Celery

gsheets_acks_late = True
gsheets_enable_utc = False
gsheets_timezone = 'Asia/Seoul'
gsheets_task_queues = [
    config('GSHEETS_PROJECT_NAME', cast=queue, default='gsheets'),
]

gsheets_worker_concurrency = config('GSHEETS_WORKER_CONCURRENCY', 1)
gsheets_worker_pool = 'solo'
gsheets_worker_prefetch_multiplier = 1

# Celery Gsheets

gsheets_broker_url = config('GSHEETS_BROKER_URL')
gsheets_result_backend = config('GSHEETS_RESULT_BACKEND', 'redis://localhost:6379/0')
