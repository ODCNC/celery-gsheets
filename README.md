# Digital Commerce

A django-celery-beat package for gsheets

## Installation

Install using pip...

```shell
pip install git+https://github.com/ODCNC/celery-gsheets.git
```

Add configurations to `.env` file

```shell
GSHEETS_BROKER_URL="amqp://..."
GSHEETS_RESULT_BACKEND="redis://..."
SERVICE_ACCOUNT_FILE="<google_account_file_name>"
SPREADSHEET_TITLE="<spreadsheet_title>"
```

---

## Run via pm2

```shell
pm2 delete gsheets
pm2 startOrReload gsheets.json
pm2 log
```

---

## Contribution

Install command-line tools and update requirements

```shell
pip install pip-tools
pip-compile -o requirements.txt config/requirements.in
pip install -r config/requirements.txt
```
