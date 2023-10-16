import requests

url = 'http://localhost:9696/predict_docker'

client = {"job": "retired", "duration": 445, "poutcome": "success"}
response = requests.post(url, json=client).json()
print(response)