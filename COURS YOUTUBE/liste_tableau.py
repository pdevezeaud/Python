'''

'''
#instanciation d'une liste vide
inventaire = list() #ou en mettant des crochet vide []
inventaire2 = [1,6,15, "voiture"]
inventaire3 = [0] * 5  # cree un tableau avec 5 zeros
inventaire4 = ["arc","epee","bouclier","potion","flèche","tunique"]

print(inventaire)
for valeur in inventaire4:
    print(valeur)

print("*******************************")
#pour acceder à l'element il suffit de lui donner son indice
#pour acceder au deuxieme element du tableaux
print(inventaire4[:2]) 
print("*******************************")
#pour acceder au derniers elements
print(inventaire4[3:])
print("*******************************")
# acceder aux element en partant de la fin
print(inventaire4[-4])
print("*******************************")
print(inventaire4[2:4])
print("*******************************")
# modification 
inventaire4[1]= "Hache de guerre"
print(inventaire4)
print("*******************************")

# rechercher dans une liste un element
if "potion" in inventaire4:
    print("Je possede une potion")
else:
    print("Je n'ai pas cette article")

print("*******************************")

#ajout d'element dans iventaire 4
inventaire5 = ["renault","renault","renault","citroen","fiat","porshe","civic","hyundai"]
print(inventaire5[:])
inventaire5.append("ferrari")
print(inventaire5[:])
inventaire5.insert(1,"sherman")
print(inventaire5[:])

print("*******************************")

#suppression d'un element dans la liste
inventaire5.remove("sherman")
print(inventaire5[:])
#autre methode
del inventaire5[0]
print(inventaire5[:])

objet_supprimer = inventaire5.index("citroen")
del inventaire5[objet_supprimer]
print(inventaire5[:])

print("*******************************")
#Trier des elements dans un tableau
inventaire5.sort()
print(inventaire5[:])

print("*******************************")
#compter ne nombre d'un meme elements

print("Nombre de renault :",inventaire5.count("renault"))

print("*******************************")

# 30;08









