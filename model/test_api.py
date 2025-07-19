import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "text": "I have experience in Python and machine learning projects."
}

response = requests.post(url, json=data)
print(response.json())



