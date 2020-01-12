# fonction qui renvoi le volume d'une sphère
def vol(rayon):
    return (4.0/3)*(3.14)*(rayon**3)

#print(vol(10.0))

# fonction qui verifie qu'un nombre est situé dans un intervalle donné(bornes incluses)
def verif_intervalle(num,bas,haut):
    #verifie si le nombre est entre haut et bas, inclus
    if num in range(bas,haut+1):
        print("%s est dans l'interval " %str(num))
    else:
        print("le nombre est hors intervalle.")

#verif_intervalle(10,2,11)


#ecrire fonction qui calcule le nombre de lettres majuscules et de minuscules dans une chaine

def maj_min(s):
    #on initialise les compteurs dans un dictionnaire
    d = {'maj':0,'min':0}
    for c in s:
        if c.isupper():
            d['maj'] +=1
        elif c.islower():
            d['min'] +=1
        else:
            pass
    print("Chaine de depart string : ",s)
    print("Nombre de majuscule : ",d['maj'])
    print("Nombre de minuscule : ",d['min'])

#maj_min("Bonjour Mr Martin, comment allez vous en cette belle journee de mardi ?")

#fonction qui prend une liste en entrée et retourne une nouvelle liste avec les elements unique de la premiere liste.

def list_unique(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return print(x)

#list_unique([2,2,2,1,1,5,6,7,9])

#fonction qui verifie que la chaine passé est un palindrome
def palindrome(s):
    #on enleveles espace dans la chaine
    s = s.replace(' ','')
    return s == s[::-1] #verifie par decoupage
print(palindrome("abcba"))