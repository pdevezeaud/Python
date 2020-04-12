argent = 1000

print("Vous vous installer à la table de roulette avec",argent," $.")

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

    