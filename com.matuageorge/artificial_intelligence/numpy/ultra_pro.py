# coding=utf-8
from __future__ import print_function

import numpy as np

mx = np.zeros((5, 5), int)
np.fill_diagonal(mx, 1)
print(mx)

arr = np.random.normal(0, 1, (6, 6))
arr_reshaped = arr.reshape((36, 1))
print(np.average(arr_reshaped))

rand_arr = np.random.random((20,))

result = np.array([])
print("This is a random array:")
print(rand_arr, end="\n\n")

result = np.append(result, rand_arr[1] - rand_arr[0])
for i in range(2, rand_arr.size):
    result = np.append(result, (rand_arr[i] - rand_arr[i - 2]) / 2)
result = np.append(result, rand_arr[-1] - rand_arr[-2])

print("This is a gradient array of the above random array:")
print(result, end="\n\n")

print("This is a gradient array of the above random array generated via numpy function:")
result_via_gradient_fun = np.gradient(rand_arr)
print(result_via_gradient_fun, end="\n\n")

# checking the correctness via gradient method
print("Arrays are the same: " + str(np.array_equal(result, result_via_gradient_fun)))

# checking the correctness via gradient method
print(np.gradient(rand_arr))
A = np.random.random((5, 6))
C = np.random.random((7, 18))
X = np.random.random((6, 7))

Y = (A.dot(X)).dot(C)
# Y = A * X * C не явялется матричным умножением
print(Y.shape)

cars = np.loadtxt('/content/sample_data/cars.csv', delimiter=';', skiprows=1, usecols=(1, 2, 3, 4, 5, 6, 7))
# 1. Всю информацию из файла в ячейку.
print(cars)
# 2. Размерность данных.
print(cars.shape)
# 3. Среднее арифметическое от всех числовых значений (если есть).
print(np.mean(cars))
# 4. Число столбов.
print(cars.shape[1])
# 5. Число строк.
print(cars.shape[0])
# 6. Типы данных всех значений.
print(cars.dtype)