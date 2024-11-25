
#seaborn xisualization library 

import seaborn as sns 
import matplotlib.pyplot as plt 
# Load the built-in tips dataset 
dataset = sns.load_dataset('tips') 
# Setting style for the plot 
sns.set_style('whitegrid') 
# Creating a simple regression plot 
sns.lmplot(x='total_bill', y='tip', data=dataset) 
# Customizing the plot with 'hue' to show different categories for 'sex' 
sns.lmplot(x='total_bill', y='tip', data=dataset, hue='sex', markers=['o', 'v']) 
# Customizing further with marker size and color palette 
sns.lmplot(x='total_bill', y='tip', data=dataset, hue='sex', markers=['o', 'v'], 
scatter_kws={'s':200}, palette='plasma') 
plt.show()
