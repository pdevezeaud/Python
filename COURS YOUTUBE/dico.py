#dcitonnaire ressemble à tableau associatif
'''
dico = {}   #vide
       {<clé>:<valeur>,<clé>:<valeur>}

accès à une valeur : dico[<cle>]
'''
dico = {1:45,"prenom":"Jason"}
print(dico)
dico["chat"] ="Meilleur ami de l'homme"
print(dico)
# SUPRESSION 
valeur_a_supprimer = dico.pop("prenom")
print(valeur_a_supprimer)
print(dico)
#autre methode avec del

#verfier existance du clé dans un dico
if "Jason" in dico:
    print("est present")
else:
    print("N'est pas présent")

# affichage des clés
for keys in dico:
    print(keys)

# ou
for keys in dico.keys():
    print(keys)

# ou
for keys,valeurs in dico.items():
    print("clé {} : valeur {}".format(keys,valeurs))

# dico 18:44