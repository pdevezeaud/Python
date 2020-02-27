import math 


def degRad(deg):
    degnumber = input("Entrez le nombre pour la conversion : ")
    calcul = (deg * math.pi) /180
    return calcul


def radDeg(rad):
    
    calcul = (rad*180) / math.pi
    return calcul

print ("Veuillez choisir le type de calcul")
print("1 : conversion Radian vers Degré")
print("2 : Conversion Degré vers Radian")
print("Q : Quitter le programme")
print(" ")
print("* * * * * * * * * * * * ")
choix = input("Veuillez entrer votre choix ? :")

if choix == "1":
    degnumber = input("Entrez le nombre pour la conversion : ")
    print(degRad(degnumber))

elif choix == "2":
    radnumber = input("Entrez le nombre pour la conversion : ")
    print(radDeg(radnumber))

elif choix == "Q":
    print("Vous quittez le programme de conversion.")

 