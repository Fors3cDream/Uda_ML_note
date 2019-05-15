"""
Create by Killer at 2019-05-08 14:15
"""

import pandas as pd
import numpy as np

data = pd.read_csv("data.csv")

# TODO: Separate the features and the labels into arrays called X and y

X = np.array(data[['x2', 'x2']])

y = np.array(data['y'])

print("X: ", X)
print("y: ", y)