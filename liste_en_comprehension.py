
liste = [x for x in 'exemple']
print (liste)

liste2 = [x**2 for x in range(0,11)]
print(liste2)

# possibilite de mettre des conditions dans la liste
liste2 = [x**2 for x in range(0,11) if x%2 == 0]
print(liste2)

celsius = [0,10,20.1,34.5]
farenheit = [((9/5)*temp + 32) for temp in celsius ]
print(farenheit)

#imbriqué une liste de compréhension
lst = [x**2 for x in [x**2 for x in range(11)]]
print (lst)


