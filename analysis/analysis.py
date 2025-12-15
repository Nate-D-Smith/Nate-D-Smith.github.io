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

list(df.columns)

list(df.province.unique())

def danger_score(province_choice):
    nkill_since_2000 = (
        df.loc[(df['year'] >= 2000) & (df['province'] == province_choice), 'nkill']
        .sum(skipna=True)
    )

    nkill_since_2015 = (
        df.loc[(df['year'] >= 2015) & (df['province'] == province_choice), 'nkill']
        .sum(skipna=True)
    )

    attacks_since_2000 = (
        df.loc[(df['year'] >= 2000) & (df['province'] == province_choice), 'eventid']
        .count()
    )

    attacks_since_2015 = (
        df.loc[(df['year'] >= 2015) & (df['province'] == province_choice), 'eventid']
        .count()
    )

    avg_nkill_since_2000 = ((
        df.loc[(df['year'] >= 2000), 'nkill']
        .sum(skipna=True)
        ) / 34)

    avg_nkill_since_2015 = ((
        df.loc[(df['year'] >= 2015), 'nkill']
        .sum(skipna=True)
        ) / 34)

    avg_attacks_since_2000 = ((
        df.loc[(df['year'] >= 2000), 'eventid']
        .count()
        ) / 34)

    avg_attacks_since_2015 = ((
        df.loc[(df['year'] >= 2015), 'eventid']
        .count()
        ) / 34)

    score = (((nkill_since_2000/avg_nkill_since_2000) +
            (nkill_since_2015/avg_nkill_since_2015) +
            (attacks_since_2000/avg_attacks_since_2000) +
            (attacks_since_2015/avg_attacks_since_2015)) / 26 * 100)

    return score

danger_score('Gao')

provinces = (
    df['province']
      .dropna()
      .astype(str)
      .str.strip()
      .unique()
)

scores = (
    pd.DataFrame({'province': provinces})
      .assign(score=lambda x: x['province'].apply(danger_score))
)

scores.loc[scores['score'].idxmax()]

print(scores)

df.loc[(df['province'] == 'Bamako') &
       (df['year'] >= 2015), 'nkill'].count()
df.loc[(df['province'] == 'Bamako') &
       (df['year'] >= 2015), 'nkill'].sum()
