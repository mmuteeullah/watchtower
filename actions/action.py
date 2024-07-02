from actions.send_alerts_utils import send_slack_notification, call_pagerduty
from actions.docker_helper import kill_container_by_name

def take_action(alert):
    message = f"Warning Alert: {alert.labels.alertname} - {alert.annotations.summary}"
    send_slack_notification(message)

def take_critical_action(alert, set_pager_flag=False, kill_container_flag=False):
    message = f"Critical Alert: {alert.labels.alertname} - {alert.annotations.summary}"
    send_slack_notification(message)
    if set_pager_flag:
        # call_pagerduty(alert)
        send_slack_notification("PagerDuty incident created for critical alert")
    if kill_container_flag:
        kill_container_by_name(alert.labels.container)
        send_slack_notification(f"Container {alert.labels.container} killed successfully")
