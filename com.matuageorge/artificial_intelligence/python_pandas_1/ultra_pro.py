# coding=utf-8
# https://colab.research.google.com/drive/1FPVsPvevGvmqdQwnQcx76wPYx-xCBPgm?usp=sharing#scrollTo=xpelBtBBoNbH

# Задание 1
# Подключите Google Drive.
#
# Откройте папку с файлами и сохраните каждый из них в виде Pandas DataFrame.
#
# Подсказка 1: получить список имен файлов можно при помощи библиотеки os, командой os.listdir (путь к папке с файлами).
#
# Подсказка 2: для сохранения всех файлов в виде Pandas DataFrame удобно использовать одну из структур данных Python.
#
# Объедините все Pandas DataFrame в один.
import matplotlib as matplotlib
from google.colab import drive
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

drive.mount('/content/drive')

files_list = os.walk('/content/drive/MyDrive/Private/Обучение/Programming/Artificial Intelligence/Databases/bookings')

data_frame_list = []

for subdir, dirs, files in files_list:
    for filename in files:
        data_frame_list.append(pd.read_csv(subdir + os.sep + filename))

data_concat = pd.concat(data_frame_list)

# ### Задание 2
#
# Хорошо бы понимать, с какими данными мы работаем.
#
# Узнайте размерность получившегося DataFrame (число столбцов и число строк).
#
# Проверьте, выведя график, есть ли пропуски в данных. Оцените, насколько их много.

# number of rows
print("Number of rows: {}".format(data_concat.shape[0]))

# number of columns
print("Number of columns: {}".format(data_concat.shape[1]))

# shape alltogether
print("Dataframe shape: {}".format(data_concat.shape))

# data gaps
print("Number of NaNs: {}".format(data_concat.isna().sum().sum()))

data_concat

# graph display
fig, ax = plt.subplots(figsize=(20,12))
sns_heatmap = sns.heatmap(data_concat.isnull(), yticklabels=False, cbar=False, cmap='GnBu') # Визуализируем прпуски
plt.show()

# Основываясь на выводах из предыдущего задания, очистите данные от пропусков.
#
# Подсказка: очевидно, что есть полностью пустые столбцы, неинформативные строки с одним лишь значением "For notes:", пустая часть датасета внизу. После этих преобразований могут остаться пустые значения в датасете с хаотичным расположением (это допускается).
#
# Если остались пропуски, заполните их словом "unknown".

data_concat_backup = data_concat.copy()

# removing column[0] and dropping empty rows
del data_concat_backup['Unnamed: 0']
data_concat_backup.dropna(axis=0, how='all')

# removing NaN columns
columns_to_drop = data_concat_backup.columns[data_concat_backup.isna().sum() == data_concat_backup.shape[0]]

# removing rows which have only 'For Notes:' in column but empty row
data_concat_backup = data_concat_backup[data_concat_backup.hotel != 'For notes:']

data_concat_backup = data_concat_backup.fillna("unknown")

# graph display
fig, ax = plt.subplots(figsize=(20,12))
sns_heatmap = sns.heatmap(data_concat_backup.isnull(), yticklabels=False, cbar=False, cmap='GnBu') # Визуализируем прпуски
plt.show()

# Задание 4
# Необходимо посмотреть, сколько всего записей есть в столбце 'lead_time' по каждому отелю, за каждый год и каждый месяц каждого года.
#
# Подсказка: примените метод groupby для столбцов 'hotel', 'arrival_date_year', 'arrival_date_month'.

lead_time = data_concat_backup.groupby(['hotel', 'arrival_date_year', 'arrival_date_month'])['lead_time'].count()
lead_time

# Задание 5
# Узнайте размерность получившегося DataFrame (число столбцов и число строк).
#
# Сохраните получившийся DataFrame в одном файле.

print(data_concat_backup.shape)

lead_time.to_csv('data_concat_backup.csv')