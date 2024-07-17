# %%
import pandas

df = pandas.read_csv("results.csv")
column_names = df.columns
df_by_process = df.groupby([column_names[0], column_names[1]]).mean()

print(df_by_process)
# %%
