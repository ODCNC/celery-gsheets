from celery_gsheets.celery import app


def test_conf():
    assert app.conf.get('acks_late') == True
    assert app.conf.get('enable_utc') == False
    assert app.conf.get('timezone') == 'Asia/Seoul'


def test_worker_conf():
    assert app.conf.get('worker_concurrency') == 1
    assert app.conf.get('worker_pool') == 'solo'
    assert app.conf.get('worker_prefetch_multiplier') == 1
