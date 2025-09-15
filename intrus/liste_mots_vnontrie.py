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

def lecture():
    #définition de la variable fin qui est la taille de la liste -1 pour la dernière occurence et dans la rendre insensible a la casse
    fin= len(liste_mots)-1
    #création de la liste contenat les mots a la fin
    retour_mot = []
    for i in range(4):
        #création de la variable position qui prend une valeur aléatoire entre 0(première occcurence) et fin (don dernière occurence)
        position = rnd(0,fin)
        #ajout du mot pris au hasard dans la liste de rendu final
        retour_mot.append(liste_mots[position])
    return retour_mot
print(lecture())

#création de la variable propositiion qui permet de récupérer la possition du supposé intru trouvé par la personne
proposition = int(input("données la position de l'intrus (premier mots = 1)"))
def vérification(retour_mot,proposition):
    #test si la proposiotion est en dehors des limites
    if proposition <= 0:
        print("le premier mot est en position 1")
    elif proposition > len(retour_mot):
        return "donner la position d'un mots dans la liste pas au-dela"
