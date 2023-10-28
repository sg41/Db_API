import psutil
import requests
import time

memory_threshold = 80
api_url = 'http://your-api-endpoint'


def send_alarm():
    response = requests.post(
        api_url, json={'message': 'Memory threshold exceeded'})
    if response.status_code == 200:
        print('Alarm generated successfully')
    else:
        print('Failed to generate alarm')


while True:
    memory_percent = psutil.virtual_memory().percent
    if memory_percent > memory_threshold:
        send_alarm()
    time.sleep(60)
