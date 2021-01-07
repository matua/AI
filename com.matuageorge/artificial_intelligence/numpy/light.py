# https://colab.research.google.com/drive/1_dI5ApmtxQRm5OWWWBN8jJHFtyFdu76H?usp=sharing

from __future__ import print_function

import numpy as np

my_array = np.loadtxt('/Users/annakockarova/Downloads/train_vector_1.csv')
print(type(my_array))

# %%timeit

total = 0
for element in my_array:
    total += element
mean = total / len(my_array)

my_list = list(my_array)
print(len(my_list))

# %%timeit

total = 0
for element in my_list:
    total += element
mean = total / len(my_list)

my_2d_array = np.loadtxt('/Users/annakockarova/Downloads/iris.csv', delimiter=',', skiprows=1)
print(my_2d_array.sum(axis=0))

sample_numpy_array = np.random.randint(low=11, high=40, size=(3, 3))  # where 40 is exclusive
print(sample_numpy_array, end="\n\n")

print("Elements below 20 are as follows:")
print(sample_numpy_array[sample_numpy_array < 20], end="\n\n")

print("The total of all the elements in the array is as follows:")
print(np.sum(sample_numpy_array))

columns_type = [('name', 'S21'), ('age', 'i'), ('average_grade', 'f')]
values = [('Jonathan', 1, 5.),
          ('Anna', 31, 4.99),
          ('Svetlana', 67, 5.),
          ('David', 41, 5.),
          ('George', 38, 4.556)]

students = np.array(values, dtype=columns_type)

# sorted_students = sort()
sorted_students = np.sort(students, order='age')

print(sorted_students)

values = [('Jonathan', 10, 5.),
          ('Anna', 10, 4.99),
          ('Svetlana', 10, 5.),
          ('David', 10, 5.),
          ('George', 10, 4.556)]

students = np.array(values, dtype=columns_type)

# sorted_students = sort()
sorted_students = np.sort(students, order='age')

print(sorted_students)
