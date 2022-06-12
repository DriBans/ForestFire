# Importing the necessary libraries
from ast import increment_lineno
import datetime as dt
from enum import unique
from filecmp import cmp
from pickle import TRUE
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#% matplotlib inline

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv("C:/Bansal Data/Drishti Data/VS code/Python/ForestFire.py/forestfires.csv")
data.head()

data.value_counts()
data.shape
data.isnull().sum()
data.describe()
data.info()

data['area_km'] = data['area'] / 100
highestarea = data.sort_values(by = "area_km", ascending= True)
plt.figure(figsize= (8, 6))

plt.title("Temperature vs Area of fire")
plt.bar(highestarea['temp'], highestarea['area_km'])

plt.xlabel("Temperature")
plt.ylabel("Area per km-sq")
plt.show()

categorical_feature = data.describe(include=['O']).columns
print(categorical_feature)

plt.figure(figsize= (10, 5))
for idx, column in enumerate(categorical_feature):
    df = data.copy()
    unique = df[column].value_counts(ascending= True);
    plt.subplot(1, 2, idx+1)
    plt.title("Count of " + column)
    plt.bar(unique.index, unique.values)

plt.tight_layout()
plt.show()


plt.xlabel(column)
plt.ylabel("Number if" + column)
plt.figure(figsize= (10, 10))
sns.heatmap(data.corr(), annot= True, cmap= 'Blues', linewidths= 0.5)
