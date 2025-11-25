from collections.abc import async_generator
from ctypes import HRESULT
from operator import ifloordiv
from selectors import SelectSelector

1.
# x = int(input("Введите число х:"))
# if x > 0:
#     print("Число положительное")
# elif x < 0:
#     print("Число отрицательное")
# else:
#     print("Число равно нулю")

2.
# x = int(input("Введите целое число x:"))
# if x % 2 == 0:
#     print("Число четное")
# else:
#     print("Число нечетное")

3.
# number = int(input("Введите число: "))
# if 1 <= number <= 10:
#     print("Число в диапазоне")
# else:
#     print("Число вне диапазона")

4.
# a = int(input("Введите число a:"))
# b = int(input("Введите число b:"))
# if a < b:
#     a, b = b, a
# print(sorted([a, b], reverse=True))


5.
# a = int(input("Введите число a:"))
# b = int(input("Введите число b:"))
# if a < b:
#     print(a)
# else:
#     print(b)

6.
# marks = [3, 4, 5, 2, 5, 4]
# if 2 in marks:
#     print("Есть неудовлетворительная оценка")
# else:
#     print("Все оценки положительные")

7.
# x = int(input("Введите число x: "))
# if x % 3 == 0 and x % 5 == 0:
#     print("Число делится на 3 и 5")
# elif x % 3 == 0:
#     print("Число делится только на 3")
# elif x % 5 == 0:
#     print("Число делится только на 5")
# else:
#     print("Число не делится на 3 и 5")

8.
# password = input("Введите пароль:")
# if password == "admin123":
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")

# password = input("Введите пароль:")
# if password in ["admin123"]:
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")

9.
# amount = float(input("Введите сумму покупки: "))
# if amount >= 5000:
#     final_amount = amount * 0.90
#     print(f"Итоговая сумма со скидкой 10%: {final_amount:.2f} руб.")
# elif amount >= 1000:
#     final_amount = amount * 0.95
#     print(f"Итоговая сумма со скидкой 5%: {final_amount:.2f} руб.")
# else:
#     print(f"Итоговая сумма: {amount:.2f} руб.")

10.
# year = int(input("Введи год:"))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Год високостный")
# else:
#     print("Год не високостный")

# 1. Вложенные условия и elif
# grade = int(input("Введите оценку от 1 до 5:"))
# if grade == 5:
#     print("Отлично")
# elif grade == 4:
#     print("Хорошо")
# elif grade == 3:
#     print("Удовлетворительно")
# elif grade == 2 or grade == 1:
#     print("Неудовлетворительная оценка")
# else:
#     print("Некорректная оценка")

2.
# time = int(input("Введите текущее время в часах (0-23):"))
# if 6 <= time <= 11:
#     print("Утро")
# elif 12 <= time <= 17:
#     print("День")
# elif 18 <= time <= 21:
#     print("Вечер")
# elif 22 <= time <= 23 or 0 <= time <= 5:
#     print("Ночь")
# else:
#     print("Некорректное время")

3.
# temperature = int(input("Введите температуру:"))
# if temperature <= -10:
#     print("Очень холодно")
# elif -10 < temperature <= 0:
#     print("Холодно")
# elif  1 <= temperature <= 10:
#     print("Прохладно")
# elif 11 <= temperature <= 25:
#     print("Тепло")
# elif temperature > 25:
#     print("Жарко")

4.
# year = int(input("Введи год: "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#      print("Високостный год")
# else:
#    print("Год не високостный")

5.
# num_1 = int(input("Введите число 1: "))
# num_2 = int(input("Введите число 2: "))
# operation = input("Введите операцию: ")
# if operation == "+":
#     print(f"Сумма чисел: {sum([num_1,num_2])}")
# elif operation == "-":
#     print(f"Разность чисел: {num_1 - num_2}")
# elif operation == "*":
#     print(f"Произведение чисел: {num_1 * num_2}")
# elif operation == "/":
#     if num_2 != 0:
#         print(f"Частное чисел: {num_1 / num_2}")
#     else:
#         print("Ошибка: деление на ноль!")
# else:
#     print("Некорректная операция")

# 1. Тернарный оператор
# number = int(input("Введите число:"))
# result = "четное" if number % 2 == 0 else "нечетное"
# print(result)

2.
# num_1 = int(input("Введите число 1: "))
# num_2 = int(input("Введите число 2: "))
# max_num = num_1 if num_1 > num_2 else num_2
# print(max_num)

3.
# num = int(input("Введите число : "))
# result = "положительное" if num > 0 else "отрицательное" if num < 0 else "ноль"
# print(result)

4.
# age = int(input("Введите возраст: "))
# result = "Вход запрещен" if age <18 else "Вход разрешен"
# print(result)

5.
sum = float(input("Введите сумму покупки: "))
result = sum * 0.9 if sum > 500 else sum
print(f"Итоговая сумма: {result:.2f} руб.")