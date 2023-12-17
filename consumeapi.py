import requests

age=19
sex='F'
response=requests.get(f"http://127.0.0.1:8000/predicttt?age={age}&sex={sex}")
output=response.json()
print(output)