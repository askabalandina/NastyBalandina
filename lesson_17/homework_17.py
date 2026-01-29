# 1.
items = [5, "hello", [1, 2], 3.14, {"a": 1}, "world"]
res_items = []
for item in items:
    if isinstance(item, (list,str)):
        res_items.append(item)
print(res_items)

items = [5, "hello", [1, 2], 3.14, {"a": 1}, "world"]
res_items = [item for item in items if isinstance(item, (str, list))]
print(res_items)


# 2.
def describe_type(x):
    if isinstance(x, str):
        print("Это строка")
    elif isinstance(x, (int, float)):
        print("Это число")
    elif isinstance(x, bool):
        print("Это булевое значение")
    else:
        print("Неизвестный тип")

print("Тест:")
describe_type(5.5)
describe_type(True)
describe_type("Привет")
describe_type([1, 2, 3])


# 3.
def filter_list(f, data: list[int])  -> list[int]:
    return [item for item in data if f(item)]

test_data = [1, 3, 5, 7]
filter_func = lambda x: x > 3
result = filter_list(filter_func, test_data)
print(f"Результат: {result}")


def filter_list(f, data: list[int]) -> list[int]:
    result = []
    for item in data:
        if f(item):
            result.append(item)
    return result


test_data = [1, 3, 5, 7]
filter_func = lambda x: x > 3
result = filter_list(filter_func, test_data)
print(f"Результат: {result}")

def filter_list(f, data: list[int]) -> list[int]:
    return list(filter(f, data))
test_data = [1, 3, 5, 7]

filter_func = lambda x: x > 3
result = filter_list(filter_func, test_data)
print(f"Результат: {result}")

# 4.
def print_info(name: str, age: int, tags: list[str]) -> None:
    print(name, age, tags)

print_info("Петр", 30, ["Aqa", "python"])

# 5.
def analyze(data: list) -> None:
    if not data:
        print("Пустой список")
        return

    count = len(data)
    average = sum(data) / count
    print(f"Количество элементов: {count}")
    print(f"Среднее значение: {average}")

analyze([1, 2, 3, 4, 5])

# 6.
flags = [True, True, True, False]
flags_all_true = all(flags) == True
print(flags_all_true)
flags_any_true = any(flags) == True
print(flags_any_true)

flags = [True, True, True, False]
print(all(flags))
print(any(flags))

# 7.
field = ['x', 'x', 'x', 'o', 'o', '', '', '', '']
winner_x_1_row = all(x == 'x' for x in field[:3])
print(winner_x_1_row)

# 8.
P = ['0', '0', '0', '*', '0']
P_contains = any(x == '*' for x in P)
print(P_contains)


# 9.
import random
colors = ["red", "green", "blue", "yellow", "purple"]
print(random.choice(colors))

# 10.
import random
random.seed(10)
num = [random.randint(1,100) for i in range(10)]
print(num)

# 11.
def greet(name: str) -> str:
    return f"Привет, {name}!"

print(greet("Анна"))

# 12.
def multiply(a: int | float, b: int | float) -> int | float:
    return a * b
print(multiply(2, 10))


# 13.
def area(length: float, width: float) -> float:
     return length * width
print(area.__annotations__)