'''
Mode d'ouvertures : r (lecture seul)
                    w (écriture avec remplacement)
                    a (écriture et ajout en fin de fichier)
                    x (lecture et écriture)
                    r+(lecture/écriture dans un même fichier)
Lecture : read(), readlin(), readlines()
ecriture: write()

'''


# fic = open("test2.txt", "r")
# content = fic.read()
# print(content)
# line = fic.readline()
# print(line)

# fic.close()

# print("************************************************")
# #autre methode d'ouverture de fichier
# with open("test2.txt", "a") as fic:
#     contenu = fic.read()
#     print(contenu)
# # plus besoin de fermer avec with open

# print("************************************************")

# with open("test2.txt", "a") as fic:
#     nombre = 15
#     fic.write(str(nombre))
#     fic.write("\nHola la compagnie\n")

# print("************************************************")


class Player:
    def __init__(self,name,level):
        self.name = name
        self.level = level

    def whoami(self):
        print("{} ({})".format(self.name,self.level))

p1 = Player("Philippe",10)
p1.whoami()

# 21:39



    
    


