# https://colab.research.google.com/drive/1CdavW4w_3MqDronco3YyeVny5GXvya7v#scrollTo=VuQOLDyRA0My
from __future__ import print_function

import numpy as np

my_array = np.loadtxt('/Users/annakockarova/Downloads/iris.csv', delimiter=',', skiprows=1)

my_generated_array = np.random.normal(0, 1, my_array.shape)

# print(my_array.shape == my_generated_array.shape)

multiplication_result = my_array * my_generated_array
glued_arrays = np.concatenate((my_array, my_generated_array), axis=1)
np.vsplit(glued_arrays, 50)

print(my_array[(my_array > 3) & (my_array < 5)])

super_array = np.random.uniform(15, 37, (2, 3, 4))  # 37 exlusively

super_array_updated = np.full(super_array.shape, "medium")

index = 0

for index_x, x in enumerate(super_array):
    for index_y, y in enumerate(x):
        for index_z, z in enumerate(y):
            if z < 20:
                super_array_updated[index_x][index_y][index_z] = "small"
            elif z > 30:
                super_array_updated[index_x][index_y][index_z] = "large"

print(super_array)
print(super_array_updated)