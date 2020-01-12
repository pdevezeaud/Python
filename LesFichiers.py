fichier = open("test.txt")
print (fichier.read())
# une fois lu ce contenu ne peut etre relu.
# Par contre si on remet le pointeur à zero celui-ci permettra de relire le fichier
fichier.seek(0)
print (fichier.read())

#autre maniere de lire un fichier avec readline (li l'integralité du fichier et le met d'une certaine facon dans un tableau)
fichier.seek(0)
print (fichier.readline())
fichier = open("test.txt", "w+")
fichier.write("ajout suite open w+")
print(fichier.readlines)
#w remplace le contenu.

#boucle sur fichier
fichier = open("test2.txt")
# Pour une ligne que j'ouvre dans le fichier txt
for ligne in open('test2.txt'):
    print(ligne)

