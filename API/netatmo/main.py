import os
from datetime import datetime
# paquet maison :-) ------------------------------------------------------
import OAuth                   # import des fonctions d'authentification
import netatmo                 # import des fonctions d'accès aux infos
import config                  # import des properties
# ------------------------------------------------------------------------

# on clear la console pour mieux voir ce qui remonte en débug
clear = lambda: os.system('cls')
clear() # on vide la console

# on commence par charger les properties 
prop = config.Properties
properties = prop.load_properties()

# Pas génial --> à voir pour la visibilité des variables
CLIENT_ID = properties[0]
CLIENT_SECRET = properties[1]
ACCESS_TOKEN_URL = properties[2]
USERNAME = properties[3]
PASSWORD = properties[4]

# authentification OAuth (access et refresh token)
Tok = OAuth.Token()
token = Tok.get_access_token(CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN_URL, USERNAME, PASSWORD)

access_token = token[0]
refresh_token = token[1]

# récupération de mesure de température
Func = netatmo.Fonc()
measure_temp = Func.getmeasure(access_token)

clear() # on vide la console

# TRAITEMENT DES DONNEES A ETOFFER !!! ----------------
# on traite les données récupérées dans le dictionnaire
compteur = 0
sum_temp = 0
for key, value in measure_temp.items():
    datetime_mesure = datetime.fromtimestamp(int(key))
    temperature = float(str(value)[1:5])
    print(f"Date : {datetime_mesure} -->> température : {temperature}")
    sum_temp += temperature
    compteur += 1

temp_moyen = sum_temp / compteur
print(f"La température moyenne est de : {str(round(temp_moyen, 2))}.")