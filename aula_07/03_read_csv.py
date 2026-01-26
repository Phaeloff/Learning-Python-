# %%
nome_arquivo= "data.csv"

with open(nome_arquivo) as open_file:
    lines = open_file.readlines()


for l in lines:
    print(l)

# %%

dados = dict()

chaves = lines[0].strip("\n").split(";")
for c in chaves:
    dados[c] = []

# %%

for l in lines[1:]:

    valores = l.strip("\n").split(",")

    for i in range(0, len(valores)):

        dados[chaves[i]].append(valores[i])

dados

# %%

idade = []
for i in dados["idade"]:
    idade.append(int(i))

media = sum(idade)/ len(idade)

media
# %%
