import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotx as mpx

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, precision_score, 
f1_score, r2_score, confusion_matrix, ConfusionMatrixDisplay)

df = pd.read_csv('C:/Users/nates/OneDrive/BYUI-NateHP/DATA PROJECTS/Projects/Upcoming Projects/sahel_terrorism/data/cleaned_gtd.csv')
df['date'] = pd.to_datetime(dict(year=df.year, month=df.month, day=df.day), errors='coerce')
df.rename(columns={'approxdate': 'date_range'}, inplace=True)
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df.shape
list(df.columns)
df.date.unique()[:20]

 # Total Killings per Year by Country
sns.set_style('ticks')
plt.figure(figsize=(12,6))
sns.lineplot(
    data=df, 
    x='year', 
    y='nkill', 
    linewidth=2.5,  
    hue='country', 
    estimator='sum',
    ci=None, 
)
plt.title('Total Killings per Year by Country', fontsize=18, pad=15)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Total Killings', fontsize=14)
plt.legend(title='Country')
plt.show()
