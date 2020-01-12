l = [1,2,3,4,5,6,7,8,9,10]
for numero in l:
    print("ceci est le numéro %i" % numero)


divisible = [1,2,3,4,5,6,7,8,9]
for num in divisible:
    if num % 2 == 0 :
        print("le numéro %i est pair" % num)


compteur = 0
for numero in l:
    compteur = compteur + numero

print("Somme Totale %i" % compteur)


for lettre in 'Une chaine de caractère':
    print(lettre)

#avec un tuple
tup = (1,2,3,5)
for t in tup:
    print(t)

#avec une liste de tuple
l = [(1,2),(3,4),(4,5)]
for tup in l:
    print(tup)


# On peut extraire le premiere element de chaque liste de 2
for (m,n) in l:
    print(m)


# affiche que les clé de la liste dico
d = {'c1':1,'c2':2,'c3':3}
for item in d:
    print(item)

#si on veut afficher la cle et la valeur il va falloir utiliser une methode. c et v represente la cle et la valeur. ici on affiche sur une ligne
for c, v in d.items():
    print(c,end=" "); print(v)
    print ("{} --> {}".format(c,v) )
    
