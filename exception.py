# try:

#     for i in ['a','b','c']:
#         i = int(i)
#         print (i**2)
# except TypeError:
#     print("Une erreur s'est produite ! ")



# def demande():
#     while True:
#         try:
#             n = int(input("Entrer un entier: "))
#         except:
#             print("Merci d'entre un entier a nouveau")
#             continue
#         else:
#             break
#     print("le nombre au carré est : ",n**2)

# demande()

ttc = lambda prixHT:prixHT +(prixHT * 20/100)
print(ttc(24))
