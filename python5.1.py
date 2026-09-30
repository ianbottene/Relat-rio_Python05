# 1
fav = {"Livro":"Percy Jackson", "Som": "Got to be real", "Árvore": "Laranjeira"}

#2
print(fav["Livro"])

#3
fav_thing = 'Livro'
print(fav[fav_thing])

#4
print(fav["Árvore"])

#5
fav["Organismo"] = "Xanthomonas"

fav_thing = 'Organismo'
print(fav[fav_thing])

#6
print("As opções são: Livro, Som, Árvore, Organismo",)
chave  = input("Digite uma opção: ")
print(fav[chave])

#7
fav['Organismo'] = 'HLB'

#8
fav_thing = chave
print("Meu novo item favorito é:",fav[fav_thing])

#9
for item in fav:
    print(item, fav[item])