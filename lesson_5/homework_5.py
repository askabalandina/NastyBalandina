# my_list = ["Москва", "Тверь", "Вологда"]
# print(my_list, type(my_list))
# numbers = list(range(1, 6))
# print(numbers)
# mixed = list((45, "строка", True, 4.5))
# print(mixed)
# mixed_1 = [45, "строка", True, 4.5]
# print(mixed_1)
from os import remove


# cities = ["Москва", "Тверь", "Вологда"]
# print(cities[0])
# numbers = list(range(6))
# # print(numbers[-1])
# print(cities[10])

# numbers = list(range(6))
# numbers[1] = 10
# print(numbers)
# mixed = list((45, "строка", True, 4.5))
# mixed[-1] = "Python"
# print(mixed)

# numbers = list(range(1, 6))
# print(len(numbers))
# numbers = [1,2,3,4,5]
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
# sorted_numbers = sorted(numbers, reverse=True)
# print(sorted_numbers)

# str_1 = [1, 2, 3]
# str_2 = [4, 5]
# str_3 = str_1 + str_2
# print(str_3)
# list_1 = ["Python", "is", "awesome"]
# print(list_1*3)

# numbers = [1,2,3,4,5]
# print(3 in numbers)
# cities = ["Москва", "Тверь", "Вологда"]
# print("Москва" in cities)
# mixed = [45, "строка", True, 4.5]
# print([1, 2] in mixed)

# numbers = [1,2,3,4,5]
# del numbers[2]
# print(numbers)

# cities = ["Москва", "Тверь", "Вологда"]
# del cities[-1]
# print(cities)

# str_1 = "Python"
# list_1 = list(str_1)
# print(list_1)
# print(max(list_1))
# print(min(list_1))
# print(sum(list_1))

# cities = ["Москва", "Тверь", "Вологда", "Тамбов"]
# cities_1=cities[0:4]
# print(cities_1)
# print("cities is cities_1:", cities is cities_1)  # False
# print("cities == cities_1:", cities == cities_1)  # True
# print("ID cities:", id(cities))
# print("ID cities_1:", id(cities_1))

# cities = ["Москва", "Тверь", "Вологда", "Тамбов"]
# print(cities[1:3])
# print(cities[1])
# print(cities[2])
# print(cities[2:])
# print(cities[:3])
# print(cities[0:4])
# print(cities[::-2])

# cities = ["Москва", "Тверь", "Вологда", "Тамбов"]
# print(cities[::2])
# print(cities[::-1])
# print(cities[::-2])
# 76
# cities = ["Москва", "Тверь", "Вологда", "Тамбов", "Екатеринбург", "Владивосток"]
# cities[1] = "Сочи"
# cities[2] = "Нижний Новгород"
# print(cities)
# cities[1::2] = ["Город", "Город", "Город"]
# cities[1::2] = ["Город"] * len(cities[1::2])
# print(cities)
# cities[1:3] = "Волгоград", "Омск"
# print(cities)

# lst_1 = [1, 2, 3]
# lst_2 = [4, 5, 6]
# lst_3_result = lst_1 + lst_2
# print(lst_3_result)
# lst = ["Python", "rocks"]
# print(lst*2)


# lst_1 = [1, 2, 3]
# lst_2 = [1, 2, 3]
# print(f"Равны ли lst_1 и lst_2: {lst_1 == lst_2}")
# print(lst_1 == lst_2)
# print("f равны ли: {lst_1 == lst_2}")
# lst_1 = [10, 5, 3]
# lst_2 = [5, 10, 3]
# print(f"Больше ли lst_1 и lst_2: {lst_1 > lst_2}")
# lst_1 = [1, 2, 3]
# lst_2 = [1, 2, "abc"]
# print(f"Сравни: {lst_1 > lst_2}")


# chars = list("Python")
# print(max(chars))
# print(min(chars))
# print(sum(chars))


# numbers = [5, 10, 15]
# numbers.append(20)
# print(numbers)
# numbers.insert(1,7)
# print(numbers)
# numbers.append('Python')
# print(numbers)
# numbers.insert(3, 'Python')
# print(numbers)


# numbers = [5, 10, 15, 90, 30]
# numbers.remove(10)
# print(numbers)
# numbers_result = numbers.pop()
# print(numbers)
# numbers_result = numbers.pop(4)
# print(numbers_result)
# print(numbers)
# numbers_result = numbers.pop(1)
# print(numbers)
# numbers_result = numbers.pop(1)
# print(numbers)


# letters = ["a", "b", "c"]
# letters_copy = letters.copy()
# letters_list = list(letters)
# print(letters_copy)
# print(letters_list)
# print(id(letters) == id(letters_copy))
# print(id(letters) == id(letters_list))
# print(letters is letters_copy)
# print(letters is letters_list)

125
# marks = [2, 3, 5, 3, 4, 5, 2, 3]
# print(marks.count(3))
# print(marks.index(5))
# marks_6 = 6 in marks     # не совсем понятно,что требуется в задании: Проверь, содержится ли число 6 в списке перед вызовом index()
# print(marks.index(6))


# nums = [8, 2, 5, 1, 7]
# nums.sort()
# print(nums)
# nums.sort(reverse=True)
# print(nums)
# nums.reverse()
# print(nums)


# cities = ["Москва", "Тверь", "Вологда", "Тамбов"]
# cities.sort()
# print(cities)
# cities_1 = sorted(cities)
# print(cities_1)


# chars = list("programming")
# print(chars.count('g'))
# chars.reverse()
# print(chars)
# chars.sort()
# print(chars)


# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(matrix)
# print(matrix[1])
# print(matrix[2][0])


# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# matrix[0] = [0, 0, 0,0]
# print(matrix)
