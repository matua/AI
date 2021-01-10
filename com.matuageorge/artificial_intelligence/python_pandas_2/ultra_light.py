# coding=utf-8 Задача 1 Загрузите таблицу city_temperature.csv в pandas DataFrame. При помощи встроенных методов
# библиотеки Pandas найдите количество стран, среднее значение температуры в которых бывает больше 100 градусов по
# Фаренгейту.
#
# Циклы и условия использовать нельзя.
#
# Описание базы:
# Region - регион
#
# Country - страна
#
# State - штат (если есть)
#
# Month - месяц
#
# Day - день
#
# Year - год
#
# AvgTemperature - средняя температура в Фаренгейтах
#
# Ссылка на базу: https://drive.google.com/file/d/1bLiz_81Kb4pMryEalRe66jS38_F6vwMX/view?usp=sharing

import pandas as pd

temperature = pd.read_csv('/Users/annakockarova/Downloads/city_temperature.csv')
print("Number of countries: {}".format(temperature['Country'].nunique()))
print("Countries with average temperature above 100 Fahrenheit: {}".format(len(temperature.loc[temperature['AvgTemperature'] > 100, ['AvgTemperature']])))

# Задача 2
# Найдите медиану столбца AvgTemperature при помощи встроенных методов библиотеки Pandas.

print("Median of AvgTemperature: {}".format(temperature['AvgTemperature'].median()))

# Задача 3
# Найдите число записей в базе данных для первого января 1995 года или первого января 2018 года при помощи масок.

print("Out of {} - {} are entries for 01.01.1995 or 01.01.2018".format(len(temperature), len(temperature[((temperature['Day'] == 1) & (temperature['Month'] == 1) & ((temperature['Year'] == 1995) | (temperature['Year'] == 2018)))])))

# Задание 4
# Решение:
#
# Получите список всех уникальных значений стран в таблице при помощи встроенных методов.

print(temperature['Country'].unique())

# Задача 5 При помощи переводчика или при помощи своих знаний переведите названия столбцов на русский язык. Замените
# в таблице английские названия столбцов на русские

temperature.rename(columns={'Region': 'Регион', 'Country': 'Страна', 'State': 'Штат',  'City': 'Город',  'Month': 'Месяц',  'Day': 'День',  'Year': 'Год', 'AvgTemperature': 'Ср. температура'}, inplace=True)
print(temperature.columns)
