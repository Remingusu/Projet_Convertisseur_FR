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