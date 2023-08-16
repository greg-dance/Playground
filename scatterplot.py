
# Goal: To import the sample dataset. Visualize the tips by total bill and sex of customer
# Import the modules
import seaborn as sns
import matplotlib.pyplot as plt

# Create some example data
tips = sns.load_dataset("tips")

# Pretty style
sns.set_style("darkgrid")

# Create a scatter plot using Seaborn
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex", palette="flare")

# Add labels and title
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Total Bill vs Tip")

# Show the plot
plt.show()