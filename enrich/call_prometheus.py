import requests

PROMETHEUS_URL = "http://prometheus:9090"

def get_cpu_usage(job: str) -> dict:
    query = f'cpu_usage{{job="{job}"}}'
    url = f'{PROMETHEUS_URL}/api/v1/query'
    params = {
        'query': query
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success' and data['data']['result']:
            return data['data']['result'][0]['value'][1]
        else:
            raise ValueError("No data returned from Prometheus")
    else:
        response.raise_for_status()
