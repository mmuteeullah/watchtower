FROM python:3.8-slim

RUN pip install fastapi uvicorn prometheus-client psutil

COPY app.py /app/app.py

WORKDIR /app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
