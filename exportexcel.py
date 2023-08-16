import seaborn as sns
import pandas as pd

# Load the dataset
tips = sns.load_dataset("tips")

# Export the dataset to an Excel file
output_file = "tips_dataset.xlsx"
tips.to_excel(output_file, index=False)

print(f"Tips dataset exported to {output_file}")