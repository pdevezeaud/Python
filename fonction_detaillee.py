

def est_premier (num):
    '''
    Fonction simple pour determiner si un nombre est premier
    parametre : num, le nombre à tester
    on par de 2 jusqu'au numero entré (num). Utilisation du range dans ce cas.
    '''
    for n in range(2,num):
        if num % n == 0:
            print("Il n'est pas premier")
            '''
            on sort du test car n'est plus divisible
            '''
            break
    else:
        print("est premier")

pass

est_premier(16)



import math
def est_premier_elabo (nume):
    '''
 Fonction plus elaborée pour determiner si un nombre est premier
 param : num le nombre à tester
 utilisation de la bibliotheque Math
 renvoi un boleen
 false n'est pas premier
 true le nombre est premier

    '''
    if nume % 2 == 0 and nume > 2:
        return False
    for n in range(3, int(math.sqrt(nume))+1, 2):
        if nume % n == 0:
            return print(False)
    return print(True)

est_premier_elabo(16)

        