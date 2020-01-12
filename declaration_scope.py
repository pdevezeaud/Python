x = 25

def afficher():
    x = 50
    return x


print(x)
print (afficher())
print(x)

# régles LEGB
# lOCAL, enclosing, Global

f =  lambda x:x**2
print (f)


nom = "Je suis global"
def bienvenue():
    nom = "sammy"

    def bonjour():
        print("bonjour "+ nom)
    


    print(bonjour())
print(bienvenue())


x = 50

def fonction():
    global x
    print("x vaut ",x)
    x = 2
    print("valeur de x ", x)

print("x vaut avant ",x)
print(fonction())
print("x vaut maintenant ",x)


