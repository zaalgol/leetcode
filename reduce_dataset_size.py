import pandas as pd

# Read the CSV file
df = pd.read_csv('wikipedia.csv')

num_rows = int(0.1 * len(df))

# Get the first 10% of the rows
df_first_10_percent = df.iloc[:num_rows]
df_first_10_percent.to_csv('df_first_10_percent.csv')