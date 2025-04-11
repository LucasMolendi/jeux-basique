from random import randint

def mot_aleatoire():
    """ Cette fonction crée un mot aléatoire de 5 lettres parmi A, B, C ou D """
    #On peut commencer par initialiser le mot à vide
    mot=''
    liste=['A','B','C','D']
    for _ in range (5):
        a = randint(0,3)
        mot+=liste[a]

    #On renvoie le mot créé
    return mot

#On essaye la fonction
mot_cache=mot_aleatoire()
def mot_valide(mot):
    """
    Cette fonction valide la saisie de l'utilisateur qui est passée par la variable mot.
        La longueur doit être 5 et les lettres parmi A, B, C et D
        Elle renvoie True si c'est correct, False sinon"""
    #On commence par initialiser le booléen qui donnera la réponde
    reponse = len(mot) == 5 #on regarde si la longueur est 5

    #on parcourt toutes les lettres
    for lettre in mot:
        reponse = reponse and lettre in "ABCD"

    #On renvoie la réponse
    return reponse
def etude_mot(mot,mot_cache):
    """ Cette fonction renvoie le nombre de lettres bien placées et de lettres mal placées
    de la variable mot par rapport au modèle mot_cache"""
    #On initialise les variables
    lettres_bien_placees=0
    lettres_mal_placees=0
    #lettres bien placées
    for i in range(5):
        if mot[i]==mot_cache[i]:
            lettres_bien_placees+=1
    #lettres mal placées
    somme_minimum=0
    for lettre in 'ABCD':
        somme_minimum += min(mot.count(lettre),mot_cache.count(lettre))
    lettres_mal_placees = somme_minimum - lettres_bien_placees


    #On renvoie les deux valeurs
    return lettres_bien_placees,lettres_mal_placees
mot_cache=mot_aleatoire()
compteur=0
bien=0
while bien!=5:
    mot=''
    while not mot_valide(mot):
        mot=input('proposez un mot de 5 lettre composé des lettres A,B,C ou D:')
    bien,mal=etude_mot(mot,mot_cache)
    if bien==5:
        print('BRAVO! en',compteur,'coups')
    else:
        print('Il y a',bien,'lettres bien placées et', mal, 'lettre mal placées')
