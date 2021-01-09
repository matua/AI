# coding=utf-8
# https://colab.research.google.com/drive/1mEH4b-Dxay-E8jGIgKb6zGFtpnibvz_L#scrollTo=pE1Y1o7KJ2YE

# ### Задача 1
# Используя соответствующую функцию библиотеки Pandas, подгрузите датасет из файла 'train.csv'.
# Выведите на экран первые 5 строк датафрейма (метод head).
# В качестве индексов датафрейма укажите нулевой столбец.
from __future__ import print_function

import pandas as pd
import numpy as np

from google.colab import drive

drive.mount('/content/drive')

train = pd.read_csv('/content/drive/MyDrive/Private/Обучение/Programming/Artificial '
                    'Intelligence/Databases/train.csv')

train.head(5)

train.set_index('Id')

# Задача 2
# Для подгруженного из предыдущей задачи датасета выполните следующее:
# посчитайте, сколько всего записей,
# определите тип данных в каждом столбце,
# проверьте, есть ли пропуски,
# выведите на экран описательные статистики.
# P.S. Используйте соответствующие встроенные методы.

print("Size: {}".format(train.size), end="\n\n")

print("Dtype of columns:")
print(train.info(), end="\n\n")

print("Number of nulls:")
print(train.isnull().sum())

# Describing stats
train.describe()

# Describing stats
train.describe(include=['O'])

# Задача 3 Используя соответствующий встроенный метод, дропните, т. е. удалите из нашей таблички все столбцы,
# у которых количество пропущенных значений больше 200.

# Найдите все такие столбцы (метод .isna() + подвыборка с условием).
# Определите их названия.
# Дропните их (используйте метод .drop(имена столбцов)).
# Результат сохраните в новой табличке data_1, исходную менять не нужно.
# Могут быть полезны следующие параметры и методы:

# columns - названия столбцов датафрейма
# df[условие] - подвыборка элементов по условию
# .drop - удаление строк или столбцов (в зависимости от параметра axis)

# short option
data_1 = train.dropna(thresh=len(train) - 200, axis=1)

# before
print(train.isnull().sum().sum())

# after
print(data_1.isnull().sum().sum())

# long_option

data_1 = train.copy()

# before
print(data_1.isnull().sum().sum())

columns_to_drop = data_1.columns[data_1.isna().sum() > 200]

for column in columns_to_drop:
    data_1.drop(column, axis=1, inplace=True)

# after
data_1.isnull().sum().sum()

# Задача 4 Данные, с которыми мы работаем в этом домашнем задании, содержат информацию о проданных домах. В
# датафрейме из прошлой задачи (data_1) найдите все дома, проданные в 2007 году, у которых цена продажи выше 300000 и
# есть бассейн. Для подвыборки с указанными условиями сначала создайте маску:
#
# цена продажи SalePrice
# год продажи YrSold
# наличие бассейна можно определить по столбцу PoolArea

search_mask = (data_1.SalePrice > 300000) & (data_1.YrSold == 2007) & (data_1.PoolArea > 0)
masked_result = data_1[search_mask]
masked_result

# Перетащите файлы, чтобы загрузить их в хранилище сеанса
# Диск
# Доступно: 75.73 GB.
# Задача 1
# Используя соответствующую функцию библиотеки Pandas, подгрузите датасет из файла 'train.csv'.
# Выведите на экран первые 5 строк датафрейма (метод head).
# В качестве индексов датафрейма укажите нулевой столбец.
# Решение:

drive.mount('/content/drive')

train = pd.read_csv('/content/drive/MyDrive/Private/Обучение/Programming/Artificial '
                    'Intelligence/Databases/train.csv')
train.head(5)

train.set_index('Id')

# Задача 4 Данные, с которыми мы работаем в этом домашнем задании, содержат информацию о проданных домах. В
# датафрейме из прошлой задачи (data_1) найдите все дома, проданные в 2007 году, у которых цена продажи выше 300000 и
# есть бассейн. Для подвыборки с указанными условиями сначала создайте маску:
#
# цена продажи SalePrice
# год продажи YrSold
# наличие бассейна можно определить по столбцу PoolArea

search_mask = (data_1.SalePrice > 300000) & (data_1.YrSold == 2007) & (data_1.PoolArea > 0)
masked_result = data_1[search_mask]
masked_result

# Задача 5 Добавьте к табличке data_1 новый столбец с названием 'Flag'. Присвойте ему значения 0 или 1 в случайном
# порядке. Для этого
#
# создайте одномерный массив из случайных целых чисел 0 или 1
# размер массива должен соответствовать количеству наблюдений в датафрейме data_1
# создайте новый столбец и присвойте ему значения одномерного массива

random_list = np.random.randint(0, 2, size=data_1.shape[0])
random_list

data_1['Flag'] = random_list
data_1
