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


# Set graph themes

BG = "#F4E7D3"
ACCENT = "#b75447"  

sns.set_theme(style="white", context="talk")

plt.rcParams.update({
    "font.family": "Arial",
    "figure.facecolor": "none",   # important for transparent export
    "axes.facecolor": "none",
    "axes.edgecolor": "black",
    "axes.labelcolor": "black",
    "text.color": "black",
    "xtick.color": "black",
    "ytick.color": "black",
    "grid.color": (0, 0, 0, 0.15), # subtle grid
    "grid.linewidth": 0.8,
})


# Create 3 month rolling average nkills graph for countries since 2000

df_2000 = df[(df['date'] < '2020-03-01') & 
             (df['date'] > '2000-01-01')]

monthly = (df_2000.groupby([pd.Grouper(key='date', freq='MS'),
                            'country'])['nkill']
                            .sum().reset_index())

monthly["deaths_3mo_avg"] = (
    monthly
    .sort_values("date")
    .groupby("country")["nkill"]
    .transform(lambda x: x.rolling(window=3, min_periods=1).mean())
)

plt.figure(figsize=(12, 6))

sns.lineplot(
    data=monthly,
    x="date",
    y="deaths_3mo_avg",
    hue="country"
)

plt.title("3-Month Rolling Average of Conflict Deaths (2000–2020)")
plt.xlabel("Year")
plt.ylabel("Deaths (3-Month Rolling Avg)")
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(10.5, 4.8))

sns.lineplot(
    data=monthly,
    x="date",
    y="deaths_3mo_avg",
    hue="country",
    linewidth=2.5,
    ax=ax
)

ax.set_title("3-Month Rolling Average of Deaths (2000–2020)", pad=12)
ax.set_xlabel("")
ax.set_ylabel("Deaths (3-mo avg)")

ax.grid(True, axis="y")   # usually enough; keeps it clean
ax.grid(False, axis="x")

# Clean spines to match your site’s minimalist boxes
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

leg = ax.legend(title="", frameon=False, ncol=3, loc="upper left")

fig.tight_layout()
plt.show()

fig.savefig("jnim_3mo_avg.svg", bbox_inches="tight")

fig.savefig("static/images/charts/countries_3mo_avg.png", bbox_inches="tight", transparent=True, dpi=300)
