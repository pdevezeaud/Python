# est une sorte de fonction anonyme

def carre(num):
    resultat = num ** 2
    return print(resultat)

#carre(2)

#simplification du code
def carree(num):
    return num ** 2

# lambda est-il pair
paire = lambda x: x%2 == 0

print (paire(2))

#print(carree(2))

# possibilité de le faire sur une ligne
def care(num): return print(num ** 2)

#care(2)

# avec la simplification lambda
carre = lambda num: num ** 2
print(carre(2))

#autre utiliation avec une chaine de caractere, retourne le premier caractere
premier_caract = lambda s: s[2]
print(premier_caract("Philippe"))

#un peu de verlan
verlan = lambda s: s[::-1]
print(verlan("merde"))

#addition (lambda très simple)
addition = lambda x,y : x+y
print(addition(12,1))