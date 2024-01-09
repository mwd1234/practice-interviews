# Write a Python function that counts the frequency of each character in a given string and returns the result as a dictionary.

def char_counter(input_word):
    char_holder = {}
    
    for char in input_word: 
        char_holder[char] = char_holder.get(char, 0) + 1

    return char_holder
    
print(char_counter("This learning sesh has been awesomeeeee"))

# ChatGPT's Answer: 
def char_frequency(input_string):
    char_count = {}
    
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

# Test the char_frequency function
input_str = "hello"
result = char_frequency(input_str)
print(result)
