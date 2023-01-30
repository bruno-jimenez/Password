from json import *

# create the list for all input for pwd generator

alphabet_min=[chr(i) for i in range(ord('a'),ord('z')+1)]
alphabet_max=[chr(i) for i in range(ord('A'),ord('Z')+1)]
chiffres = [ chr(i) for i in range(48,58) ]
caracteres_speciaux = [ '%' , '_' , '-' , '!' , '$' , '^' , '&' , '#' , '(' , ')' , '[' , ']' , '=' , '@']

print(alphabet_min)
print(alphabet_max)
print(chiffres)
print(caracteres_speciaux)

