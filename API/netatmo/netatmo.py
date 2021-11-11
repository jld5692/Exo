import requests
import json
import sys

class Fonc:
    # récupération de données auprès de netamo 
    def getmeasure(self, access_token):
        URL_API = "https://api.netatmo.com/api/getmeasure"

        payload = {'device_id': '70:ee:50:12:9f:18', 
                    'scale': '1hour',
                    'type': 'temperature', 
                    'limit': '12', 
                    'optimize': 
                    'false', 
                    'real_time': 'false'
                    }

        headers = {'Authorization': 'Bearer ' + access_token}

        measure_response = requests.get(URL_API, params=payload, headers=headers)

        if measure_response.status_code !=200:
            print("Erreur dans la mesure")
            sys.exit(1)
            
        measure = json.loads(measure_response.text)
        return measure['body']