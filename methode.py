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

    def perimetre(self):
        p = 2*Cercle.pi*self.rayon
        return print(p)

# methode pour redefinir le rayon
    def definirRayon(self,rayon): #une sorte se setter
        self.rayon = rayon

    def obtenirRayon(self):
        return print(self.rayon)
       

#instanciation de mon_cercle
mon_cercle = Cercle(12)

#appel de la methode  calcul surface surface
mon_cercle.surface()

mon_cercle.obtenirRayon()

mon_cercle.definirRayon(2.8)
mon_cercle.obtenirRayon()
mon_cercle.perimetre()

