# Dictionnaire (table de hashage voir tableau associatif) pour les dico on met des parenthèse {}
mon_dict = {'clef1':"premiere valeur",'clef2':"seconde valeur"}
print (mon_dict)
# on accède a l'element que l'on souhaite
print (mon_dict['clef2'])
mon_dict = {'clef1':123,'clef2':[12,23,64],'clef3':['item1','item2','item3']}
#on accede à la clef3 de mon dictionnaire
print (mon_dict['clef3'])
#on peut acceder à un element particulier de la clef 3
print (mon_dict['clef3'][1])
#on peut appliquer des methode au dico
print (mon_dict['clef3'][1].upper())
#on peut faire des calcul 
mon_dict['clef1'] = mon_dict['clef1'] - 23
print (mon_dict['clef1'])

# on peut initialiser un dictionnaire vide en mettant un simple {}
d = {}
#on assigne une clef
d['reponse'] = 'chien'
print (d)
d['nombre'] = '1966'
print (d)

#Méthode dans les dico
c = {'c1':1,'c2':2,'c3':3}
print (c)
print(c.keys())
print(c.values())
print(c.items())


