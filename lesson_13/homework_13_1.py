1.
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper
@uppercase_decorator
def say_hello():
    return "hello, world!"

print(say_hello())

2.
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for x in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(2)
def hello():
    print("Hello!")

hello()


3.
def cache(func):
    memory = {}

    def wrapper(*args):
        if args not in memory:
            result = func(*args)
            memory[args] = result
        else:
            result = memory[args]
        return result

    return wrapper

@cache
def slow_add(a, b):
    print(f"Вычисляю {a} + {b}...")
    return a + b

print(slow_add(2, 3))
print(slow_add(2, 3))


4.
import time


def timer(repeat):
    def decorator(func):
        def wrapper(*args, **kwargs):
            total_time = 0

            for _ in range(repeat):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                execution_time = end_time - start_time
                total_time += execution_time

            avg_time = total_time / repeat
            print(f"Среднее время выполнения: {avg_time:.4f} секунд")

            return result

        return wrapper

    return decorator


@timer(3)
def slow_function():
    time.sleep(1)


slow_function()