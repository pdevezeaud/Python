import random

#boolean utilisé pour savoir si la main est en jeu
jouer = False

#initialisation des jetons. Aurais pu etre demandé en début de partie
jeton = 100

pari = 1

rejouer_phrase = "Entrez 'd" pour donner les cartes à nouveau, ou 'q' pour quitter"

# symbol carte
symbole = ('Coeur','Carreau', 'Trèfle','Pique')

# hauteur possible
hauteur_cartes =('As','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Reine', 'Roi')

# Les valeurs de points, (L'AS peut valoir 1 ou 11, regardez self.petit pour comprendre)
valeur_carte = {'As':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Valet':10, 'Reine':10, 'Roi':10}

class Carte:

    def __init__(self,symbole,hauteur):
        self.symbole = symbole
        self.hauteur = hauteur

    def __str__(self):
        return self.symbole + self.hauteur

    def affiche_couleur(self):
        return self.symbole
    def affiche_hauteur(self):
        return self.hauteur

    def tirer(self):
        print(self.hauteur + " de " + self.symbole)
