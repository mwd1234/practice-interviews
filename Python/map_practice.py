# Given a list of strings representing numbers, use map() to convert each string to an integer.

my_list = ["1", "2", "3", "4", "5"]

my_int_list = list(map(int, my_list))

print(my_int_list)

# Given a list of integers, use map() to calculate the square of each number.

square_int_list = list(map(lambda x: x**2, my_int_list))

print(square_int_list)

# Given a list of temperatures in Celsius, use map() to convert each temperature to Fahrenheit.
celsius_temps = [0, 10, 20, 30, 40]

# (C * 9/5) + 32

fahrenheit_temps = list(map(lambda x: (x * 9/5) + 32, celsius_temps))

print(fahrenheit_temps)

# Count Length of Words in a Sentence:
# Given a sentence, use map() to find the length of each word.

sentence = "This is a sample sentence"

print(list(map(len, sentence.split())))

# Multiply Elements of Two Lists:
# Given two lists of numbers, use map() to multiply corresponding elements.

list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 4, 5, 6]

print(list(map(lambda x, y: x*y, list1, list2)))

# Given a list of strings, use map() to convert each string to uppercase.

strings = ["apple", "banana", "cherry", "date"]

print(list(map(str.upper, strings)))

# Given a list of numbers, use map() to calculate the factorial of each number.

numbers = [1, 2, 3, 4, 5]

def factorial_func(num):
    num_holder = 1
    for i in range(1, num + 1): 
        num_holder *= i
    
    return num_holder

print(list(map(factorial_func, numbers)))

# Given a list of strings, use map() to check if each string is a palindrome.

strings = ["radar", "level", "python", "madam"]

print(list(map(lambda x: x == x[::-1], strings)))

# Given a list of words, use map() to count the number of vowels in each word.

words = ["apple", "banana", "cherry", "date"]

print(list(map(lambda x: sum(1 for char in x if char.lower() in "aeiou"), words)))