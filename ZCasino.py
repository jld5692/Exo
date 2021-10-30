import os
import math
from random import randint
#from math import ciel

argent = 1000
continuer_partie = True

while continuer_partie:

    # on traite la saisie du nombre du client
    nombre_mise = -1
    while nombre_mise < 0:
        nombre_mise = input("Tapez le nombre sur lequel vous voulez miser (entre 0 et 49) : ")
        try:
            nombre_mise = int(nombre_mise)
            if nombre_mise < 0 or nombre_mise > 49:
                raise ValueError
        except ValueError:
            print("Vous n'avez pas saisi de nombre valide.")
            nombre_mise = -1
    # ----------------------------------------

    # on traite la mise du client
    mise = -1
    while mise < 0 or mise > argent:
        mise = input("Tapez le montant de votre mise : ")
        try:
            mise = int(mise)
            if mise < 0 or mise > argent:
                raise ValueError
        except ValueError:
            print("Vous n'avez pas saisi de nombre valide.")
            mise = -1
    # ----------------------------------------

    # on lance la roulette
    numero_gagnant = randint(0,49)
    print(f"La roulette s'est arrêté sur le {numero_gagnant}")
    # ----------------------------------------

    # on vérifie si gagné ou pas 
    if numero_gagnant == nombre_mise:
        print("Bravo gagné !")
        argent += mise * 3
    elif numero_gagnant %2 == nombre_mise %2:
        argent += math.ceil(mise * 0.5)
    else:
        print("Désolé perdu")
        argent -= mise
    # ----------------------------------------

    if argent <= 0:
        continuer_partie = False
    else:
        print(f"Vous disposez actellement de {argent} euros dans votre cagnote.")
        quitter = input("Souhaitez vous quitter le casino (o/n)")
        if quitter == "o" or quitter == "O":
            print("Fin de la partie. Au revoir.")
            continuer_partie = False

os.system("pause")

