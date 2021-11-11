import requests
import json
import sys
# paquet maison :-) ------------------------------------------------------
import config
# ------------------------------------------------------------------------

class Token:
    # token OAuth chez netatmo
    def get_access_token(self, CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN_URL, USERNAME, PASSWORD):
        #CLIENT_ID = "618a158d3fd6211eb73f584f"
        #CLIENT_SECRET = "RGKs0pJLMBHNP8mRtfbiZw7HFX4NaIuZcrAoeJb9J6GuE"
        #ACCESS_TOKEN_URL = "https://api.netatmo.com/oauth2/token"
        #USERNAME = "jerome.ledorze@gmail.com"
        #PASSWORD = "Mig29Fulcrum%4"

        data = [
            ('grant_type', 'password'),
            ('client_id', CLIENT_ID),
            ('client_secret', CLIENT_SECRET),
            ('username', USERNAME),
            ('password', PASSWORD),
            ('scope', 'read_station')
        ]
        
        access_token_response = requests.post(ACCESS_TOKEN_URL, data=data)
    
        #print(access_token_response.text)

        if access_token_response.status_code !=200:
            print("Aye caramba !")
            sys.exit(1)
            
        tokens = json.loads(access_token_response.text)
        return tokens['access_token'], tokens['refresh_token'] 