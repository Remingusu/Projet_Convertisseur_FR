loop=True
while loop: # boucle tant que loop est True
    enter_base = int(input("Base d'entrée (aucun effet): ")) # demande la base du nombre
    exit_base = int(input("Base de sortie (aucun effet): ")) # demande la base dans laquel le nombre va être converti
    if (enter_base != 2 and enter_base != 10 and enter_base != 16) or (exit_base != 2 and exit_base != 10 and exit_base != 16): # verifie si la base est 2, 10 ou 16
        print("Une des bases n'est pas conforme.") # si non, afficher la phrase
    else: # sinon
        loop=False # fin de la boucle
nbr = input(f"Nombre en base 16 à convertir en base 2: ") # demande le nombre
