# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 19:03:15 2020

@author: Philippe
"""


x = -3
z = 3.14
print(abs(x))
print(round(z))

liste_1 = [0,25,14,-19]
print(max(liste_1))
print(min(liste_1))

print(sum(liste_1))

#conversion de int ou en string
a = 10
print(type(a))
a = str(a)
print(type(a))

# transformation de liste en tuple ou en dico

liste_1 = [10,5,8,78]
tuple_1 = tuple(liste_1)
print(tuple_1)


# Fonction format
x = 25
ville = 'Paris'
#message = "La temperature est de {} degréCelsius a {}".format(x,ville)
#ou
message= f"La temperature est de {x} degréCelsius a {ville}"
print(message)

#fonction Open
f = open('fichier.txt','w')
f.write("Bonjour")
f.close()

f = open('fichier.txt','r')
f.read()

with open('fichier.txt','r') as f:
    print(f.read())
    
with open('fichier.txt','w') as f:
    for i in range(10):
        f.write("{}^2 = {} \n".format(i, i**2))