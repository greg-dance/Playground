# Goal: to show the average tip amount by day of week as a percentage of the total bill

# Import the modules
import seaborn as sns
import matplotlib.pyplot as plt
#this is for the read_excel method
import pandas as pd

# Import the sample data from excel
tips = pd.read_excel("tips_dataset.xlsx")

# Calculate percentage tip and add it as a new column
tips["percentage_tip"] = (tips["tip"] / tips["total_bill"]) * 100

# Make it look nice
sns.set_style("darkgrid")

# Create a bar plot using Seaborn
sns.barplot(data=tips, x="day", y="percentage_tip", palette="pastel")

# Add labels and title
plt.xlabel("Day of Week")
plt.ylabel("Tip Amount (%)")
plt.title("Tips by Day of Week")

# Show the plot
plt.show()