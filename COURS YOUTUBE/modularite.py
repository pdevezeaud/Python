'''
Importer un module : import <nom_module>
                     from <nom_module> import <nom_fonction>
                     from <nom_module> import *

                     import os
                     os.system("cls")

import includes.player as player

'''
import os
import player_module
from math import sqrt
resultat = sqrt(100)
print(resultat)
#clean l'ecran
os.system("cls")
os.system("ping 127.0.0.1")

player_module.au_revoir()
player_module.parler("Philippe","Salut les Noobs!!")