# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6,782 -> 23
# - 0,56 -> 11


# sum = 0
# input_num = input('Введите число: ')

# for a in input_num:
#     if a.isdigit():
#         sum += int(a)

# print(sum)

print(sum(list(map(lambda a: 0 if a == '.' else int(a), input('введите число: ')))))