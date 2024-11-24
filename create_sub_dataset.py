import pandas as pd

# File paths
input_file = r'C:/code/tabular-wizard-server\datasets\semantic/MedicalReviews_280000_no_empty_ratings.csv'
output_file = r'C:/code/tabular-wizard-server\datasets\semantic/MedicalReviews_last_10_rows.csv'

# Read the CSV file
df = pd.read_csv(input_file)

# Select the last 10 rows (including headers)
last_10_rows = df.tail(10)

# Save the result to a new file
last_10_rows.to_csv(output_file, index=False)

print(f"The last 10 rows have been saved to {output_file}")
