# def e_potentielle(masse,hauteur,e_limite=1000,g=9.81):
#     E = masse * hauteur * g
#     if E <= 1000:
#         print("Vous êtes limite")        
#     else:
#         return E
# resultat = e_potentielle(masse=20,hauteur=2,g=9.81)
# print(resultat, 'Joules')


# def signe(x):

#     if x > 0: 
#         print(x," Positif")
#     elif x == 0:
#         print(x,'nul')
#     else:
#         print(x,'negatif')

# print(signe(5))

# for chiffre in range(10,-10,-1):
#     signe(chiffre)

# compteur = 0
# fibo = 0 
# def fibonacci (n):

#     while compteur < n:
#         fibo += compteur + 1
#         return fibo
# print(fibonacci(20))

#Liste
liste_1 = [1,4,35,84]
ville = ['paris','marseille','aix','Orange','Londre']
liste_2 = [liste_1,ville]
liste_3 = []

#Tuple
# Ne peut être modifié
tuple_12 = (1,2,5,2)

# String est aussi un tableau

#slicing
#Liste[debut:fin:pas]
# print(ville[0:1])
# print(ville[::-1])
# print(ville[::2])

for index, valeur in enumerate(ville):
    if 'marseille' in ville:
        print('Oui')
    else:
        print('Non')
    # print(index,valeur)

#La commande zip
for a,b in zip(ville,liste_1):
    print(a,b)


def fibonacci(n):
    a = 0
    b = 1
    while a < n:
        print(a)
        a,b =b, a+b
print(fibonacci(10))