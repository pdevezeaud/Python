#creation de la classe cercle
class Cercle (object):
    '''
    classe Cercle pour representer le cercle et faire des calculs de base.
    '''
    #attribut de classe
    pi = 3.14

    # premiere methode d'initialisation attribut d'instance
    def __init__(self,rayon=1):
        self.rayon = rayon

    
# methode
    def surface(self):
        calcul = Cercle.pi * self.rayon **2   
        return print(calcul)

# methode pour redefinir le rayon
    def definirrayon(self,rayon):
        self.rayon = rayon

#instanciation de mon_cercle
mon_cercle = Cercle(12)

#appel de la methode surface
mon_cercle.surface()

mon_cercle.definirrayon(5)

mon_cercle.surface()