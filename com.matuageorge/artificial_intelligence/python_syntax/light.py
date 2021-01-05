# coding=utf-8
# https://colab.research.google.com/drive/1K38SS4vvNVYv2A8CmCi-eJluLQMZq4wa#scrollTo=eHA_26PRqDqm

# N = int(input())
# if (N % 2) != 0:
#     print("N нечетное")
# else:
#     if 5 <= N <= 10:
#         print("N четное и принадлежит интервалу[5, 10]")
#     elif N > 10:
#         print("N четное и N > 10")
#     else:
#         print("N четное и N < 5")

n = 15
total = 0
while n < 23:
    total += n ** 2
    n += 1
print(total)

total = 0
my_list = [56, 23, 67, 45, 67, 2, 47, 158, 31, 34, 78, 23, 78, 23, 89, 23, 36]

for i in my_list:
    total += i
print(total)

maximus = 0
for i in my_list:
    if i > maximus:
        maximus = i
print(maximus)

candies = {
    'Natasha': 2,
    'Alina': 3,
    'Marat': 15,
    'Lev': 1,
    'Valera': 0,
}

candies.update(
    {'Roma': 4}
)

print(candies)