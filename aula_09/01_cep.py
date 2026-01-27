# %%
import requests #para realizar requisições na web
import json #para tratar json de lista/dicionarios para arquivos.
from tqdm import tqdm  #barra de progresso como fosse loading.
import pandas as pd

cep = ["25065160","25080-700","25065-260","25051-100"]

url = "https://viacep.com.br/ws/{cep}/json/"
dados=[]

for i in tqdm(cep):
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())
dados

# %% criar tipo uma panilha no excel utilizando o pandas.

dataset = pd.DataFrame(dados)
dataset.to_csv("cep.cvs", sep=';')


# %% Salvando o arquivo em json
with open("cep.json", "w", encoding='utf-8') as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)

# %%



