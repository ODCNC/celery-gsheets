import os

from decouple import config

from celery import Celery

# set the default Django settings module for the 'celery' program.
settings_module = config('DJANGO_SETTINGS_MODULE', default='config.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

app = Celery('gsheets')

# Using a string here means the worker doesn't have to serialize
app.config_from_object('django.conf:settings', namespace='GSHEETS')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
