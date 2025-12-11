from types import new_class

1.
# dict_fruits = {
#     "apple": 154,
#     "banana": 66,
#     "cherry": 22
# }

# dict_fruits = dict(apple = 154, banana = 66, cherry= 22)
# dict_fruits['pear'] = 199
# print(dict_fruits)

2.
# grades = {"Анна": 5, "Борис": 4, "Виктор": 3, "Галина": 5, "Дмитрий": 2}
# for name, grade in grades.items():
#     if grade >= 4:
#         print(name)

3.
# countries = dict(Russia = "Moscow", Italy = "Rome", Peru = "Lima",  Japan = "Tokyo")
# country = input("Введите название страны: ")
# if country in countries:
#     print(countries[country])
# else:
#         print("Страна не найдена")

# countries = dict(Russia = "Moscow", Italy = "Rome", Peru = "Lima",  Japan = "Tokyo")
# country = input("Введите название страны: ")
# country = country.title()
# if country in countries:
#     print(countries[country])
# else:
#     print("Страна не найдена")

# countries = dict(Russia="Moscow", Italy="Rome", Peru="Lima", Japan="Tokyo")
# country = input("Введите название страны: ")
# capital = countries.get(country, "Страна не найдена")
# print(capital)

4.
# students = [
#     ("Анна", "Python"),
#     ("Борис", "Java"),
#     ("Виктор", "Python"),
#     ("Галина", "C++"),
#     ("Дмитрий", "Python")
# ]
# courses = {}
# for name, course in students:
#     if course not in courses:
#         courses[course] = []
#     courses[course].append(name)
#
# print(courses)

5.
# grades = {"Анна": 5, "Борис": 4, "Виктор": 3, "Галина": 5, "Дмитрий": 2}
# # new_grades = grades.pop("Дмитрий")
# # print(new_grades)
# # print(grades)
#
# if grades:
#     student_min_grade = min(grades, key=grades.get)
#     new_grade = grades.pop(student_min_grade)
#
# print(grades)

6.
# students = ["Анна", "Борис", "Виктор", "Галина"]
# new_lst = dict.fromkeys(students)
# print(new_lst)
# new_lst["Анна"] = 20
# new_lst["Борис"] = 21
# new_lst["Виктор"] = 19
# new_lst["Галина"] = 22
# print(new_lst)

7.
# exchange_rates = {"USD": 90, "EUR": 98, "GBP": 115}
# currency = input("Введите валюту: ")
# if currency in exchange_rates:
#     exchange_rate = exchange_rates[currency]
#     print(f'Курс {currency}: {exchange_rate}')
# else:
#     exchange_rates[currency] = None
#     print('Неизвестная валюта.')
#
# print(exchange_rates)

8.
dict1 = {"Python": "Язык программирования", "Java": "Популярный язык", "C++": "Язык для высокопроизводительных систем"}
dict2 = {"Python": "Простой и мощный", "JavaScript": "Язык для веба"}
dict1.update(dict2)
print(dict1)