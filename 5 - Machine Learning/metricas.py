# %%

import pandas as pd

df = pd.read_csv('data/dados2.csv')

# %%
df = df.replace({"Sim":1 , "Não":0} )

#lista de variaveis numericas
num_vars=[
    'Curte games?',
    'Curte futebol?',
    'Curte livros?',
    'Curte jogos de tabuleiro?',
    'Curte jogos de fórmula 1?',
    'Curte jogos de MMA?',
    'Idade',
]

#converter de texto para numero
dummy_vars =[
    "Como conheceu o Téo Me Why?",
    "Quantos cursos acompanhou do Téo Me Why?",
    "Estado que mora atualmente",
    "Área de Formação",
    "Tempo que atua na área de dados",
    "Posição da cadeira (senioridade)",
]

# cria uma variavel por variavel separadamente.
df_analise= pd.get_dummies(df[dummy_vars]).astype(int)
df_analise [num_vars] = df[num_vars].copy()


df_analise['uma pessoa feliz?'] = df['Você se considera uma pessoa feliz?'].copy()
df_analise

# %%
features = df_analise.columns[:-1].tolist()
x = df_analise[features]
y = df_analise['uma pessoa feliz?']

from sklearn import tree


arvore = tree.DecisionTreeClassifier(random_state=42,
                                    min_samples_leaf=5,
                                    )

arvore.fit(x, y)


# %%

arvore_predict = arvore.predict(x)
arvore_predict

df_predict = df_analise[['uma pessoa feliz?']]
df_predict['predict_arvore'] = arvore_predict
df_predict

# %%

(df_predict['uma pessoa feliz?'] == df_predict['predict_arvore']).mean()


