1.
# set_1 = {1, 5, False, "python", (5, 6) }
# set_1.add(7)
# print(set_1)

2.
# cities_lst = {"Москва", "Санкт-Петербург", "Новосибирск", "Москва", "Екатеринбург", "Новосибирск"}
# print(cities_lst)
# print(len(cities_lst))

3.
# set_1 = {1, 3, 5, 6, 8, 9}
# set_1.remove(5)
# set_1.discard(15)
# print(set_1)


4.
# str = "abrakadabra"
# set_str = set(str)
# print(set_str)
# print(len(set_str))

5.
# set_1 = set()
# print(set_1)
# set_1.add(10)
# set_1.add('hello')
# set_1.add((1, 2, 3))
# set_1.add([4, 5, 6])
# print(set_1)

6.
# set_A = {1,2,3,4,5,"str"}
# set_B = {5,6,7,"str_1",9}
# res = set_A & set_B
# res = set_A.intersection(set_B)
# res = set_A | set_B
# res = set_A.union(set_B)
# res = set_A - set_B
# res = set_B - set_A
# res = set_A ^ set_B
# print(res)

7.
# even_numbers = {x for x in range(1, 11) if x % 2 == 0}
# odd_numbers = {x for x in range(1, 11) if x % 2 == 1}
# # print(even_numbers)
# # print(odd_numbers)
# res = even_numbers & odd_numbers
# res_1= even_numbers | odd_numbers
# print(res)
# print(res_1)

8.
python_students = {"Анна", "Иван", "Мария", "Сергей"}
java_students = {"Иван", "Дмитрий", "Сергей", "Алексей"}
# two_course = python_students & java_students
# two_course = python_students.intersection(java_students)
# print(two_course)
# one_course = python_students ^ java_students
# one_course = python_students.symmetric_difference(java_students)
# print(one_course)
# course =  python_students | java_students
# print(course)

9.
text1 = set("программирование")
text2 = set("автоматизация")
# common_letters = text1 & text2
# common_letters = text1.intersection(text2)
# print(common_letters)
# first_word = text1 - text2
# print(first_word)
unique_letters = text1 | text2
print(unique_letters)













5.


6.


7.


8.



9.
