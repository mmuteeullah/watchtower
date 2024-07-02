import requests

def call_pagerduty(alert):
    pagerduty_url = "https://api.pagerduty.com/incidents"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_PAGERDUTY_API_KEY"
    }
    payload = {
        "incident": {
            "title": "Critical Incident",
            "description": alert.annotations.summary        }
    }
    response = requests.post(pagerduty_url, headers=headers, json=payload)
    if response.status_code == 201:
        print("PagerDuty incident created successfully")
    else:
        print("Failed to create PagerDuty incident")


def send_slack_notification(message: str):
    webhook_url = "https://hooks.slack.com/services/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"
    payload = {"text": message}
    requests.post(webhook_url, json=payload)