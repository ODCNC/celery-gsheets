from celery_gsheets.tasks import gs_write

def test_write(celery_session_worker):
    result = gs_write('오류', 'append_rows', ['test'])
    assert result.get()
