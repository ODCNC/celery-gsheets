#!/bin/env python
from celery_gsheets.celery import app

if __name__ == "__main__":
    app.worker_main(['worker', '-l', 'info', '-B'])
