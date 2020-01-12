tableau = list(range(10))
print (tableau)

start = 0
stop = 20
x = range(start,stop)
print(x)
print(list(x))

#on peut définir un pas dans la liste
x = range(start,stop,2)
print(list(x))

#on peut boucler sur un range
for num in range(10):
    print (num)