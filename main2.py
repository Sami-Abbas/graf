import time
import requests
import json
import random

def get_rounded_timestamp():
    return int(time.time() / 10) * 10

def generate_random_metric_value():
    return random.uniform(100, 1000)

def create_data(timestamp_now, timestamp_prev):
    value_now = generate_random_metric_value()
    value_prev = generate_random_metric_value()
    
    return [
        {
            "name": "test.metric",
            "interval": 10,
            "value": value_prev,
            "time": timestamp_prev
        },
        {
            "name": "test.metric",
            "interval": 10,
            "value": value_now,
            "time": timestamp_now
        },
        {
            "name": "test.metric.tagged",
            "interval": 10,
            "value": 1,
            "tags": ["foo=bar", "baz=quux"],
            "time": timestamp_prev
        },
        {
            "name": "test.metric.tagged",
            "interval": 10,
            "value": 2,
            "tags": ["foo=bar", "baz=quux"],
            "time": timestamp_now
        }
    ]


headers = {
    "Authorization": "Bearer 149418:eyJrIjoiZTVkYWY1N2MzZmNmYjIzMjU0YTNlNDhlMWFmZjlhZmNiMTAxNGJhNSIsIm4iOiJ0ZXN0IiwiaWQiOjQyMDQ5fQ==",
    "Content-Type": "application/json"
}
ingest_endpoint = "https://graphite-blocks-prod-us-central1.grafana.net/graphite/metrics"

while True:
   
    timestamp_now_rounded = get_rounded_timestamp()
    timestamp_prev_rounded = timestamp_now_rounded - 10


    data = create_data(timestamp_now_rounded, timestamp_prev_rounded)


    response = requests.post(ingest_endpoint, headers=headers, data=json.dumps(data))


    print(response.status_code)
    print(response.content)


    time.sleep(10)
