c = "ici une chaine"
print ("insertion de variable premier exemple " + c)
print ("insertion de variable deuxieme exemple %s" %(c) )

# avec des chiffres
print ("un nombre %1.2f" %(1.31))

#on peut cumler les deux 
print ("une chaine de caractere : %s et un nombre: %1.2f" % ('bonjour', 13.12))

# %r peut faire la conversion de façon automatique
print ("une chaine de caractere : %r et un nombre: %r" % ('bonjour', 13.12))

#autre méthode
print ("un élement dans une chaine {p}" .format(p="à inserer"))

print("Plusieurs {p} peuvent permettre de ne pas oublier le mot {p}".format(p = "envoir"))
