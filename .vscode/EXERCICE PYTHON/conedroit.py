#formule : pi / 3 (rayon)*2 *hauteur  (donne volume)
from math import pi

rayon = float(input("Entrer le rayon : "))
hauteur = float(input("Entrer la hauteur : "))

volume = (pi * rayon * rayon * hauteur) / 3
print(volume)