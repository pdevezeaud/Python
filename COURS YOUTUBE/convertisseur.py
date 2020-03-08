import math 

def degRad(deg):
    calcul = (deg * math.pi) /180
    return calcul


def radDeg(rad):   
    calcul = (rad*180) / math.pi
    return calcul


loop = 1
while loop == 1:


    print("Convertisseur Degré en Radian et de Radian en degré")
    print()
    print ("Veuillez choisir le type de calcul")
    print("(1) : conversion Radian vers Degré")
    print("(2) : Conversion Degré vers Radian")
    print("(3) : Quitter le programme")
    print()
    print("* * * * * * * * * * * * ")

    choix = float(input("Veuillez entrer votre choix de calcul  ? :"))

    if choix == 1:
        degnumber = float(input("Entrez le nombre de Radian pour la conversion en Degré : "))
        print("Résultat de la conversion Radian vers Degré")
        print(degRad(degnumber))
        

    elif choix == 2:
        radnumber = float(input("Entrez le nombre de Dégré pour la conversion en Radian : "))
        print("Résultat de la conversion Degré vers Radian")
        print(radDeg(radnumber))
               
    
    elif choix == 3:
        loop = 0
        print()
        print ("FIN DU PROGRAMME")
        print()
    





    