FROM python:3.8-slim

RUN pip install flask

COPY webhook_receiver.py /app/webhook_receiver.py

WORKDIR /app

CMD ["python", "webhook_receiver.py"]
