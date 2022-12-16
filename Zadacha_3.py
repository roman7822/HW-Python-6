# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:* - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# input_num = int(input('Введите число: '))
# list = [1]

# for i in range (1,input_num):
#     list.append ((i+1) * list [i-1])

# print(list)




from math import factorial
input_num = int(input('Введите число: '))
print(list(map(lambda i: ((i == 1) and 1) or i * factorial(i -1),list(range(1,input_num+1)))))


