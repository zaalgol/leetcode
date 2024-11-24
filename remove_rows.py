import pandas as pd

# Load the CSV file into a DataFrame
input_file = "C:/code/tabular-wizard-server/datasets/semantic/MedicalReviews_280000.csv.csv"  # Replace with your CSV file name
output_file = "C:/code/tabular-wizard-server/datasets/semantic/MedicalReviews_280000_no_empty_ratings.csv"  # Replace with the desired output file name

# Read the CSV file
df = pd.read_csv(input_file)

# Filter the rows where 'rating' is not "No rating" and not blank
filtered_df = df[(df['Rating'] != "No rating") & (df['Rating'].notna()) & (df['Rating'] != "") & (df['Rating'] != "No rating available")]

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv(output_file, index=False)

print(f"Filtered rows saved to {output_file}")

