
# Load packages used for data manipulation and visualization.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotx as mpx
import os

# Load machine learning (AI) tools used to create predictive models (I plan on doing more with this soon)
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, precision_score, 
f1_score, r2_score, confusion_matrix, ConfusionMatrixDisplay)

# Load the dataset I previously cleaned (the uncleaned version is too large for GitHub)
df = pd.read_csv('C:/Users/nates/OneDrive/BYUI-NateHP/DATA PROJECTS/Projects/Upcoming Projects/sahel_terrorism/data/cleaned_gtd.csv')
# Add date column to help with line graphs
df['date'] = pd.to_datetime(dict(year=df.year, month=df.month, day=df.day), errors='coerce')
df.rename(columns={'approxdate': 'date_range'}, inplace=True)
df['date'] = pd.to_datetime(df['date'], errors='coerce')
# Checking if it worked
df.shape
list(df.columns)
df.date.unique()[:20]

# Adjusting working directory
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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

# Changing perameters to comply with CSS style 
plt.rcParams.update({
    "font.family": "Arial",
    "figure.facecolor": "none",  
    "axes.facecolor": "none",
    "axes.edgecolor": "black",
    "axes.labelcolor": "black",
    "text.color": "black",
    "xtick.color": "black",
    "ytick.color": "black",
    "grid.color": (0, 0, 0, 0.15), # subtle grid
    "grid.linewidth": 0.8,
})


# 3 month rolling average nkills graph for countries since 2000

# Cut the data to only include attacks after 2005
df_2005 = df[(df['date'] < '2020-03-01') & 
             (df['date'] > '2005-01-01')]

# Group data by monthly deaths
monthly = (df_2005.groupby([pd.Grouper(key='date', freq='MS'),
                            'country'])['nkill']
                            .sum().reset_index())

# Create 3 month rolling average
monthly["deaths_3mo_avg"] = (
    monthly
    .sort_values("date")
    .groupby("country")["nkill"]
    .transform(lambda x: x.rolling(window=3, min_periods=1).mean())
)

# Create plot for all 3 countries
fig, ax = plt.subplots(figsize=(10.5, 4.8))

sns.lineplot(
    data=monthly,
    x="date",
    y="deaths_3mo_avg",
    hue="country",
    linewidth=2.5,
    ax=ax
)
# Set axis titles
ax.set_title("3-Month Rolling Average of Deaths (2005–2020)", pad=12)
ax.set_xlabel("")
ax.set_ylabel("Deaths (3-mo avg)")

# Adjust grid style
ax.grid(True, axis="y")
ax.grid(False, axis="x")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
leg = ax.legend(title="", frameon=False, ncol=3, loc="upper left")

# Save graph as an svg file in the project
fig.tight_layout()
fig.savefig("jnim_3mo_avg.svg", bbox_inches="tight")
plt.show()

# Now time for the regional graphs

# Create a custom function that asks for Province (region) name
def graph(province):

    # Cut data for after 2005
    df_province = df.loc[
        (df["date"] >= "2005-01-01") &
        (df["date"] <  "2020-03-01") &
        (df["province"] == province)
    ].copy()

    # Get monthly data
    monthly = (
        df_province
        .groupby(pd.Grouper(key="date", freq="MS"))["nkill"]
        .sum()
        .reset_index(name="nkill")
    )

    # Create 3 month rolling average
    monthly["deaths_3mo_avg"] = monthly["nkill"].rolling(window=3, min_periods=1).mean()

    # Create graph size
    fig, ax = plt.subplots(figsize=(10.5, 4.8))

    # Create lineplot
    sns.lineplot(
        data=monthly,
        x="date",
        y="deaths_3mo_avg",
        linewidth=2.5,
        ax=ax
    )

    # Set axis labels
    ax.set_title(f"{province} — 3-Month Rolling Average of Deaths (2005–2020)", pad=12)
    ax.set_xlabel("")
    ax.set_ylabel("Deaths (3-mo avg)")

    # Adjust grid styles
    ax.grid(True, axis="y")
    ax.grid(False, axis="x")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Save graph as svg file in the project
    fig.tight_layout()
    fig.savefig(f"static/images/charts/{province.lower()}_3mo_avg.svg", bbox_inches="tight")
    plt.show()

# Used as a reference for province names
list(df.loc[df['country'] == 'Mali', 'province'].unique())

# Run the above custom function "graph()" for each applicable region
# All graphs are now saved to the project to be referenced in HTML files
graph('Centre')
graph('Tahoua')
graph('Zinder')
graph('Gao')
graph('Unknown')
graph('Agadez')
graph('Niamey')
graph('Timbuktu')
graph('Mopti')
graph('Tillaberi')
graph('Iferouane')
graph('Maradi')
graph('Dosso')
graph('Bamako')
graph('Diffa')
graph('Kidal')
graph('Tanout Department')
graph('Agadez Department')
graph('Niamey Capital District')
graph('Segou')
graph('Tillabéri')
graph('Kayes')
graph('Sahel')
graph('Sikasso')
graph('Koulikoro')
graph('Centre-Nord')
graph('Haut-Bassins')
graph('Menaka')
graph('Boucle du Mouhoun')
graph('Nord')
graph('Est')
graph('Centre-Est')
graph('Sud-Ouest')
graph('Cascades')
graph('Centre-Sud')