# Write a Python function to reverse a given string.

# def string_reverser(input_word):
#     return input_word[::-1]

# print(string_reverser("I love you"))

# # ChatGPT's Answer:
# def reverse_string(s):
#     return s[::-1]

# # Test the reverse_string function
# text = "Hello, World!"
# reversed_text = reverse_string(text)
# print(f'The reversed string of "{text}" is: "{reversed_text}"')


# def string_reverser2(input_word):
#     # abcdefg
#     for char in input_word: 

word = "hello"

for i in range(len(word), 0, -1):
    print(word[i - 1])