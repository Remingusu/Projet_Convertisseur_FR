numtoconvert = input("Enter a number to convert from base 16 to base 2 : ")

for num in numtoconvert:
    print(num)

print(f"Taille : {len(numtoconvert)}")
dico= {0: '0000',
       1: '0001',
       2: '0010',
       3: '0011',
       4: '0100',
       5: '0101',
       6: '0110',
       7: '0111',
       8: '1000',
       9: '1001',
       10: 'A',
       11: 'B',
       12: 'C',
       13: 'D',
       14: 'E',
       15: 'F'}
