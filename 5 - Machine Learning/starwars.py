#%%
import pandas as pd


df = pd.read_parquet('data/dados.clones.parquet')

df['General Jedi encarregado'].unique()

df.shape
