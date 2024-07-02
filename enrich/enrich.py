from models.models import Alert
from enrich.call_prometheus import get_cpu_usage

def enrich_critical_alert(alert: Alert, **kwargs) -> Alert:
    alert, set_pager_flag, kill_container_flag  = check_cpu_usage(alert)
    return alert, set_pager_flag, kill_container_flag

def check_cpu_usage(alert: Alert) -> Alert:
    instance = alert.labels.container
    job = alert.labels.job
    cpu_usage = 0
    set_pager_flag = False
    kill_container_flag = False
    try:
        cpu_usage = float(get_cpu_usage(job))
        if cpu_usage > 80.0:
            set_pager_flag = True
            kill_container_flag = True
    except Exception as e:
        print(f"Failed to fetch CPU usage: {e}")
    return alert, set_pager_flag, kill_container_flag
