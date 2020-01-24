import pandas as pd

file_name = "myZipPopulations.csv"
df = pd.read_csv(file_name,delimiter=',').dropna()
df["population"].sum()
