enter_base = int(input("Base d'entrée: ")) # demande la base du nombre
exit_base = int(input("Base de sortie: ")) # demande la base dans laquel le nombre va être convertis
nbr = input(f"Nombre à convertir en base {enter_base}: ") # demande le nombre
num_bin = "" # def 'num_bin' pour qu'il ne soit pas indéfini

if (enter_base != 2 or 10 or 16) or (exit_base != 2 or 10 or 16):
    print("Cette base n'est pas conforme.") # afficher la phrase

dico={ '0': '0000',
       '1': '0001',
       '2': '0010',
       '3': '0011',
       '4': '0100',
       '5': '0101',
       '6': '0110',
       '7': '0111',
       '8': '1000',
       '9': '1001',
       'A': '1010',
       'B': '1011',
       'C': '1100',
       'D': '1101',
       'E': '1110',
       'F': '1111' } # définition du dictionnaire (chaque caractère de l'hexa est définie en base 2)

for i in range(len(nbr)): # boucle 'for' de la taille du nombre donner au départ
    index = nbr[i] # def 'index' avec le charactère du nombre du début par rapport à l'incrémentation
    if 97 <= ord(index) <= 122: # verification si le code décimal ascci du charactère est entre 97 et 122 (charactères minuscules)
        index = chr(ord(index)-32) # si oui, on retire 32 pour mettre le charactère en majuscule
        num_bin = num_bin + dico[index] + " " # concaténation du code binaire précédent avec le code binaire du characètre dont la valeur est définie dans le dictionnaire
    elif 48 <= ord(index) <= 57 or 65 <= ord(index) <= 90: # vérification si le charactère est entre 48 et 57 ou 65 et 90 (majuscule ou nombre)
        num_bin = num_bin + dico[index] + " " # concaténation du code binaire précédent avec le code binaire du characètre dont la valeur est définie dans le dictionnaire

print("Nombre converti en base 2:", num_bin) # afficher la phrase + le nombre converti