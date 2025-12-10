from multiprocessing.util import log_to_stderr
from operator import ifloordiv
from os import lstat

1.
# N = 6
#
# result = [num **2 for num in range(1, N+1)]
# print(result)

2.
# result = [num % 2 == 0 for num in range (-10, 10)]
# print(result)

# result_num = [num for num in range (-10, 11)if num % 2 == 0]
# print(result_num)

3.
# str = ["язык", "программирования", "Python"]
# result_str = [len(str) for str in str]
# print(result_str)

4.
# numbers = [1, 2, 3,  6, 7,  9, 10, 15, 20]
# result = []
# for num in numbers:
#     if num % 2 == 0:
#         result.append(f"четное")
#     else:
#         result.append(f"нечетное")
# print(result)


5.
# lst = [123, "Python", ["apple", "banana", "cherry"]]
# result_lst  =[ hasattr(lst, "__iter__") for lst in lst]
# print(result_lst)

import collections.abc
lst = [123, "Python", ["apple", "banana", "cherry"]]
result_lst  =[ isinstance(lst, collections.abc.Iterable) for lst in lst]
print(result_lst)