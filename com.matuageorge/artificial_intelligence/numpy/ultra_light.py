# https://colab.research.google.com/drive/1M1kgfZT74MH3-cesU71xLM-Icbb3GOjD?usp=sharing#scrollTo=2uanDwJ3joEB

import numpy as np

sample_list = [1, 2, 3, 4, 5]
sample_nupmy_array = np.array(sample_list)
print(sample_nupmy_array)

print(sample_nupmy_array[0])
print(sample_nupmy_array[2])

print(type(sample_nupmy_array))

print(np.sum(sample_nupmy_array))

print(np.arange(0, 10))  # if 10 is exclusive
print(np.arange(0, 11))  # if 10 is inclusive
