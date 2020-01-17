class Exemple (object):
    pass

x = Exemple()
print(type(x))

#Classe chien
class Chien(object):
    #initialisation des attributs de classe (espece, couleur)
    espece = 'mammifere'

    def __init__(self,race,couleur):
        self.race = race
        self.couleur = couleur

sam = Chien(race="Labradeur",couleur = "vert")
print(sam)
print(sam.race)
print(sam.couleur)
print(sam.espece + ' '+ sam.race + ' '+ sam.couleur)
