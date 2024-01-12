def reverse_string(input_word):
    return input_word[::-1]


def reverse_string_no_built_in(input_word):
    reversed_word = ""
    for i in range(len(input_word), 0, -1): 
        reversed_word += input_word[i - 1]
    return reversed_word



print(reverse_string("hello"))

print(reverse_string_no_built_in("wassup"))
