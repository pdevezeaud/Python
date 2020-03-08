import math 

def degRad(deg):
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


while choix != "Q":

    if choix == "1":
        degnumber = float(input("Entrez le nombre pour la conversion : "))
        print(degRad(degnumber))
        

    elif choix == "2":
        radnumber = float(input("Entrez le nombre pour la conversion : "))
        print(radDeg(radnumber))
        
        
    
    else choix == "Q":
        print ("fin de programme")
    





    