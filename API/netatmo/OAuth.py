import requests
import json
import sys
# paquet maison :-) ------------------------------------------------------
import config
# ------------------------------------------------------------------------

class Token:
    # token OAuth chez netatmo
    def get_access_token(self, CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN_URL, USERNAME, PASSWORD):
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