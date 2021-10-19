import pandas as pd
import numpy as np
from pandas import DataFrame

volume = 'Объем двигателя'
number_seats = 'Кол-во сидений'
up_to_one_hundred = 'ускорение 0/100'
fuel_consumption = 'Расход топлива'

input_table = pd.read_csv('data.csv')

volume_t = input_table[volume].to_list()
number_seats_t = input_table[number_seats].to_list()
up_to_one_hundred_t = input_table[up_to_one_hundred].to_list()
fuel_consumption_t = input_table[fuel_consumption].to_list()


def normalized_array(input_array):
    output_array = input_array.copy()
    output_array = [element for element in output_array if not np.isnan(element) ]
    output_array.sort()
    lower_quartile_value = np.quantile(output_array, 0.25)
    upper_quartile_value = np.quantile(output_array, 0.75)
    interquartile_range = lower_quartile_value - upper_quartile_value
    lower_inner_fence = lower_quartile_value + 0.45 * interquartile_range
    upper_inner_fence = upper_quartile_value - 0.5 * interquartile_range
    median_value = np.median(output_array)
    return list(map(lambda x: x if lower_inner_fence <= x <= upper_inner_fence else median_value,
                    input_array))


volume_t = normalized_array(volume_t)
number_seats_t = normalized_array(number_seats_t)
up_to_one_hundred_t = normalized_array(up_to_one_hundred_t)
fuel_consumption_t = normalized_array(fuel_consumption_t)

output_table = DataFrame({"volume": volume_t, "number_seats": number_seats_t, "up_to_one_hundred": up_to_one_hundred_t,
                          "fuel_consumption": fuel_consumption_t})

mean_volume = output_table['volume'].mean()
median_number_seats = output_table['number_seats'].median()
min_fuel_consumption = output_table['fuel_consumption'].min()

print(output_table)

print('Средний объем двигателя:')
print(mean_volume)

print('Медиана по кол-ву сидений:')
print(median_number_seats)

print('Минимальный расход топлива:')
print(min_fuel_consumption)

output_table.to_csv('dataNormal.csv', index=False)
