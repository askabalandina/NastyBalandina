1.
f = "data.txt"
file = open(f, 'r', encoding='utf-8')
text = file.read()
print(text)
file.close()

2.
f = "data.txt"
file = open(f, 'r', encoding='utf-8')
text_line = file.readline()
print(text_line)
file.close()

f = "data.txt"
with open('data.txt', 'r', encoding='utf-8') as file:
     text_line = file.readline()
     print(text_line)

3.
f = "data.txt"
file = open(f, 'r', encoding='utf-8')
print(file.read(10))
file.close()


f = "data.txt"
with open('data.txt', 'r', encoding='utf-8') as file:
    print(file.read(10))

4.
f = "data.txt"
file = open(f, 'r', encoding='utf-8')
text_lines = file.readlines()
print(text_lines)
file.close()


f = "data.txt"
with open('data_2.txt', 'r', encoding='utf-8') as file:
     text_lines = file.readlines()
     print(text_lines)

5.
f = "data.txt"
file = open(f, 'r', encoding='utf-8')
for line in file:
   print(f"Строка: {line}", end="")
file.close()

6.
f = "data.txt"
file = open(f, 'r', encoding='utf-8')
print(file.read(6))
file.seek(0)
print(file.read(6))
file.close()

7.
import os

try:
    f = "data.txt"
    with open('data_2.txt', 'r', encoding='utf-8') as file:
        size = os.path.getsize(f)
        print(f"Размер файла: {size} байт")

except FileNotFoundError:
       print("Файл не найден")

8.
f = "data.txt"
with open('data_2.txt', 'r', encoding='utf-8') as file:
    print(file.read())


9.
import os

try:
    f = "data.txt"
    with open('data_2.txt', 'r', encoding='utf-8') as file:
        size = os.path.getsize(f)
        print(file.read())
        print(f"Размер файла: {size} байт")

except FileNotFoundError:
       print(f"Ошибка: Файл не найден")


import os

try:
    f = "data7.txt"
    with open('data_7.txt', 'r', encoding='utf-8') as file:
        size = os.path.getsize(f)
        print(file.read())
        print(f"Размер файла: {size} байт")

except FileNotFoundError:
       print(f"Ошибка: Файл не найден")


10.
try:
   f = "data.txt"
   file = open(f, 'r', encoding='utf-8')
   try:
    text = file.read()
    print(text)
   finally:
      file.close()
except FileNotFoundError:
        print(f"Ошибка: Файл не найден")


11.
import os

try:
   f = "data.txt"
   file = open(f, 'r', encoding='utf-8')
   for line in file:
       print(f"{line}", end="")
   file.close()
except FileNotFoundError:
        print(f"Ошибка: Файл не найден")

12.
try:
    with open('numbers.txt', 'r', encoding='utf-8-sig') as f:
        numbers = map(int, f.read().splitlines())  # splitlines разбивает текст на строки
        total = sum(numbers)
        print(f"Сумма чисел: {total}")
except FileNotFoundError:
    print("Ошибка: Файл не найден")

try:
    with open('numbers.txt', 'r', encoding='utf-8-sig') as f:
        numbers = list(map(int, f.read().splitlines()))  # преобразовываем строки в числа и делаем список
        print("Прочитанные числа:", numbers)
        total = sum(numbers)
        print(f"Сумма чисел: {total}")
except FileNotFoundError:
    print("Ошибка: Файл не найден")
except ValueError:
    print("Ошибка: Некорректные данные в файле")


try:
   f = "numbers.txt"
   with open(f, 'r', encoding='utf-8-sig') as file:
    text = file.read()
    print(text)
    sum_result = sum(map(int, text.split()))
    print(f"Сумма чисел:{sum_result}")
    file.close()
except FileNotFoundError:
        print(f"Ошибка: Файл не найден")


13.
import datetime

current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

with open('log.txt', mode='a', encoding='utf-8') as log_file:
    log_entry = f"{formatted_time} Запуск программы\n"
    log_file.write(log_entry)

import datetime

with open('log.txt', 'a', encoding='utf-8') as f:
    f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Запуск программы\n")