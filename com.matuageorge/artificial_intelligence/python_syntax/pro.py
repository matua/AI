# coding=utf-8
from __future__ import print_function

for i in range(1, 6):
    if i == 4:
        continue
    for j in range(0, i):
        print("@ ", end='')
    print("", end="\n\n")

for i in range(6):
    for j in range(i):
        print(i, end='')
    print()
    k = 4
for i in range(6, 10):
    for j in range(k):
        print(i, end='')
    print()
    k -= 1

x = 7
y = 1
while y < 10:
    print("{} * {} = {}".format(x, y, x * y))
    y += 1

d1 = int(input())
d2 = int(input())
if not (1 <= d1 <= 6) or not (1 <= d2 <= 6):
    if not (1 <= d1 <= 6):
        print("Ошибка! Значение на кубике 1 не входит в интервал [1, 6]")
    if not (1 <= d2 <= 6):
        print("Ошибка! Значение на кубике 2 не входит в интервал [1, 6]")
else:
    total = d1 + d2
    if total == 7 or total == 11:
        print("Я победил!!!")
    elif total == 2 or total == 3 or total == 12:
        print("Я проиграл :(")
    else:
        print("Сумма значений = {}".format(total))

for x in range(3000, 4301):
    if x % 11 == 0 and x % 5 != 0:
        print(x)
