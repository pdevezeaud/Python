loop = 1
while loop == 1:

    
    ht = float(input("Entrer la valeur HT: "))
    tva = float(ht * 20.60) / 100
    ttc = ht + tva
    print("Le montant ttc est de:",ttc)
    loop = int(input("autre calcul: "))

