1.
# def multiply_by(n):
#     def multiply(x):
#         return x * n
#     return multiply
#
# times3 = multiply_by(3)
# times5 = multiply_by(5)
#
# print(times3(10))
# print(times5(10))

2.
def counter(start=0):
    count = start

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


c1 = counter(5)
c2 = counter()

print(c1())
print(c1())
print(c2())
print(c2())