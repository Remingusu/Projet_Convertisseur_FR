enter_base = int(input("Base d'entrée: "))
exit_base = int(input("Base de sortie: "))
nbr = int(input("Nombre à convertir en base", enter_base))

if enter_base is not 2 or 10 or 16 or exit_base is not 2 or 10 or 16:
    print("Cette base n'est pas conforme.")
