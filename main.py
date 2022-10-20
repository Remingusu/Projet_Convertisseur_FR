loop=True
while loop: # boucle tant que loop est True
    enter_base = int(input("Base d'entrée (aucun effet): ")) # demande la base du nombre
    exit_base = int(input("Base de sortie (aucun effet): ")) # demande la base dans laquel le nombre va être converti
    if (enter_base != 2 and enter_base != 10 and enter_base != 16) or (exit_base != 2 and exit_base != 10 and exit_base != 16): # verifie si la base est 2, 10 ou 16
        print("Une des bases n'est pas conforme.") # si non, afficher la phrase
    else: # sinon
        loop=False # fin de la boucle
nbr = input(f"Nombre en base 16 à convertir en base 2: ") # demande le nombre

# Base 16 --> base 10
result = 0 # mettre result a 0
exposant = 0 # mettre exposant a 0
char_pos = -1 # mettre char_pos a -1
for i in range(len(nbr)): # ajouter 1 a i, le nombre de fois qu'il y a de caractère dans nbr
    code_char = ord(nbr[char_pos]) # récup code ascii décimal   
    if 65<=code_char<=70: # verif si le code_char est entre 65 et 70 (si c'est  une lettre)
        code_char = code_char - 55 # si oui, retirer 55 a code_char
        result += code_char * (16**exposant) # puis multiplier par 16**exposant le code_char-55
    elif 97<=code_char<=102:# verif si le code_char est entre 97 et 102 (si c'est  une lettre)
        code_char = code_char - 87 # si oui, retirer 87 a code_char
        result += code_char * (16**exposant) # puis multiplier par 16**exposant le code_char-87
    else: # sinon
        result += int(nbr[char_pos]) * (16**exposant) # multiplier par 16**exposant le caractère transformé en int() et l'ajouter a result (si c'est un nombre)
    exposant += 1 # ajouter un a l'exposant
    char_pos -= 1 # retirer 1 à char_pos

# Base 10 --> 2
binary="" # nombre binaire à 0
i=0 # i a 0
while result!=0: # tant que le résultat est différent de 0; si non, rien
    if i==4: # verif si i égale 4
        i=0 # si oui, i à 0
        binary=" "+binary # ajouter un espace
    if result%2==1:# verif si le résultat divisé par 2 à son reste égale à 1
        binary="1"+binary # si oui, ajouter 1 devant binary
    else: # sinon
        binary="0"+binary # ajouter 0 devant binary
    result=result//2 # diviser result par 2
    i+=1 # ajouter 1 a i

print("La conversion en base 2 est:", binary) # afficher le résultat binaire