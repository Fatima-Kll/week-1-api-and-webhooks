import requests

url = "http://localhost:5678/webhook-test/36ac1fef-9062-4eb3-913f-0491442dd6a7"

payload = {
    "name": "kellal fatima",
    "email": "kelfatima22@gmail",
    "service": "AI automation"
}

response = requests.post(url , json=payload , timeout=10)

print(response.status_code)
print(response.json())