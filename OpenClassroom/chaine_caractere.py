# chaine = str() #on crée une chaine vide
# #ou chaine = ""

# while chaine.lower !="q":
#     print("tapez q pour quitter !")
#     chaine = input()
# print("merci !!")

# minuscules = "une chaine en minuscule"
# print(minuscules.upper())
# print(minuscules.capitalize())

# prenom = "Philippe"
# nom = "DEVEZEAUD"
# age = 25
# print("Je m'appelle {0} {1} et j'ai {2} ans.".format(prenom,nom,age))

# ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# for i, element in enumerate(ma_liste):
#     print("L'indice {} se trouve à {}".format(i,element))

# for element in enumerate(ma_liste):
#     print(element)

# def decomposer(entier,divise_par):
#     '''Cette fonction retourne la partie entiere et le reste de entier / divse_par'''
#     p_e = entier // divise_par
#     reste = entier % divise_par
#     return p_e, reste

# partie_entiere = decomposer(20,3)
# print(partie_entiere)

# ma_chaine = "Bonjour à vous"
# print(ma_chaine.split())
# # print("ce que devien ma chaine après la methode split: ",ma_chaine)
# print("".join(ma_chaine))

# flottant = input("Donner un floattant en exemple : ")

# if type(flottant) is not float:
#     raise TypeError("Le parametre doit etre un flottant")
# flottant = str(flottant)
# partie_entiere,partie_flottante = flottant.split(".")
# print(",".join([partie_entiere,partie_flottante[:3]]))

# def afficher_flottant(flottant):
#     """Fonction prenant en paramètre un flottant et renvoyant une chaîne de caractères représentant la troncature de ce nombre. La partie flottante doit avoir une longueur maximum de 3 caractères.

#     De plus, on va remplacer le point décimal par la virgule"""
    
#     if type(flottant) is not float:
#         raise TypeError("Le paramètre attendu doit être un flottant")
#     flottant = str(flottant)
#     partie_entiere, partie_flottante = flottant.split(".")
#     # La partie entière n'est pas à modifier
#     # Seule la partie flottante doit être tronquée
#     return ",".join([partie_entiere, partie_flottante[:3]])


# print(afficher_flottant("toto"))
     
# def afficher(*parametres,sep='',fin='\n'):

#     parametres = list(parametres)
#     return print(parametres)

# afficher("titi va a la plage")


# liste_origine = [0,1,2,3,4,5]
# calcul =[nb *nb for nb in liste_origine]
# print(calcul)

qtt_a_retirer = 7
fruits_stockes = [15,3,18,11]
sorti = [nb_fruits - qtt_a_retirer for nb_fruits in fruits_stockes if nb_fruits > qtt_a_retirer]
print(sorti)
    

        
