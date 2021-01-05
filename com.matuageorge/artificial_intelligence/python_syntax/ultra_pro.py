# coding=utf-8
# 1. Перебором параметра i в цикле for.
total = 0

for i in range(21):
    total += i
print (total)

# 2. Перебором параметра i в цикле while.
total = 0
i = 1
while i <= 20:
    total += i
    i += 1
print (total)

# 3. При помощи специальной функции для созданного списка.
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(sum(list_of_numbers))

# 4. При помощи перебора элементов созданного списка в цикле for.
total = 0

for x in list_of_numbers:
    total += x
print(total)

# 5. При помощи перебора элементов созданного списка в цикле while.
total = 0
i = 0

length = len(list_of_numbers)
while i <= length:
    total += i
    i += 1
print(total)

sample_list = ["мандаринки", "киви", "лимон"]

n = 3
result_list = []

for x in range(n):
    for fruit in sample_list:
        result_list.append(fruit + "_" + str(x + 1))
print(result_list)

list_for_pro_task_2 = [35, 0.24, 3 + 4j, "котики", 0.45, (8, 9), "слоники", {"Мадрид": 3, 'Лондон': 5}, 23498]

for index, element in enumerate(list_for_pro_task_2):
    if isinstance(element, dict):
        break
print(index)

sample_dict = {}

for x in range(1, 21):
    sample_dict.update({x: x ** 2})

print(sample_dict)

string = '[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,]'

result_list = [0]

for element in string.split(','):
    stripped_element = element.strip()
    if stripped_element.isdigit():
        result_list.append(int(stripped_element))

print(result_list)
