'''
"""--------------------------------------------------------------------------------"""
# # Bug: The default argument items=[] is mutable and retains changes across calls. 
# def add_items_to_list(item, items=[]):
#     items.append(item)
#     return items

# Fix:
def add_items_to_list(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


my_list = add_items_to_list('apple')
print(my_list)  # ['apple']
my_list = add_items_to_list('banana')
print(my_list)  # Expected ['banana'], but the result is ['apple', 'banana']

"""--------------------------------------------------------------------------------"""
# Bug: This will raise a syntax error because of the incorrect use of = in the condition. 
# The assignment operator = is used instead of the comparison operator ==.
# def check_even_odd(num):
#     if num % 2 = 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")

# check_even_odd(5)

# Fix:
def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

check_even_odd(5)

"""--------------------------------------------------------------------------------"""
#Bug: The code will throw an IndexError because my_list does not have an element at 
# index 3 (Python indexing is zero-based, so index 3 would be the 4th element).
# def get_third_item(items):
#     return items[3]

# Fix:
def get_third_item(items):
    if len(items) > 2:
        return items[2]
    return "less than 3 items in the list :/"

my_list = [1, 2]
print(get_third_item(my_list))  # Raises an IndexError

"""--------------------------------------------------------------------------------"""
# Bug: division by zero
# def divide_numbers(a, b):
#     return a / b

# fix: 
def divide_numbers(a, b):
    if b != 0:
        return a / b
    return "cannot divide by zero"

print(divide_numbers(10, 0))

"""--------------------------------------------------------------------------------""" 
# Bug: prints 1 number less
# def print_numbers(n):
#     for i in range(1, n):
#         print(i)

# fix:
def print_numbers(n):
    for i in range(1, n+1):
        print(i)
print_numbers(5)
"""--------------------------------------------------------------------------------""" 
# Bug: adding list[num] instead of num. index probably will be out of range and the function will add the wrong numbers
# def sum_list_elements(lst):
#     total = 0
#     for num in lst:
#         total += lst[num]
#     return total

# Fix: either simply switch to total += num or change the loop to 'for num in range(len(lst))'
def sum_list_elements(lst):
    total = 0
    for num in lst:
        total += num
    return total


numbers = [10, 20, 30]
print(sum_list_elements(numbers))

"""--------------------------------------------------------------------------------""" 
# Bug: not reversing anything
# def reverse_string(s):
#     reversed_s = ""
#     for i in range(len(s)):
#         reversed_s += s[i]
#     return reversed_s


# fix 1:
# def reverse_string(s):
#     reversed_s = ""
#     for i in range(len(s)):
#         reversed_s += s[len(s) - i - 1]
#     return reversed_s

# fix 2:
def reverse_string(s):
    reversed_s = ""
    for i in range(len(s)-1, -1, -1):
        reversed_s += s[i]
    return reversed_s

print(reverse_string("hello"))

"""--------------------------------------------------------------------------------""" 
#Bug: count is 0, not 2
# def count_vowels(word):
#     vowels = "aeiou"
#     count = 0
#     for char in word:
#         if char in vowels:
#             count += 1
#     return count

# Fix: the function did not take in consideration the upper case letters
def count_vowels(word):
    vowels = "aeiou"
    count = 0
    for char in word:
        if char.lower() in vowels:
            count += 1
    return count

print(count_vowels("HELLO"))

"""--------------------------------------------------------------------------------""" 
# bug: the function doesn't take into consideration negative values
# def factorial(n):
#     result = 1
#     while n > 0:
#         result *= n
#         n -= 1
#     return result

# fix: check if n is negative
def factorial(n):
    if n < 0:
        return "complex infinaty"
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

print(factorial(-5))
print(factorial(5))

"""--------------------------------------------------------------------------------""" 
# Bug: doesnt handle spaces or uppercases
# def check_palindrome(word):
#     return word == word[::-1]

# fix:
def check_palindrome(word):
    original = word
    word = word.lower().replace(" ", "")
    return word == word[::-1]

print(check_palindrome("racecar"))
print(check_palindrome("Race Car "))
print(check_palindrome("hello"))

"""--------------------------------------------------------------------------------"""
# Bug: if word is not in dict then we will get a keyError
# def get_most_frequent_word(words):
#     frequency = {}
#     for word in words:
#         frequency[word] += 1
    
#     return max(frequency, key=frequency.get)


# fix 1:
# def get_most_frequent_word(words):
#     frequency = {}
#     for word in words:
#         if word in frequency:
#             frequency[word] += 1
#         else:
#             frequency[word] = 1
    
#     return max(frequency, key=frequency.get)

# fix 2: 
def get_most_frequent_word(words):
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    return max(frequency, key=frequency.get)


word_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(get_most_frequent_word(word_list))

"""--------------------------------------------------------------------------------""" 
# Bug: not doint its purposes
# def flatten_list(lst):
#     flat_list = []
#     for sublist in lst:
#         flat_list.append(sublist)
#     return flat_list

# fix:
# def flatten_list(lst):
#     flatten_list = []
#     for sublist in lst:
#         for element in sublist:
#             flatten_list.append(element)
#     return flatten_list

def flatten_list(lst):
    return [x for sub in lst for x in sub]

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
print(flatten_list(nested_list))

"""--------------------------------------------------------------------------------""" 
# Bug:
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet():
#         return f"Hello, my name is {self.name}"

# Fix:
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}"
    
p = Person("David")
print(p.greet())

'''