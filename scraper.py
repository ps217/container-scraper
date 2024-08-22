import time
import requests

METRICS_URL = "http://metrics-server/metrics"

while True:
    try:
        response = requests.get(METRICS_URL)
        response.raise_for_status()
        print(f"Metrics:\n{response.text}", flush=True)
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch metrics: {e}", flush=True)
    time.sleep(5)
