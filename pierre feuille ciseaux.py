import random 
#on importe random
#taille de la partie
short = 1 #1 manche
moyenne = 3 #3 manche
longue = 10 # 10 manche
def shifumi(namej1,namej2,nbr_de_manche):
    #on crée une liste composée par tout ce que l'on peux faire
    possibility = [ "pierre" , "feuille" , "ciseaux"]
    #on initialise le compteur de points de chaque joueur
    j2_compteur = 0
    j1_compteur = 0 
    while j1_compteur < nbr_de_manche  and  j2_compteur < nbr_de_manche:
        #on affiche le score de chaque joueur
        print(j1_compteur, j2_compteur)
        #on demande au joueur de choisir entre pierre, feuille et ciseaux
        joueur1 = input("choissez entre pierre, feuille et ciseaux " )
        #on choisit de manière alétaoire pour l'ordi
        i= random.randint(0,2)
        joueur2 = possibility[i]
        #on test le choix du joueur pour savoir s'il est valide
        if joueur1 in possibility:
            #on procède à la comparaison entre le choix du joueur et celui de l'ordi
            if joueur1 == joueur2:
               résultat = "aucun gagnant"
            elif joueur1 == possibility[0] and i == 1:
                j2_compteur+=1
                résultat ="perdu victoire de l'ordi"
            elif joueur1 == possibility[2] and i == 0:
                j2_compteur+=1
                résultat = "perdu victoire de l'ordi"
            elif joueur1 == possibility[1] and i == 2:
                j2_compteur+=1
                résultat ="perdu victoire de l'ordi"
            elif joueur1 == possibility[2] and i == 1:
                j1_compteur +=1
                résultat = "victoire!!🎉"
            elif joueur1 == possibility[0] and i == 2:
                j1_compteur +=1
                résultat = "victoire!!🎉"
            elif joueur1 == possibility[1] and i == 0:
                j1_compteur +=1
                résultat = "victoire!!🎉"
            #on affiche le résultat de la manche
            print(résultat)
        else:
        #on affiche un message, si le joueur ne respecte pas les règles
            return "eh oh, on a dit pierre, feuille et ciseaux. tu fais quoi là!?"
    # on test la différence entre les deux compteurs pour savoir qui a gagné
    if j1_compteur>j2_compteur:
        #on affiche le nom du gagnant
        return namej1 + " a gagné🎉"
    elif j1_compteur == j2_compteur:
        #on affiche un message si il y a égalité
        return "égalité" 
    else:
        #on affiche le nom du gagnant
        return namej2 + " a gagné"
    
print(shifumi(namej1="Vladimir", namej2="Ordi",nbr_de_manche=longue ))