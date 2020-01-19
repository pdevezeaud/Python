'''
Module pour le joueur
'''

def parler(personnage,message):
    print("{}  {}".format(personnage,message))

def au_revoir():
    print("Au revoir !!")

#important de mettre main plutot que le nom du prog principale

if __name__ == "__main__":
    parler("Jason", "Bonjour tous le monde")
    au_revoir()

