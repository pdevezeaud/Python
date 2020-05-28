# -*- coding: utf-8 -*-
"""
Created on Sat May  2 09:52:40 2020

@author: Philippe

on travaille le plus souvent avec des tableaux à deux dimensions

A[ligne,colonne]--> indexing

A[debut:fin,debut fin]---> slicing


"""

#tableau à trois lignes et trois colonnes
import numpy as np
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
#donnera le chiffre 9
print(A[2,2])

print(A[:,0]) #on lis toute la colonne zero
print(A[0,:]) #On lis toute la ligne zero

print(A[0:2,0:2])


B = np.zeros((4,4))
B[1:3, 1:3] = 1
print(B)

C = np.zeros((5,5))
C[::2,::2] # pas de 2


A = np.random.randint(0,10,[5,5])
A[A<5]
print(A)

from scipy import misc
import matplotlib.pyplot as plt
face = misc.face(gray=True)
plt.imshow(face, cmap = plt.cm.gray)
plt.show()

A = face[400:900,400:900]
print(A.shape)


    
    







