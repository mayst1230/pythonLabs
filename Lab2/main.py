import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 2000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 2000)
pd.set_option("display.precision", 2)

volume = 'Объем двигателя'
numberSeats = 'Кол-во сидений'
upToOneHundred = 'ускорение 0/100'
fuelConsumption = 'Расход топлива'

table = pd.read_csv('data.csv')

max_volume = 7.0
default_volume = 12.0
default_upToOneHundred = 10.0
max_upToOneHundred = 2.0
max_numberSeats = 8
default_numberSeats = 4
default_fuelConsumption = 15.0
max_fuelConsumption = 25.0

volume_t = table[volume]
numberSeats_t = table[numberSeats]
upToOneHundred_t = table[upToOneHundred]
fuelConsumption_t = table[fuelConsumption]

volume_t.update(volume_t.replace(np.nan, default_volume))
table.loc[(table[volume] > max_volume), volume] = max_volume

numberSeats_t.update(numberSeats_t.replace(0, default_numberSeats))
table.loc[(table[numberSeats] > max_numberSeats), numberSeats] = max_numberSeats

upToOneHundred_t.update(upToOneHundred_t.replace(np.nan, default_upToOneHundred))
table.loc[(table[upToOneHundred] < max_upToOneHundred), upToOneHundred] = max_upToOneHundred

fuelConsumption_t.update(fuelConsumption_t.replace(np.nan, default_fuelConsumption))
table.loc[(table[fuelConsumption] > max_fuelConsumption), fuelConsumption] = max_fuelConsumption

meanVolume = table['Объем двигателя'].mean()
medianNumberSeats = table['Кол-во сидений'].median()
minFuelConsumption = table['Расход топлива'].min()

print('Средний объем двигателя:')
print(meanVolume)

print('Медиана по кол-ву сидений:')
print(medianNumberSeats)

print('Минимальный расход топлива:')
print(minFuelConsumption)

table.to_csv('dataNormal.csv', index=False)