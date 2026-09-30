#10
mySet = set('ATGTGGG')
mySet2 = {'ATGCCT'}

# A forma de criar o conjunto é importante, pois impacta diretamente na interpretação do python referente ao conjunto.
# Se for criado com chaves, o python entende que é um conjunto de strings,
# e se for criado com a função set(), o python entende que é um conjunto de caracteres.

#11
Set_A = set(3 14 15 9 26 5 35 9)
Set_B = set(60 22 14 0 9)

print(Set_A | Set_B) # União entre os conjuntos A e B
print(Set_A - Set_B) # Diferença entre os conjuntos A e B
print(Set_A, Set_B) # Interseção entre os conjuntos A e B
print(Set_A ^ Set_B) # Diferença simétrica entre os conjuntos A e B

