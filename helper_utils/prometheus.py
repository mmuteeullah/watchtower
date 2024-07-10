import requests

class Prometheus:
    def __init__(self, url="http://prometheus:9090/api/v1/query"):
        self.url = url

    def get_cpu_usage(self, job: str) -> dict:
        query = f'cpu_usage{{job="{job}"}}'

        params = {
            'query': query
        }
        response = requests.get(self.url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success' and data['data']['result']:
                return data['data']['result'][0]['value'][1]
            else:
                raise ValueError("No data returned from Prometheus")
        else:
            response.raise_for_status()
