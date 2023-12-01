FROM python:3.11.6-alpine3.18
WORKDIR /app
ADD main.py .
ADD requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT [ "gunicorn", "-w", "4","-b", "0.0.0.0", "main:app" ]