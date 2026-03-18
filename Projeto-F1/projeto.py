# %%

import pandas as pd


results = pd.read_csv("data/results.csv")
races = pd.read_csv("data/races.csv")
pitstops = pd.read_csv("data/pit_stops.csv")

# %%

results

# %%
pit_count = pitstops.groupby("driverId").size()

pit_count = pit_count.reset_index()
pit_count.columns = ["driverId", "total_pitstops"]

print(pit_count.head())