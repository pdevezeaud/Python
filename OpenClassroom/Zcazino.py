import os
import random
from math import ceil

argent = 1000
somme_a_miser = -1
continuer_partie = True


print("Vous vous installer à la table de roulette avec",argent," $.")

while continuer_partie:



# Choix du chiffre a miser
    nbre_a_miser = -1
    while nbre_a_miser < 0 or nbre_a_miser > 49:
        nbre_a_miser = input("Taper le chiffre compris en 1 et 49 : ")
        try:
            nbre_a_miser = int(nbre_a_miser)
        except ValueError:
            print("Vous n'avez pas saisie de nombre")
            nbre_a_miser = -1
            continue
        if nbre_a_miser < 1:
            print("Vous devez rentrer un chiffre superieur à 0")
            nbre_a_miser = -1
        if nbre_a_miser > 49:
            print("Ce nombre est superieur à 49")
            nbre_a_miser = -1

    print(nbre_a_miser)

    # choix de la somme à miser

    print("Il est temps de miser une somme")
    while somme_a_miser <= 0 or somme_a_miser > argent:
        somme_a_miser = input("Entrer votre mise svp : ")
        try:
            somme_a_miser = int(somme_a_miser)
        except ValueError:
            print("vous n'avez pas rentré de somme à somme_a_miserr")
            somme_a_miser = -1
            continue
        if somme_a_miser <=0:
            print("La somme doit être superieur à 0")
        if somme_a_miser > argent:
            print("La somme ne peut être superieur a la somme engagé soit :",argent)
        
    print(somme_a_miser)


    # tirage aletoire du chiffre de la roullette
    nombre_aleatoire = random.randrange(1,49,1)
    print("Rien ne va plus, la roulette tourne !! les jeux sont faits. Le casino tire : ",nombre_aleatoire)


    # comparaison choix joueur et tirage
    if nombre_aleatoire == nbre_a_miser:
        argent += somme_a_miser * 3
        
    elif nombre_aleatoire %2 == nbre_a_miser %2:
        somme_a_miser = ceil(somme_a_miser *3)
        print("Vous avez parié sur la bonne couleur, vous obtnez ",somme_a_miser," $")
    else:
        print("Desolais l'ami vous perdez votre mise, pour la prochaine fois peut etre")
        argent -= somme_a_miser
    print(argent)

    # On verifie que joueur à toujour de l'argent
    if argent <= 0:
        print("Vous n'avez plus d'argent en poche pour continuer à jouer")
        continuer_partie = False
    else:
        # on affiche l'argent du joueur
        print("vous avez à présent en argent la somme de :",argent)
        quitter_partie = input("Souhaitez vous quittez la partie (o/n) ?")
        if quitter_partie == "o" or quitter_partie == "O":
            print("Vous quittez le casino avec vos gains")
            continuer_partie = False

# pause systeme
os.systeme("pause")



    

    