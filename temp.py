

# # Step 2: Load the Dataset
# from datasets import load_dataset

# # Load the French Wikipedia dataset (20220301.fr)
# dataset = load_dataset("wikipedia", "20220301.fr",  trust_remote_code=True)

# # Step 3: Save the Dataset Locally
# import pandas as pd

# # Convert the dataset to a pandas DataFrame
# df = pd.DataFrame(dataset['train'])

# # Save the DataFrame to a CSV file
# df.to_csv('wikipedia.csv', index=False)
import os
# os.environ['JAVA_HOME'] = "C:\\Program Files\\OpenLogic\\jdk-8.0.422.05-hotspot"
print(os.environ['JAVA_HOME'])