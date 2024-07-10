import requests

class Notification:
    def send_to_pagerduty(self, alert):
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

    def slack_url(self, critical: bool = False):
        """
        Get the Slack webhook URL

        Usage:
        slack_url()
        """
        if critical:
            return "https://hooks.slack.com/services/some_critical_webhook_url"
        else:
            return "https://hooks.slack.com/services/some_webhook_url"

    def send_to_slack(self, message: str, critical: bool = False):
        """
        Send a message to a Slack channel #watchtower

        Usage:
        send_to_slack("Hello World")
        """
        webhook_url = self.slack_url(critical)
        payload = {"text": message}
        requests.post(webhook_url, json=payload)