from pandas import *
import numpy as np


countRows = 500
min_noise_level = 10
max_noise_level = 100


def mask(size):
    digits = abs(np.random.randint(low=0, high=max_noise_level, size=size))
    return list(map(lambda x: 0 if x < min_noise_level else 1, digits))


speed = np.random.randint(low=-50, high=400, size=countRows) * mask(countRows)
speed = map(lambda x: np.nan if x == 0 else x, speed)
speed = map(lambda x, y: x * y, speed, mask(countRows))
speed = list(map(lambda x: int((np.random.random() * max_noise_level)) if x == 0 else x, speed))


weight = abs(
    np.random.randint(low=500, high=10000, size=countRows)
) * mask(countRows)
weight = map(lambda x: np.nan if x == 0 else x, weight)
weight = map(lambda x, y: x * y, weight, mask(countRows))
weight = list(map(lambda x: int((np.random.random() * max_noise_level)) if x == 0 else x, weight))

accelerationTime = abs(
    np.random.gamma(shape=1, scale=20, size=countRows)
) * mask(countRows)
accelerationTime = map(lambda x: np.nan if x == 0 else x, accelerationTime)
accelerationTime = map(lambda x, y: x * y, accelerationTime, mask(countRows))
accelerationTime = list(
    map(lambda x: int((np.random.random() * max_noise_level)) if x == 0 else x, accelerationTime))

numberSeats = abs(
    np.random.randint(low=1, high=6, size=countRows)
) * mask(countRows)
numberSeats = map(lambda x: np.nan if x == 0 else x, numberSeats)
numberSeats = map(lambda x, y: x * y, numberSeats, mask(countRows))
numberSeats = list(
    map(lambda x: int((np.random.random() * max_noise_level)) if x == 0 else x, numberSeats))

table = DataFrame({"max speed": speed, "weight": weight, "accelerationTime to up 100 km/h": accelerationTime,
                   "numberSeats": numberSeats})
print(table)

table.to_csv('carsInfo.csv', index=False)

# минимальный вес автомобиля
# самый быстрый разгон до 100км/ч
# средняя макс скорость
