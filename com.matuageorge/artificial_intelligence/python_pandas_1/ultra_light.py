# coding=utf-8
# https://colab.research.google.com/drive/1sUaDu47w8HLBc5SdDDVZFCCrq8DaC4Zc#scrollTo=HzCIMqcTGMUB

import pandas as pd

columns = ['0', '1', '2', '3', '4', '5', '6']

index = ['0', '1', '2', '3']

# Создаем список с данными, каждая строка таблицы - отдельный список
data = [[0, 0, 0, 0, 0, 0, 0],
        [0, 1, 2, 3, 4, 5, 6],
       [0, 2, 4, 6, 8, 10, 12],
       [0, 3, 6, 9, 12, 15, 18]]
table = pd.DataFrame(data, columns = columns, index = index)
table

table.sum()

table.shape

table.iloc[:, [1, 4]] # if 2nd and 5th colums named as their indices
table.iloc[:, [2, 5]] # if 2nd and 5th colums named as their column names