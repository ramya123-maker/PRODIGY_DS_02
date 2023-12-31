# -*- coding: utf-8 -*-
"""Task2 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WFg1yjZ9-2Gx0w1wtr2FxzVqVq5bv76O
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt     #for visualization
# %matplotlib inline
import seaborn as sns               #for visualization
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('https://raw.githubusercontent.com/arienugroho050396/Airline-Passenger-Satisfaction/main/airline_passenger_satisfaction.csv')
df

df.head().T

df.columns

df.shape

df.info()

df = df.drop_duplicates()
df.count()

df.isnull().sum()

df.info()

df.sample(5)

df['ID'].nunique()

df['Age'].nunique()

df.describe()

sns.boxplot(x = df['Age'])

plt.show()

print(df['Age'].max())

# Create a figure with a custom size
plt.figure(figsize=(12, 5))

# Set the seaborn theme to darkgrid
sns.set_theme(style='darkgrid')

# Create a histogram of the 'price' column of the Airbnb_df dataframe
# using sns distplot function and specifying the color as red
sns.distplot(df['Age'],color=('r'))

# Add labels to the x-axis and y-axis
plt.xlabel('Age', fontsize=14)
plt.ylabel('Density', fontsize=14)

# Add a title to the plot
plt.title('Distribution of  Age',fontsize=15)

corr = df.corr()

# Display the correlation between columns
corr

# Set the figure size
plt.figure(figsize=(12,6))

# Visualize correlations as a heatmap
sns.heatmap(corr, cmap='BrBG',annot=True)

# Display heatmap
plt.show()

sns.pairplot(df)

# show the plot
plt.show()