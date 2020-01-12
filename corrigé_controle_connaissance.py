#utilisation du split et if pour creer un code qui ne va afficher que les mots qui commenenct par "c" dans cette phrase
st = "Cet exercice consiste à afficher uniquement les mots qui commencent par la lettre c"
for mot in st.split():
    if mot[0] == 'c'or mot[0]=='C':
        print(mot)
    pass

#utiliser range() pour afficher les nombres pairs de 0 à 10
print(list(range(0,11,2)))

#utilisez la compréhension de liste pour creer la liste des nombres divisible par 3 compris entre 1 et 50.
liste2 = [x for x in range(1,51) if x%3 == 0]
print(liste2)

#dans la chaine suivante, vérifier le nombre de lettre de chaque mot et si celui-ci est pair, affichez le mot avec "pair !"
st= "affichez chaque mot de cette phrase dont le nombre de lettres est pair"

for mot in st.split():
    if len(mot) %2 == 0:
        print(mot + " <-- longueur paire !")

#ecrire un programme qui affiche les nombres entiers de 1 à 100. Pour les afficher les multiples de trois afficher "Fizz" à la place du nombre et pour
#les multiples de 5 imprimer "buzz". Pour les nombres qui sont multiples de 3 et 5 afficher "FizzBuzz"

for num in range(1,101):
    if num % 5 == 0 and num % 3 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
        
    else:
        print(num)

#compréhension de liste pour creer la liste des cinq premieres lettres de chaque mot dans la chaine ci-dessous:
st ="Création d'une liste des cinqu première lettres de chaque mot de cette chaine de caractères"
chaine = [mot[0:5] for mot in st.split()]
print(chaine)

  