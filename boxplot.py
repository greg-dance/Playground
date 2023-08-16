
# Goal: to visualize the effects of time of day on tips

# Import the modules
import seaborn as sns
import matplotlib.pyplot as plt
#this is for the read_excel method
import pandas as pd

# Import the sample data from excel
tips = pd.read_excel("tips_dataset.xlsx")

# Make it look nice
sns.set_style("darkgrid")

# Create a box plot using Seaborn
sns.boxplot(data=tips, x="time", y="tip", palette="Spectral")

# Add labels and title
plt.xlabel("Time of day")
plt.ylabel("Tip Amount ($)")
plt.title("Tips by Time of Day")

# Show the plot
plt.show()