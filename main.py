"""
loop=True
while loop: # boucle tant que loop est True
    enter_base = int(input("Base d'entrée (aucun effet): ")) # demande la base du nombre
    exit_base = int(input("Base de sortie (aucun effet): ")) # demande la base dans laquel le nombre va être converti
    if (enter_base != 2 and enter_base != 10 and enter_base != 16) or (exit_base != 2 and exit_base != 10 and exit_base != 16): # verifie si la base est 2, 10 ou 16
        print("Une des bases n'est pas conforme.") # si non, afficher la phrase
    else: # sinon
        loop=False # fin de la boucle
"""
nbr = input(f"Nombre en base 16 à convertir en base 2: ") # demande le nombre

result = 0
exposant=0
n = -1
for i in range(len(nbr)):
    code_char = ord(nbr[n])
    if 65<=code_char<=70 or 97<=code_char<=102:
        code_char=code_char-55
        result += code_char * (16**exposant)
    else:
        result += int(nbr[n]) * (16**exposant)
    print("Result:", result)
    exposant+=1
    n -= 1
print("Total:", result)