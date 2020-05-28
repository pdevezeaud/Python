# -*- coding: utf-8 -*-
"""
Created on Fri May  1 14:06:15 2020

@author: Philippe
"""
import numpy as np

#np.shape
#shape est un tuple
#shape n'est pas modifiable

a = np.array([1,2,3])
#permet de connaitre la dimension du tableau
print(a.shape) 
# deux commande importante pour np
# l'attribut size
# on initie un tableau de 3 lignes et 2 colonnes
b = np.zeros((3,2))
print(b)

# np.full((2,3),9)
#np.ones(shape)
#np.eye()
#np.size()

#np.random.randn

#dtype permet de préciser le type de données.

#manipulation de ces tableaux

c = np.zeros((3,2))
print(c)
d= np.ones((3,2))
print(d)

#1er methode (l'assemblage soit de facon vertical ou horizontale)
#hstack pour horizontale
#vstack pour la verticale
#np.concatenate

a = np.hstack((c,d))
print(a)

#ravel()

#reshape, random, concatenate
