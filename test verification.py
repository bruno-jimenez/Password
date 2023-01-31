# create the list for all input for pwd 

alphabet_min=[chr(i) for i in range(ord('a'),ord('z')+1)]
alphabet_maj=[chr(i) for i in range(ord('A'),ord('Z')+1)]
chiffres = [ chr(i) for i in range(48,58) ]
caracteres_speciaux = [ '%' , '_' , '-' , '!' , '$' , '^' , '&' , '#' , '(' , ')' , '[' , ']' , '=' , '@']

spc=input("do you want special caractere in your pwd ? Y/N ")

if "Y" in spc:
    print(alphabet_min)
    print(alphabet_maj)
    print(chiffres)
    print(caracteres_speciaux)

if "N" in spc:
    print(alphabet_min)
    print(alphabet_maj)
    print(chiffres)
    