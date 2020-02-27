import math 


def degRad(deg):
    degnumber = input("Entrez le nombre pour la conversion : ")
    calcul = (deg * math.pi) /180
    return print(calcul)


def radDeg(rad):
    radnumber = input("Entrez le nombre pour la conversion : ")
    calcul = (rad*180) / math.pi
    return print(calcul)

print ("Veuillez choisir le type de calcul")
print("1 : conversion Radian vers Degré")
print("2 : Conversion Degré vers Radian")
print("Q : Quitter le programme")
print(" ")
print("* * * * * * * * * * * * ")
#choix = input("Veuillez entrer votre choix ? :")

#degRad(1)
#radDeg(1)  