## watchtower

**Table of Contents**

* Prerequisites
* Steps to Run the App
* Notes

## Prerequisites

Before running the application, you'll need the following:

* Docker
* Docker-compose
* Slack Webhook URL

## Steps to Run the App

1. **Running the Prometheus and Alertmanager Infra:**
    
    * First Create the docker network "watchtower-network":
    
     ```
     docker network create watchtower-network
     ```

     ```
     cd some_docker_stuff
     ```

     ```
     docker-compose up --build
     ```

2. **Running the App:**

    * Go back to the main directory 

     ```
     cd ..
     ```

     ```
     ./run.sh
     ```

     * The above run.sh script will build, test and deploy the project.

## Notes
- WatchTower App runs on port 80 [HealthCheck : curl "http://localhost"]
- A custom app is created to mimic high cpu behaviour.
- Call the below api to mimic high cpu for 600 sec. (Metrics can be seen on localhost:8000/metrics)

    ```bash
    curl -X POST "http://localhost:8000/trigger/high-cpu/?duration=600"
    ```

- For Warning Alert
    ```bash
    curl --location 'localhost/webhook' \
    --header 'Content-Type: application/json' \
    --data '{
        "annotations": {
            "description": "Test alert description",
            "runbook_url": "http://example.com",
            "summary": "WARNING ALERT FIRING"
        },
        "labels": {
            "alertname": "Prod Alert",
            "cluster": "test-cluster",
            "container": "some_docker_stuff-custom-app",
            "endpoint": "http",
            "job": "custom-app",
            "namespace": "test-namespace",
            "pod": "test-pod",
            "priority": "P1",
            "prometheus": "test-prometheus",
            "region": "us-west-2",
            "replica": "1",
            "service": "test-service",
            "severity": "WARNING"
        },
        "startsAt": "2025-07-02T07:31:57.339Z",
        "status": "firing"
    }'
    ```

- For Critical Alert
    ```bash
    curl --location 'localhost/webhook' \
    --header 'Content-Type: application/json' \
    --data '{
        "annotations": {
            "description": "Test alert description",
            "runbook_url": "http://example.com",
            "summary": "CRITICAL ALERT FIRIRNG"
        },
        "labels": {
            "alertname": "Prod Alert",
            "cluster": "test-cluster",
            "container": "31596233c820",
            "endpoint": "http",
            "job": "custom-app",
            "namespace": "test-namespace",
            "pod": "test-pod",
            "priority": "P1",
            "prometheus": "test-prometheus",
            "region": "us-west-1",
            "replica": "1",
            "service": "test-service",
            "severity": "CRITICAL"
        },
        "startsAt": "2025-07-02T07:31:57.339Z",
        "status": "firing"
    }'
    ```

- For Documentation related to API on Browser visit
    http://localhost/redoc OR http://localhost/docs

- Please change the url for slack in /actions/send_alerts_utils.py

- Please watch the video before testing.

## Flow 

### Alert Type ==> Warning

![Warning FLow](/assets/warning.png "Warning Flow")

### Alert Type ==> Critical

![Critical Flow](/assets/critical.png "Critical Flow")