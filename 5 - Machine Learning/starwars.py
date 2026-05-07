#%%
import pandas as pd


df = pd.read_parquet('data/dados.clones.parquet')

df['General Jedi encarregado'].unique()


#

from sklearn import tree
tree.plot_tree(max_depth=3)
