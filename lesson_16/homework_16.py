# 1.
lst_1 = ["Python", 123, "Java", 456, "C++", 789]
str_gen = (item for item in lst_1 if isinstance(item,str))
result_str_gen = ' '.join(str_gen)
print(result_str_gen)


# 2.
import random
random_num = [random.randint(1, 100) for _ in range(10)]
max_num = max(random_num)
print(random_num)
print(max_num)

# import random
# random_gen = (random.randint(1, 100) for _ in range(5))
# num = list(random_gen)
# max_num = max(num)
# print(num)
# print(max_num)

# import random
# max_num = max(random.randint(1,100) for _ in range(10))
# print(max_num)

# import random
# numbers = [random.randint(1, 100) for _ in range(8)]
# print(f"Числа: {numbers} | Максимальное число: {max(numbers)}")

# 3.
def long_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            for word in line.split():
                if len(word) > 5:
                    yield word


for word in long_words('words.txt'):
    print(word)


# def long_words(file_path):
#     with open(file_path, 'r', encoding='utf-8') as f:
#         for line in f:
#             words = line.split()
#             for word in words:
#                 if len(word) > 5:
#                     yield word
#
# for word in long_words('words.txt'):
#     print(word)


# long_words = (word for line in open('words.txt', 'r', encoding='utf-8')
#              for word in line.split() if len(word) > 5)
# for word in long_words:
#     print(word)


# 4.
def find_python_lines(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if 'Python' in line:
                    yield line.strip()

for line in find_python_lines('text.txt'):
    print(line)


# def find_python_lines(file_path):
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             for line in file:
#                 if 'Python' in line:
#                     yield line.strip()
#     except FileNotFoundError:
#         print(f"Файл '{file_path}' не найден.")
#
# for line in find_python_lines('text.txt'):
#     print(line)

# 5.
import random

def infinite_random_generator():
    while True:
        num = random.randint(1, 100)
        if num == 50:
            break
        yield num
    yield 50

gen = infinite_random_generator()
for number in gen:
    print(number, end=' ')


# 6.
def prime_gen(N):
    primes_found = 0
    num = 2
    while primes_found < N:
        is_prime = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            yield num
            primes_found += 1
        num += 1

primes = prime_gen(10)
for prime in primes:
    print(prime)

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def generate_primes(n):
#     count = 0
#     number = 2
#
#     while count < n:
#         if is_prime(number):
#             yield number
#             count += 1
#         number += 1
#
# for prime in generate_primes(10):
#     print(prime, end=" ")

# 7.
def load_data():
    for i in range(1, 6):
        yield f"Получены данные {i}"

loader = load_data()

for data in loader:
    print(data)

# 8.
input_str = input("Введите числа через пробел: ")
numbers = list(map(int,input_str.split()))
sq = list(map(lambda x: x ** 2, numbers))
print(sq)


# input_str = input("Введите числа через пробел: ")
# sq_numbers = list(map(lambda x: int(x) ** 2, input_str.split()))
# print(sq_numbers)


# 9.
cities = ["Москва", "Санкт-Петербург", "Казань"]
list_cities = list(map(str.upper, cities))
print(list_cities)

# 10.
numbers = [15, 30, 45, 22, 60, 77, 90, 100]
even_numbers = filter(lambda num: num % 3 == 0 and num % 5 ==0, numbers)
print(list(even_numbers))


# input_str = input("Введите числа через пробел: ")
# numbers = map(int, input_str.split())
# even_num = filter(lambda num: num % 3 == 0 and num % 5 == 0, numbers)
# print(list(even_num))

# 11.
list_words = ["hello", "world42", "python3", "abc", "123", "data1science"]
string_num = filter(lambda word: any(char.isdigit() for char in word), list_words)
print(list(string_num))


# list_words = ["hello", "world42", "python3", "abc", "123", "data1science"]
# def contains_digit(word):
#     for char in word:
#         if char.isdigit():
#             return True
#     return False
# srt_num = filter(contains_digit, list_words)
# print(list(srt_num))

# 12.
countries = ["Россия", "Франция", "Германия"]
capitals = ["Москва", "Париж", "Берлин"]
my_dict = dict(zip(countries, capitals))
print(my_dict)

# 13.
data = [(1, 'a'), (2, 'b'), (3, 'c')]
num, let = zip(*data)
print(list(num))
print(list(let))

# 14.
names = ["петр", "Иван", "мария", "Анна"]
def get_sort_key(name):
    first_char = name[0]
    return (0 if ord('А') <= ord(first_char) <= ord('Я') else 1, name)
sorted_names = sorted(names, key=get_sort_key)
print(sorted_names)


# names = ["петр", "Иван", "мария", "Анна"]
# names.sort(key=lambda x: (not x[0].isupper(), x))
# print(names)


# 15.
products = [("Телефон", 500), ("Ноутбук", 1000), ("Планшет", 700)]
prices_sort = sorted(products, key = lambda item: item[1])
print(prices_sort)