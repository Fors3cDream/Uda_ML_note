"""
Create by Killer at 2019-05-31 17:09
"""

import pandas as pd
from sklearn.linear_model import LinearRegression

bmi_life_data = pd.read_csv('bmi_and_life_expectancy.csv')

bmi_life_model = LinearRegression()
bmi_life_model.fit(bmi_life_data[['BMI']], bmi_life_data[['Life expectancy']])

predict_bmi = [[21.07931]]

laos_life_exp = bmi_life_model.predict(predict_bmi)

print(laos_life_exp)