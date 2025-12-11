1.
# t = "Python", 8, True, [1, 2 ,4], 1.2
# print(type(t))
# print(t[1])
# print(t[-1])

2.
# nums = (4, 7, 2, 9, 4, 1, 7, 4, 3, 9)
# print(nums.count(4))
# print(nums.index(7))

3.
# lst = ["Python", "Java", "C++", "JavaScript"]
# t= tuple(lst)
# print(type(t))

4.
# tuple = (1,2,3,4,5,7,9,10)
# print(tuple[0:3])
# print(tuple[-3::])
# print(tuple[2:])


5.
# t = ([1,3,5,7], {"Python","Java"})
lst_1 = [1, 3, 5, 7]
dict_1 = {"lang1": "Python", "lang2": "Java"}
t = (lst_1, dict_1)
# print(t)
t[0].append(9)
print(t)