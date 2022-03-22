import pytest

from decouple import config

@pytest.fixture(scope='session')
def celery_config():
    return {
        'broker_url': config('GSHEETS_BROKER_URL'),
        'result_backend': config('GSHEETS_RESULT_BACKEND'),
    }


@pytest.fixture(scope='session')
def celery_includes():
    return [
        'celery_gsheets.tasks',
    ]
