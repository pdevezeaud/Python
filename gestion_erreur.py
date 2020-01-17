
# iNSTRUCTION POUR GERER LES EXCEPTIONS (BASE)

# ageUtilisateur = input("Quel âge as tu ?")

# try:
#     ageUtilisateur = int(ageUtilisateur)
# except:
#     print("L'âge indiqué est incorrect !")
# else:
#     print("Tu as", ageUtilisateur, "ans")
# finally:
#     print("FIN DU PROGRAMME")

#autre Exemple
nombre1 = 150

nombre2 = input("Choisir nombre pour diviser : ")
try:
    nombre2= int(nombre2)
    print("Résultat = {}".format(nombre1/nombre2))
except ZeroDivisionError:
    print("Vous ne pouvez diviser par 0.")
except ValueError:
    print("Vous devez entrer un nombre.")
except:
    print("Valeur incorrect.")
finally:
    print("FIN DU PROGRAMME")