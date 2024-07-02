# models.py
from pydantic import BaseModel
from typing import Dict, Any

class AlertAnnotations(BaseModel):
    description: str
    runbook_url: str
    summary: str

class AlertLabels(BaseModel):
    alertname: str
    cluster: str
    container: str
    endpoint: str
    job: str
    namespace: str
    pod: str
    priority: str
    prometheus: str
    region: str
    replica: str
    service: str
    severity: str

class Alert(BaseModel):
    annotations: AlertAnnotations
    labels: AlertLabels
    startsAt: str
    status: str