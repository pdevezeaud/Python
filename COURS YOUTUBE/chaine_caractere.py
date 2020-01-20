'''
Une methode de chaine travaille sur une copie, et pas sur la chaine elle même.

str.upper(),str.lower(),str.capitalizaze(), str.title()
str.center(<largeur>, <Caractere de remplissage>)
str.find(<chaine>,<debut>,<fin>)
str.index(<chaine>,<debut>,<fin>)
str.replace(<ancienne>,<nouvelle>)

str.isalpha(), str.isdigit(), str.isdecimal(), str.isnumeric(), str.isalphanume()

'''
# ma_chaine = "BLACK JACK"
# print(ma_chaine)
# print(ma_chaine.find("JACK"))

# ma_chaine = ma_chaine.center(90,"-")
# print(ma_chaine)

phrase = "Magicien|10|5"
print(phrase.split("|"))

ch = "Le langage Python"
if "Langage" in ch:
    print("Trouvé")
else:
    print("Non trouvé")


