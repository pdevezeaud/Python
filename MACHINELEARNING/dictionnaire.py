# import numpy as np
# import time

# traduction = {
#     "chien": "dog",
#     "chat": "cat",
#     "souris": "mousse",
#     "oiseau": "bird"
# }

# #print (type(traduction))

# inventaire = {
#     "banane": 5000,
#     "Pomme": 2094,
#     "Poires": 4200

# }

# #peut contenir d'autres dico
# dictionnaire_3 = {
#     "dict_1":traduction,
#     "dict_2": inventaire
# }


# parametres = {
#     "w1": np.random.randn(10,100),
#     "b1": np.random.randn(10,100),
#     "w2": np.random.randn(10,100),
#     "b2": np.random.randn(10,100)
# }

# print(inventaire.values())
# print(inventaire.keys())
# print(len(inventaire))
# #ajout dans inventaire
# inventaire["Abricot"] = "100"
# print(inventaire)
# #provoque une erreur car peche n'existe pas dans le dico
# #print(inventaire["peches"])
# #avec la methode get on peut ajouter un deuxieme argument pour avoir un retour
# print(inventaire.get("peches",1))

# #a partir d'une liste on peut crée un dico sans valeur
# liste_1 = ('Paris','Cognac','Londres','Bruxelles')
# print(inventaire.fromkeys(liste_1,'Défaut'))
# print(inventaire)

# for i in inventaire:
#     print(i)

# for i in inventaire.values():
#     print(i)

# for k,v in inventaire.items():
#     print(k,v)

# #liste de comprehension (ici on stocke le carre des nombres)
# liste_2 = [i**2 for i in range(10)]
# print(liste_2)

# start_time = time.time()
# list_3 = []
# for i in range(10000000):
#     list_3.append(i**2)

# end_time = time.time()

# print(end_time - start_time)

# #avec une liste de comprehension
# start_time = time.time()
# list_4 = [i**2 for i in range(10000000)]
# end_time = time.time()
# print(end_time - start_time)

#nested list soit une liste dans une liste
#premiere liste
# list_5 = [i for i in range(3)]
# #la liste dans la liste
# list_6 =[[i for i in range(3)] for j in range(3)]
# print(list_5)
# print(list_6)

# #dictionnaire comprehension
# liste_nom = {
#     "0": "Pierre",
#     "1": "Jean",
#     "3": "Julie",
#     "4": "Sophie"
# }

# prenoms = ['Pierre','Jean','Julie', 'Sophie']

# dico = {k:v for k,v  in enumerate(prenoms)}
# print(dico)

# #Utilisation de zip
# ages = [24,62,21,45]
# dico_age = {prenom:age for prenom, age in zip(prenoms,ages)}
# print(dico_age)

#Tuple comprehension

tuple_1 = {i**2 for i in range(10)}
print(tuple_1)




