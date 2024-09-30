"""----------------------------- Snippet 1 ---------------------"""
def func1(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

func1(10)

# Answer: fibonacci

"""----------------------------- Snippet 2 ---------------------"""
def func2(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

nums = [3, 5, 1, 8, 2]
print(func2(nums))

# Answer: max num in a list

"""----------------------------- Snippet 3 ---------------------"""
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f"{self.name} makes a sound!"

my_animal = Animal("Buddy")
print(my_animal.sound())

# Answer:
"""----------------------------- Snippet 4 ---------------------"""

def func(lst):
    result = []
    for i in range(len(lst)):
        temp = []
        for j in range(i + 1, len(lst)):
            if lst[i] < lst[j]:
                temp.append(lst[j])
        if temp:
            result.append(temp)
    return result

lst = [3, 1, 4, 1, 5, 9, 2, 6]
print(func(lst))

"""----------------------------- Snippet 4 ---------------------"""
def func(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                matrix[i][j] = 0
            elif i > j:
                matrix[i][j] = matrix[j][i]
    return matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

mat = func(matrix)
for m in mat:
    print(m)

"""----------------------------- Snippet 5 ---------------------"""
def func(s):
    seen = {}
    start = 0
    max_len = 0
    for end in range(len(s)):
        if s[end] in seen:
            start = max(start, seen[s[end]] + 1)
        seen[s[end]] = end
        max_len = max(max_len, end - start + 1)
    return max_len

s = "abcabcbb"
print(func(s))

# this function returs the length of the longest substring in a given string, that has uniqe numbers
