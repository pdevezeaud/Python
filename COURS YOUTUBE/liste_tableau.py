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

#22:46



