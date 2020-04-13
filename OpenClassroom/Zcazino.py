import random
from math import ceil

argent = 1000
somme_a_miser = -1


print("Vous vous installer à la table de roulette avec",argent," $.")


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


