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

# Base 16 --> base 10
result = 0 # mettre result a 0
exposant = 0 # mettre exposant a 0
char_pos = -1 # mettre char_pos a -1
for i in range(len(nbr)): # ajouter 1 a i, le nombre de fois qu'il y a de caractère dans nbr
    code_char = ord(nbr[char_pos]) # récup code ascii décimal c
    if 65<=code_char<=70 or 97<=code_char<=102: # verif si le code_char est entre 65 et 70 ou 97 et 102
        code_char = code_char - 55 # si oui, retirer 55 a code_char
        result += code_char * (16**exposant) # puis multiplier par 16**exposant le code_char-55
    else: # sinon
        result += int(nbr[char_pos]) * (16**exposant) # multiplier par 16**exposant le caractère transformé en int() et l'ajouter a result
    exposant += 1 # ajouter un a l'exposant
    char_pos -= 1 # retirer 1 à char_pos

# Base 10 --> 16
binary=""
i=0
while result!=0:
    if i==4:
        #i=0
        #binary=" "+binary
        if result%2==1:
            binary="1"+binary
            result=result//2
        else: # sinon
            binary="0"+binary
            result=result//2
    #i+=1

print("La conversition en base 2 est:", binary)