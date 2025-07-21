import requests
import json

response = requests.get("https://api.sampleapis.com/coffee/hot")
data = response.json()
print(json.dumps(data,indent=4))
