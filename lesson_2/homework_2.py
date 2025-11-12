a = 5
b = 4
x = 2.9
y = -9.7
print(type(a),type(b),type(x),type(y))
print(type(a))
print(type(b))
print(type(x))
print(type(y))
print(f"переменная a = {a}, тип: {type(a)}")
print(f"переменная b = {b}, тип: {type (b)}")
print(f"переменная x = {x}, тип: {type (x)}")
print(f"переменная y = {y}, тип: {type (y)}")

num1 = 5
num2 = 9
print("Результат сложения:", num1+num2)
print("Результат вычитания:", num1-num2)
print("Результат умножения:", num1*num2)
print("Результат деления:", num1/num2)
print("Результат целочисленное деление:", num1//num2)
print("Результат остаток от деления:", num1 % num2)
print("Результат возведение в степень:", num1 ** num2)

a = 10
b = 3
print("Резульат деления:", a / b)
print("Результат целочисленного деления:", a // b)
print("Результат остаток от деления:", a % b)
a = -10
b = 3
print("Резульат деления:", a / b)
print("Результат целочисленного деления:", a // b)
print("Результат остаток от деления:", a % b)
a = 10
b = -3
print("Резульат деления:", a / b)
print("Результат целочисленного деления:", a // b)
print("Результат остаток от деления:", a % b)

print("Выведи результат:", 5+3*2)
print("Выведи результат:", (5+3)*2)
print("Выведи результат:", 10/2**2)

count = 10
count += 5
count -= 3
count *= 2
count /= 4
print(count)

s1 = "Python"
s2 = 'Программирование'
print(s1)
print(s2)
multi_line_str= """Многострочная строка,
созданная с помощью
тройных кавычек"""
print(multi_line_str)
empty = ""
print(len(empty))

first_name = "Иван"
last_name = "Петров"
print("full_name:", first_name + " " + last_name)
full_name = first_name + " " + last_name
print(full_name)
full_name = f"{first_name} {last_name}"
print(full_name)

s = "Возраст: "
age = 25
print(s + str(age))

str_1="ха "
print(str_1 * 5)
print(str_1*2.5)

text = "Привет, мир!"
print(len(text))
text_1 = ""
print(len(text_1))

sentence = "Я изучаю Python"
print("Python" in sentence)
print("Java" in sentence)

a = "apple"
b = "banana"
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)

print(ord('A'))
print(ord('а'))
print(ord('Я'))