#pip install requests
#pip install lxml
import requests

response = requests.get("https://randomfox.ca/floof")
#fox = response.json()
#print(fox['image'])

print(response.status_code)
print(response.text)
print(response.json())
