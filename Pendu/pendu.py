"""
Fichier main du pendu
"""

# on import les deu autres fichiers
from donnees import *
from fonctions import *

# on commence par récupérer les scores de la partie
scores = recuperer_scores()

# on récupère un nom d'utilisateur
utilisateur = recuperer_nom_utilisateur()

# si l'utilisateur n'a pas encore de score, on l'ajoute
if utilisateur not in scores.keys():
    scores[utilisateur] = 0  # 0 point pour commencer

# variable pour savoir si la partie continue ou non
continuer_partie = 0

while continuer_partie != "n":
    print(f"Joueur {utilisateur} : {scores[utilisateur]} point(s)")
    mot_a_trouver = choisir_mot()
    lettres_trouvees = set()
    mot_trouve = recuperer_mot_masque(mot_a_trouver, lettres_trouvees)
    nb_chances = NB_COUPS

    while mot_a_trouver != mot_trouve and nb_chances > 0:
        print(f"Le mot à trouver : {mot_trouve}")
        lettre = recuperer_lettre()
        if lettre in lettres_trouvees:
            print("Vous avez déjà choisit cette lettre.")
        elif lettre in mot_a_trouver:
            print("Bien joué.")
        else:
            nb_chances -= 1
            print("... non, cette lettre ne se trouve pas dans le mot ...")
        lettres_trouvees.add(lettre)
        mot_trouve = recuperer_mot_masque(mot_a_trouver, lettres_trouvees)

    if mot_a_trouver == mot_trouve:
        print(f"Félicitations ! Vous avez trouvé le mode {mot_a_trouver}.")
    else:
        print("PENDU !!! Vous avez perdu.")

    scores[utilisateur] += nb_chances

    continuer_partie = input("souhaitez-vous continuer la partie (O/N) ?")
    continuer_partie = continuer_partie.lower()

enregistrer_scores(scores)
