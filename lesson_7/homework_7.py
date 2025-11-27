from gc import is_finalized
from traceback import format_tb

1.
# N = int(input("Введите число N: "))
# num = 1
# while num <= N:
#     print(num)
#     num += 1


2.
# N = int(input("Введите число N: "))
# num = 2
# sum = 0
# while num <= N:
#     sum_1 = sum + num
#     num = num + 2
#
# print("Сумма всех чётных чисел от 1 до", N, "равна:", sum_1)

3.
# n = input("Введите натуральное число N: ")
# i = 0
# s = 0
# while i < len(n):
#     if n[i].isdigit():
#         s += 1
#     i += 1
#
# print("В числе", n, "содержится", s, "цифр(а)")

4.
# n = input("Введите натуральное число N: ")
# max_digit = -1
# while len(n) > 0:
#     digit = int(n[-1])
#     if digit > max_digit:
#         max_digit = digit
#     n = n[:-1]
# print(f"Максимальная цифра в числе: {max_digit}")

5.
# correct_password = "qwerty123"
# input_password = input("Введите пароль: ")
# while input_password != correct_password:
#     print("Пароль не верен, введите еще раз")
#     input_password = input("Введите пароль: ")
# print("Пароль верен")


# Задачи по уроку "Операторы break, continue и else в цикле while"
1.
# numbers = [23, 43, 75, 33, 80, 51, 62]
# i = 0
# while i < len(numbers):
#     if numbers[i] % 2 == 0:
#         print("Первое четное число:", numbers[i])
#         break  # Останавливаем цикл
#     i += 1
# else:
#     print("Четное число не найдено")

2.
# plus_sum = 0
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     if n < 0:
#         continue
#     plus_sum += n
# print("Сумма положительных чисел:", plus_sum)

3.
# a = int(input("Введите число a:"))
# b = int(input("Введите число b:"))
# if a > b:
#     a, b = b, a
# i = a
# while i <= b:
#     if i % 2 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1

4.
# N = int(input("Введите число N: "))
#
# if N <= 1:
#     print("Число не является простым (простые числа > 1)")
# else:
#
#     for i in range(2, int(N**0.5) + 1):
#         if N % i == 0:
#             print(f"Число {N} не является простым, делится на {i}")
#             break
#     else:
#
#         print(f"Число {N} является простым")

5.
# max_num = None
#
# while True:
#     num = input("Введите число: ")
#
#     if num == "" or num == "0":
#         break
#
#     num = int(num)
#     if max_num is None or num > max_num:
#         max_num = num
#
# if max_num is not None:
#     print("Наибольшее число:", max_num)
# else:
#     print("Числа не вводились")

# Задачи по уроку "Цикл for в Python – основы и применение"
1.
# str = "Hello World!"
# for char in str[::-1]:
#     print(char)

2.
# numbers = [1, 2, 8, 9, 10]
#
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         numbers[i] = 0
#
# print(numbers)

# numbers = [1, 2, 3, 4, 5]
#
# for i in range(len(numbers)):
#     numbers[i] = 0 if numbers[i] % 2 == 0 else numbers[i]
#
# print(numbers)

3.
# N = int(input("Введите число N:"))
# extent_2 = [2 ** i for i in range(N + 1)]
# print(f"Степени двойки от 2^0 до 2^{N}: {extent_2}")

4.
A = int(input("Введите число A:"))
B = int(input("Введите число B:"))
K = int(input("Введите число K:"))

for number in range(A, B + 1, K):
    print(number, end=" ")
