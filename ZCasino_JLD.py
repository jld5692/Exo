from random import randint;
import os;
import math;

# Programme Casino -----------------------------------
# ----------------------------------------------------

# On commence par l'acceuil
print("Bienvenu au Casino Python")
1500
apportJeux = input("Saisiez le montant que vous apportez ce soir : ")
apportJeux = int(apportJeux)
print("-------------------------------------")
print(f"{apportJeux} euros ! Et c'est parti :-)")
print("-------------------------------------")
leJeuxContinue = True
onContinue = True

while leJeuxContinue: # La partie continue
    
    # Numéro utilisateur avec contrôle ---------------------------------------
    while True:
        numJoueur = int(input("Quel numéro jouez-vous (entre 0 et 49) ? "))

        if (numJoueur >= 0) and (numJoueur <= 49):
            if (numJoueur % 2) == 0:
                numJoueurPair = True
            else:
                numJoueurPair = False    
            break
        else:
            print("Saisie erronée --> entre à et 49 seulement !!!") 
            os.system("pause")
    # ------------------------------------------------------------------------  

    # Mise du joueur avec contrôle ---------------------------------------
    while True:
        miseJoueur = float(input("Quelle somme jouez-vous ? "))

        if (miseJoueur > 0) and (miseJoueur <= apportJeux):
            break
        else:
            print("Saisie erronée --> pas de valeur négative et pas plus que vous n'avez dans votre portefeuille !!!") 
            os.system("pause")
    # ------------------------------------------------------------------------  

    # Roulette ---------------------------------------------------------------
    print("Rien ne vas plus, la roue tourne")
    retourRoulette = int(randint(0,49))

    if (retourRoulette % 2) == 0:
        retourRoulettePair = True
    else:
        retourRoulettePair = False  

    print("-----------------------------------------------")
    print(f"La boule s'est arrêtée sur le {retourRoulette}")
    print("-----------------------------------------------")
    # ------------------------------------------------------------------------ 

        # Comparaison saisieJoueur et retour de la roulette
    if numJoueur == retourRoulette:
        print("C'est la fête !!! Vous avez gagné ;-)")
        apportJeux = apportJeux + (miseJoueur * 3)        
    elif (retourRoulettePair) == (numJoueurPair):
        print("Vous n'avez pas trouvé le bon numéro pour vous êtes en pahse avec la parité pair/impair")
        apportJeux = apportJeux + (math.ceil(miseJoueur * 0.5))        
    else:    
        print("Perdu :-(")
        apportJeux = apportJeux- miseJoueur

    print(f"Vous disposer maintenant de {apportJeux} euros")

    if apportJeux == 0:
        print("Vous êtes fauché ! FIN DU GAME !!!")
        leJeuxContinue = False
        break
    # ------------------------------------------------------------------------

    # Est-ce que l'on remise une nouvelle fois ? -----------------------------
    while True:
        onContinue = input("Vous voulez miser à nouveau O/N ?")
        if (onContinue == "O") or (onContinue == "o"): 
            leJeuxContinue = True
            break
        elif (onContinue == "N") or (onContinue == "n"):
            leJeuxContinue = False
            break
        else: 
            print(f"{onContinue} n'est pas une saisie valide")
    # ------------------------------------------------------------------------