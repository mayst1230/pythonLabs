import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option("display.precision", 2)

volume = 'Объем двигателя'
numberSeats = 'Кол-во сидений'
upToOneHundred = 'ускорение 0/100'
fuelConsumption = 'Расход топлива'

table = pd.read_csv('dataNormal.csv')

x = np.array(table[volume]).reshape((-1, 1))
y = np.array(table[upToOneHundred])

model = LinearRegression()
model.fit(x, y)
r_sq = model.score(x, y)

print('coefficient of determination: ', r_sq)