import requests

class Notification:
    def send_to_pagerduty(self, alert:Al):
        """
        Send an alert to PagerDuty

        Usage:
        send_to_pagerduty(alert)
        """
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


    def send_to_slack(self, message: str):
        """
        Send a message to a Slack channel #watchtower

        Usage:
        send_to_slack("Hello World")
        """
        webhook_url = "https://hooks.slack.com/services/YOUR_SLACK_WEBHOOK_URL"
        payload = {"text": message}
        requests.post(webhook_url, json=payload)