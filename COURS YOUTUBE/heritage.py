

class Vehicule(object):
    def __init__(self,nom, quantite_essence ):
        self.nom = nom
        self.essence = quantite_essence

    def se_deplacer(self):
        print("Le vehicule se déplace")

       

#heritage classe fille
class Voiture(Vehicule):
    def __init__(self,nom,quantite_essence,puissance):
        Vehicule.__init__(self,nom,quantite_essence)
        self.puissance = puissance

class Avion(Vehicule):
    def __init__(self,nom,essence,marchandise):
        Vehicule.__init__(self,nom,essence)
        self.marchandise = marchandise
   

#Programme principale
avion1 = Avion("rafale",1000,2000)
avion1.se_deplacer()
print(avion1.nom)

print(isinstance(avion1,Voiture))

# Fonction utiles
'''
# pour connaitre la parente d'une instance
            isinstance(<objet>,classe) : verifie q'un objet est bien une instance de la classe

issubclass(<classe_fille>, <classe_mere>): verifie qu'il herite bien de la classe mere

def __str__(self) --> renvoi un prin de l'objet

def __len__(self)

def __del__(self)
    return self.pages


'''
