from math import degrees

1.
# def greet(name):
#     message = f"Привет, {name}! Добро пожаловать!"
#     return message
#
# result = greet("Анна")
# print(result)

2.
# def square(num):
#     res = num * num
#     return res
#
# result = square(5)
# print(result)

3.
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
# print(is_even(4))
# print(is_even(7))

4.
# def repeat_string(text, times):
#     res = text * times
#     return res
#
# print(repeat_string("Python", 3))

# def repeat_string(text, times):
#     res = ''
#     for i in range(times):
#         res += text
#     return res
# print(repeat_string("Python", 8))

# def repeat_string(text, times):
#     return "".join([text] * times)
#
# print(repeat_string("Python", 3))

5.
# def add(a,b):
#     sum_1 = a + b
#     return sum_1
#
# print(add(3,9))

6.
# def get_max(a, b, c):
#     max_num = max(a, b, c)
#     return max_num
#
# print(get_max(10, 25, 7))

# def get_max(a, b, c):
#     numbers = [a, b, c]
#     return max(numbers)
#
# print(get_max(10, 25, 7))

# def get_max(*args):
#     if not args:
#         return None
#     return max(args)
#
# print(get_max(10, 25, 7))

7.
# def calculate(a, b, operation):
#     if operation == '+':
#         return a + b
#     elif operation == '-':
#         return a - b
#     elif operation == '*':
#         return a * b
#     elif operation == '/':
#         return a / b
#     else:
#         return None
#
# print(calculate(10, 5, "+"))
# print(calculate(10, 5, "*"))

8.
# def reverse_string(text):
#     return text[::-1]
#
# print(reverse_string("Python"))

9.
# def compare_strings(s1, s2, ignore_case=True, ignore_spaces=True):
#     str_1 = s1
#     str_2 = s2
#     if ignore_case:
#         str_1 = str_1.lower()
#         str_2 = str_2.lower()
#     if ignore_spaces:
#         str_1 = str_1.replace(' ', '')
#         str_2 = str_2.replace(' ', '')
#     return str_1 == str_2
#
# print(compare_strings("Hello", " hello "))
# print(compare_strings("Hello", "HELLO", ignore_case=False))
# print(compare_strings("Hello ", "Hello", ignore_spaces=False))


10.
# def summarize(*args):
#     total_sum = 0
#     for num in args:
#         if isinstance(num, (int, float)):
#             total_sum += num
#     return total_sum
#
# print(summarize(1, 2, 3))
# print(summarize(10, "abc", 5, 2))

# def summarize(*args):
#
#     return sum(num for num in args if isinstance(num, (int, float)))
#
# print(summarize(1, 2, 3))
# print(summarize(10, "abc", 5, 2))

11.
# def create_profile(name, age, **extra):
#     print("Профиль пользователя:")
#     print(f"Имя: {name}")
#     print(f"Возраст: {age}")
#
#     if extra:
#         print("Дополнительная информация:")
#         for key, value in extra.items():
#             print(f"{key}: {value}")
#
# create_profile("Иван", 30, city="Москва", job="Инженер")

12.
# def process_orders(*orders, discount=0):
#     res_sum = sum(orders)
#     discounted_total = res_sum * (1 - discount / 100)
#     print(f"Сумма заказа: {res_sum}")
#     print(f"С учетом скидки: {discounted_total}")
#
# process_orders(100, 200, 300, discount=10)


13.
# def merge_lists(*lists):
#     return sum(lists, [])
# print(merge_lists([1, 2], [3, 4], [5, 6]))

# def merge_lists(*lists):
#     result = []
#     for lst in lists:
#         result += lst
#     return result
#
# print(merge_lists([1, 2], [3, 4], [5, 6]))

14.
def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)

    return result
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = {"c": 5, "d": 6}
print(merge_dicts(d1, d2, d3))