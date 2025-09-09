#création d'une base de données contenant la liste de nom
liste_mots = [
    "Étoile",
    "Mystère",
    "Papillon",
    "Crépitement",
    "Lumière",
    "Sérénité",
    "Mélodie",
    "Océan",
    "Vertige",
    "Souvenir",
    "Marbre",
    "Éclair",
    "Silence",
    "Aventure",
    "Racine",
    "Éphémère",
    "Rêverie",
    "Courage",
    "Brouillard",
    "Élan"
]
#import random pour prnedre un mot au hasard
from random import randint as rnd
#définition de la variable fin qui est la taille de la liste -1 pour la dernière occurence
fin= len(liste_mots)-1
position = rnd(0,fin)
print(position)
print(liste_mots[position])
