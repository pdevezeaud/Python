t=(4,1,5,2,3,9,7,2,8)
print(t)
print(t[2:3])
t +=(10,) #concenation
print(t)
print(len(t))
ch ='trou du cul'
st = tuple(ch)
print(st)
print("*******************************************")

'''
(!) Tuple : conteneur imuable (dont on ne peut modifier les valeurs)
création de tupe : mon_tuple = ()      #vide
                   mon_tuple = 17      #avec une valeurs
                   mon_tuple = (4,17)  #plusieurs valeurs

raisons d'utiliser les tuples : affectation multiple de variable
                                retour multiple de fonction

'''
