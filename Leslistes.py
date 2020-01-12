ma_liste = [1,2,3]
print (ma_liste)
ma_liste_heterogene = ["une chaine",23,12,"o"]
print (ma_liste_heterogene)

print (ma_liste_heterogene[0])
ma_liste_heterogene = ma_liste_heterogene + ['nouveau']
print (ma_liste_heterogene)
ma_liste_heterogene
ma_liste_heterogene.append("un de plus")
print (ma_liste_heterogene)
# pop permet d'extraire- ici on enleve "une chaine". celui-ci ne sera plus dans le tableau
ma_liste_heterogene.pop(0)
print (ma_liste_heterogene)
# reverse permet de renverser la liste
ma_liste_heterogene.reverse()
print (ma_liste_heterogene)

#Matrice
l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]

matrice = [l1,l2,l3]
print (matrice)

#liste en compréhension (fait une ligne avec les élements de chaque ligne --> ici ligne 0)
col = [ligne[0] for ligne in matrice]
print(col) 

