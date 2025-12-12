from operator import ifloordiv

1.
# set_1 = {x ** 2 for x in range(1, 11) if x % 2 == 0}
# print(set_1)

2.
# words = ["apple", "banana", "cherry", "apple", "banana", "date", "cherry"]
# set_words = set(words)
# uppercase_words = {words.upper() for words in set_words}
# print(uppercase_words)

3.
# grades = {"Alice": 85, "Bob": 78, "Charlie": 92, "David": 60, "Eve": 88}
# dict_grades = {student: "отлично" if grade >= 80 else "удовлетворительно"
#     for student, grade in grades.items()
# }
# print(dict_grades)


4.
# text = {"Python", "automation", "programming", "testing"}
# word_lengths = {word: len(word) for word in text}
# print(word_lengths)

5.
n = 10
result = {
    i: {j ** 2 for j in range(1, i + 1)}
    for i in range(1, n + 1)
}
print("Вложенный словарь (n = 10):")
for key, value in result.items():
    print(f"  {key}: {value}")