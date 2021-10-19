import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns

volume = 'volume'
numberSeats = 'number_seats'
upToOneHundred = 'up_to_one_hundred'
fuelConsumption = 'fuel_consumption'

table = pd.read_csv('dataNormal.csv')

x = np.array(table[volume]).reshape((-1, 1))
y = np.array(table[upToOneHundred])

model = LinearRegression()
model.fit(x, y)
r_sq = model.score(x, y)

y_pred = model.predict(x)
ax = plt.subplots(figsize=(10, 6))
sns.regplot(x=x, y=y)
sns.regplot(x=x, y=y_pred)
plt.xlabel("Объем двигателя")
plt.ylabel("Разгон до 100")
box_style = {'facecolor': 'blue', 'edgecolor': 'blue', 'boxstyle': 'round'}
plt.text(2.2, -1.7, 'Коэффициент детерминации: ' + str(r_sq), bbox=box_style, color='white', fontsize=10)
plt.title("Диаграмма рассеяния", fontsize=20)
plt.show()
