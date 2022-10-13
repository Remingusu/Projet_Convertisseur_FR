enter_base = int(input("Base d'entrée: "))
exit_base = int(input("Base de sortie: "))
nbr = int(input("Nombre à convertir en base", enter_base))

if not enter_base==2 or not enter_base==10 or not enter_base==16:
    print("Cette base n'est pas conforme.")
