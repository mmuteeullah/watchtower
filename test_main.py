# test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_receive_alert_warning():
    alert = {
        "annotations": {
            "description": "Test alert description",
            "runbook_url": "http://example.com",
            "summary": "Test alert Passed"
        },
        "labels": {
            "alertname": "Testing",
            "cluster": "test-cluster",
            "container": "test-container",
            "endpoint": "http",
            "job": "test-job",
            "namespace": "test-namespace",
            "pod": "test-pod",
            "priority": "P1",
            "prometheus": "test-prometheus",
            "region": "us-west-2",
            "replica": "1",
            "service": "test-service",
            "severity": "WARNING"
        },
        "startsAt": "2024-07-02T07:31:57.339Z",
        "status": "firing"
    }
    response = client.post("/webhook", json=alert)
    assert response.status_code == 200
    assert "enriched_alert" in response.json()
    assert "action_result" in response.json()

def test_receive_alert_critical():
    alert = {
        "annotations": {
            "description": "Test alert description",
            "runbook_url": "http://example.com",
            "summary": "Test alert Passed"
        },
        "labels": {
            "alertname": "Testing",
            "cluster": "test-cluster",
            "container": "test-container",
            "endpoint": "http",
            "job": "test-job",
            "namespace": "test-namespace",
            "pod": "test-pod",
            "priority": "P1",
            "prometheus": "test-prometheus",
            "region": "us-west-2",
            "replica": "1",
            "service": "test-service",
            "severity": "CRITICAL"
        },
        "startsAt": "2024-07-02T07:31:57.339Z",
        "status": "firing"
    }
    response = client.post("/webhook", json=alert)
    assert response.status_code == 200
    assert "enriched_alert" in response.json()
    assert "action_result" in response.json()