# s = "Python для автоматизации"
# print(f"Преобразованная строка в верхний регистр: {s.upper()}")
# print(f"Преобразованная строка в нижний регистр: {s.lower()}")


# msg = "абракадабра"
# print(msg.count("ра"))
# print(msg.count("а", 3))

# msg = "абракадабра"
# print(msg.index("ра"))
# print(msg.index("а", -1))
# print(msg.rindex("а"))
# print(msg.find("xyz"))
# print(msg.index("xyz"))

# text = "Я изучаю Java"
# print(text.replace("Java","Python"))
# print(text.replace(" ",""))


# text = "Python"
# text_1 = "12345"
# text_2 = "123abc"
# print(text.isalpha())
# print(text_1.isdigit())
# print(text_2.isdigit())

# code = "42"
# print(code.rjust(5, "0"))
# str_1 = "text"
# print(str_1.ljust(10, "*"))

# fruits = "яблоко, груша, банан"
# apple, pear, banana = fruits.split()
# print(apple)
# print(pear)
# print(banana)
# programming_languages = "python; java; c++"
# lng_1, lng_2, lng_3 = programming_languages.split(";")
# print(lng_1)
# print(lng_2)
# print(lng_3)
# result = programming_languages.split(";")
# print(result)

# list_1 = ["Привет,", "мир", "!"]
# str_1 = " ".join(list_1)
# print(str_1)
# list_fruits = ["apple", "banana", "cherry"]
# str_fruits = ", ".join(list_fruits)
# print(str_fruits)

# str_1 = " Python"
# print(str_1.replace(" ", ""))
# str_2 = "Python  "
# print(str_2.replace(" ", ""))
# str_3 = " Python  "
# print(str_3.replace(" ", ""))

# text = "программирование"
# print(text.title())
# print(text.capitalize())
# text_1 = text[0].upper() + text[1:]
# # print(text_1)
# # print(text.count("р"))
# print(text.index("и"))
# print(text[::-1])

# text = "Hello\nPython"
# print(text)

# t = "Python\tAutomation"
# print(t)

# path = "C:\\new\\test.txt"
# print(path)

# text = "Марка вина \"Ягодка\""
# print(text)

# path = r"C:\new\test.txt"
# print(path)

# s = "Hello\b World"
# print(s)
# s = "Hello\fPython"
# print(s)

# name = "Иван"
# age = 20
# str_1 = "Меня зовут" + " " + name + ", мне " + str(age) + " " + "лет."
# print(str_1)
# str_2 = "Меня зовут" + " " + name + ", мне " + 20 + " " + "лет."
# print(str_2)


# str_1 ="Привет, меня зовут {}, мне {}  лет." .format("Иван", 10)
# print(str_1)
# str_2 ="Привет, меня зовут {0}, мне {1}  лет." .format("Иван", 10)
# print(str_2)
# str_3 ="Привет, меня зовут {name}, мне {age}  лет." .format(name = "Иван",age = 10)
# print(str_3)
# str_4 ="Привет, меня зовут {1}, мне {0}  лет." .format("Иван", 10)
# print(str_4)

# city = "Санкт-Петербурге"
# year = 2025
# print(f"Сегодня {year} год, и я живу в {city}.")
# print(f"Через 5 лет будет {year + 5} год.")

# print(f"Дважды мой возраст: {34 *2}")
# print(f"Мое имя в верхнем регистре:{"nasty".upper()}")

text = "Курс валют: {} доллар = {} рубля.".format(1, 92.5)
print(text)
text_1 = "Курс валют: {value_1} доллар = {value_2} рубля.".format(value_1 = 1,value_2 = 92.5)
print(text_1)
print(f"Квадрат числа 7 = {7**2}")