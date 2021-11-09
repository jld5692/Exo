import requests

CLIENT_ID = "tdb"
CLIENT_SECRET = "tdb"
REDIRECT_URL = "https://gmail.com"
AUTHORIZE_URL = "https://api.netatmo.com/oauth2/authorize"
ACCESS_TOKEN_URL = "https://api.netatmo.com/oauth2/token"

#pip install requests
#pip install lxml
import requests

response = requests.get("https://api.netatmo.com/api/getmeasure?device_id=70%3Aee%3A50%3A12%3A9f%3A18&scale=1hour&type=temperature&limit=12&optimize=false&real_time=false")
#fox = response.json()
#print(fox['image'])

print(response.status_code)
print(response.text)
print(response.json())