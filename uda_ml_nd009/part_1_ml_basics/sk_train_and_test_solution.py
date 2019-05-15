"""
Create by Killer at 2019-05-08 14:43
"""

# Reading the csv file
import pandas as pd

data = pd.read_csv("data.csv")

# Spliting the data into X and y
import numpy as np

X = np.array(data[['x1', 'x2']])
y = np.array(data['y'])

# Import statement for train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)