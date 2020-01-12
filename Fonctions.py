'''
fonction qui dit bonjour
'''
def dire_bonjour():
    print("bonjour !")


'''
fonction avec parametre ici le nom
'''
def bienvenu(nom):
    print("Bonjour %s" %nom)

bienvenu('Philippe')

'''
fonction avec un retour (return)
'''
def ajoute (num1,num2):
    return num1 + num2

x =ajoute(5,10)
print (x)