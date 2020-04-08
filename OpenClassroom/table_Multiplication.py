# def table(nb):

#     i = 0
#     while i < 10: # tant que i est strictement inferieure à 10.
#         print(i + 1, "*",nb,"=",(i+1)*nb)
#         i += 1 #on incremente i de 1 à chaque tour
# table(2)

# version avec le choix du chiffre multipliant x

def table(nb,max):
    i=0
    while i < max:
        print(i + 1, "*",nb,"=",(i+1)*nb)
        i += 1 #on incremente i de 1 à chaque tour

table(2,20)
        