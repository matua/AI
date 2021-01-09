# coding=utf-8
# https://colab.research.google.com/drive/1mKKJ5UM1OZLYUy0rH3rj8HQ0rqtolRMa?usp=sharing#scrollTo=B6MSVCRmC8nL
# Загрузите базу температур любым удобным способом. Выведите базу. Посчитайте число пустых записей в столбце State.
#
# Ссылка на скачивание базы: https://drive.google.com/file/d/1bLiz_81Kb4pMryEalRe66jS38_F6vwMX/view?usp=sharing
import pandas as pd

from google.colab import drive

drive.mount('/content/drive')

temperature_base = pd.read_csv('/content/drive/MyDrive/Private/Обучение/Programming/Artificial '
                               'Intelligence/Databases/city_temperature.csv')

# Заполните пустые данные в базе словом "No". Запишите результат в ту же переменную. Выведите ее на экран.

temperature_base

temperature_base.loc[:, 'State'].isnull().sum()

# При помощи метода Pandas определите число уникальных записей в столбцах Country, City, Year.

unique_countries = temperature_base['Country'].nunique()
unique_cities = temperature_base['City'].nunique()
unique_years = temperature_base['Year'].nunique()

print("Unique countries: {}".format(unique_countries))
print("Unique cities: {}".format(unique_cities))
print("Unique years: {}".format(unique_years))

# При помощи библиотеки Pandas выведите строки, где в столбце Country встречается страна Russia.
#
# При помощи метода Pandas отдельно выведите число элементов в этой выборке.

russia = temperature_base[temperature_base['Country'] == 'Russia']
print(russia)
print("Number of rows with Russia: {}".format(russia.shape[0]))


# Создайте новый столбец температур, в котором будут записаны те же значения AvgTemperature, но в градусах Цельсия (
# исходная единица измерения - градусы Фаренгейта).

def convert_fahrenheit_to_celcius(fahrenheit):
    return round((fahrenheit - 32) * 5 / 9, 1)


temperature_base['AvgTemperatureCelcius'] = [convert_fahrenheit_to_celcius(temp) for temp in
                                             temperature_base['AvgTemperature']]
temperature_base
