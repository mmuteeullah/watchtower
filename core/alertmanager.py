from fastapi import HTTPException
from models import Alert, SeverityType
from helper_utils import Prometheus
from helper_utils import Notification
from helper_utils import kill_container_by_name

class Config():
    """ 
    Config class to set the CPU usage threshold
        Usage: config = Config(cpu_usage=90.0)
    """
    cpu_usage_threshold = 80.0
    def __init__(self, cpu_usage_threshold: float):
        self.cpu_usage = cpu_usage_threshold


class AlertManager():
    def __init__(self, alert: Alert):
          self.alert = alert
          self.set_pager_flag = False
          self.kill_container_flag = False

    def check_cpu_usage(self):
        notification_service = Notification()
        try:
            prometheus = Prometheus()
            cpu_usage = float(prometheus.get_cpu_usage(self.alert.labels.job))
            if cpu_usage > Config.cpu_usage_threshold:
                notification_service.send_to_slack(f"CPU usage is {cpu_usage} which is above the threshold")
                self.set_pager_flag = True
                self.kill_container_flag = True
        except Exception as e:
            print(f"Failed to fetch CPU usage: {e}")

    def enrich(self):
        self.check_cpu_usage()
        # self.check_memory()
        # self.check_somethine_else()
        return self

    def notify_warning(self):
        notification_service = Notification()
        message = f"Warning Alert: {self.alert.labels.alertname} - {self.alert.annotations.summary}"
        notification_service.send_to_slack(message)

    def notify_critical(self):
        notification_service = Notification()

        message = f"Critical Alert: {self.alert.labels.alertname} - {self.alert.annotations.summary}"
        notification_service.send_to_slack(message)
        if self.set_pager_flag:
            # notification_service.send_to_pagerduty(alert)
            notification_service.send_to_slack("PagerDuty incident created for critical alert")
        if self.kill_container_flag:
            kill_container_by_name(self.alert.labels.container)
            notification_service.send_to_slack(f"Container {self.alert.labels.container} killed successfully")

    def notify(self):
        if self.alert.labels.severity == SeverityType.CRITICAL:
            self.notify_critical()
        elif self.alert.labels.severity == SeverityType.WARNING:
            self.notify_warning()
        else:
            raise HTTPException(status_code=400, detail="Invalid severity level")
        