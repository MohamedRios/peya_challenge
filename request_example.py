from imp import source_from_cache
from platform import platform
import requests

url = 'http://localhost:5000/api'

r = requests.post(url, json={
    "user_id": ["abc"],
    "country": ["ar"],
    "source": ["Organic"],
    "platform": ["Android"],
    "device_family": ["Samsung Galaxy Tab"],
    "event_1": [10],
    "event_2": [1]
    })

print(r.json())