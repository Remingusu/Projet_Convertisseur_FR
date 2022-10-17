loop=True
while loop:
    enter_base = int(input("Base d'entrée (aucun effet): ")) # demande la base du nombre
    exit_base = int(input("Base de sortie (aucun effet): ")) # demande la base dans laquel le nombre va être converti
    if (enter_base != 2 and enter_base != 10 and enter_base != 16) or (exit_base != 2 and exit_base != 10 and exit_base != 16):
        print("Une des bases n'est pas conforme.") # si non, afficher la phrase
    else:
        loop=False
    
print('test')