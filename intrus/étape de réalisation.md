# Création d'un programme intrus.

Le programme a pour mission finale de données une liste de mots et c'est à nous de trouver l'intrus celui-ci sera défini par rapport à des thèmes. 

## Etape 1 : base de donnée.
Création d'une base de test avec 20 occurences (**agrandi plus tard**).

## Etape 2 : Algorithme de lecture.
Création d'un algorithme basique qui import randint et qui prend un mot aléatoire de la liste (**sur le doc de la base de données pour le moment**).

## Etape 3 : Mise en place de cet algorithme sour forme de fonction.
Transformation de toutes les variables isolés en une fonction qui retourne maintenant une liste de 4 mots (***cependant il peut encore y avoir des doublons à corriger***)

## Etape 4 : Création d'une question pour qui est l'intru.
Création d'un input pour sélectionner le supposer intru pour le joueur, ce à partir de la position avec 1 = le premier mot (même si en python le premier de la liste est 0).
Ajout du début de la fonction complémentaire de vérification qui prend en compte si le retour est en dehors des limite donc au-dessus du nombre d'occurence ou négatif.

## Etape 5 : Séparation entre le code et la database
Création du doc code et déplacement des fonctions définies et variable dessus.
Ajout d'une liste de 200 mots uniques dans la base de donnée (*généré par IA*).

## Etape 6 : Transformation de la database pour ajout de thèmes.
Modfication de la base de donnée en transformant en dictionnaire la précédente liste prenant comme clef le thème et comme valeur une liste de mots appartenants a ce thème.