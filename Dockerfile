FROM python:3.8-slim-buster
COPY . /usr/share/gsheets
WORKDIR /usr/share/gsheets
RUN python3 -m pip install -r requirements.txt
ENTRYPOINT python3 gsheets.py
