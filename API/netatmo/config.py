import json
import os

path = os.getcwd() + "\\API\\netatmo\\"     # répertoire projet
ficProperties = path + "properties.json"

class Properties:
    # chargement des properties de l'application
    def load_properties():
        # on lit le fichier et on positionne les variables
        with open(ficProperties, "r") as json_data_file:
            data = json.load(json_data_file)

            CLIENT_ID = data["netatmo"].get("CLIENT_ID")
            CLIENT_SECRET = data["netatmo"].get("CLIENT_SECRET")
            ACCESS_TOKEN_URL = data["netatmo"].get("ACCESS_TOKEN_URL")
            USERNAME = data["netatmo"].get("USERNAME")
            PASSWORD = data["netatmo"].get("PASSWORD")

            return CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN_URL, USERNAME, PASSWORD