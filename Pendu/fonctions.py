# Fonction de récupération du score de la partie
from donnees import *
from pathlib import Path
from random import choice
import pickle


def recuperer_scores():
    chemin_scores = Path(NOM_FICHIERS_SCORES)
    if chemin_scores.exists():  # le fichier existe
        with chemin_scores.open("rb") as fichier_scores:
            mon_depickler = pickle.Unpickler(fichier_scores)
            scores = mon_depickler.load()
    else:
        scores = {}

    return scores


def recuperer_nom_utilisateur():
    nom_utilisateur = input("Tapez votre nom : ")
    nom_utilisateur = nom_utilisateur.capitalize()
    if not nom_utilisateur.isalnum() or len(nom_utilisateur) < 4:
        print("Ce nom est invalide.")
        return recuperer_nom_utilisateur()
    else:
        return nom_utilisateur


def choisir_mot():
    return choice(LISTE_MOTS)


def recuperer_mot_masque(mot_complet, lettres_trouvees):
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvees:
            mot_masque += lettre
        else:
            mot_masque += "*"

    return mot_masque


def recuperer_lettre():
    lettre = input("Tapez une liettre : ")
    lettre = lettre.lower()
    if len(lettre) > 1 or not lettre.isalpha():
        print("Vous n'avez pas saisie une lettre valide.")
        return recuperer_lettre()
    else:
        return lettre


def enregistrer_scores(scores):
    with open(NOM_FICHIERS_SCORES, "wb") as fichier_scores:
        mon_pickler = pickle.Pickler(fichier_scores)
        mon_pickler.dump(scores)
