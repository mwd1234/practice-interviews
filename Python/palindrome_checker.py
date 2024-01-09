# Create a Python function to check whether a given string is a palindrome or not.

def palindrome_yes_or_no(input_word):
    # the first letter + last letter are the same
    # beg+1:end-1 are the same, too

    if len(input_word) == 1:
        return True    
    
    for idx in range(len(input_word) // 2): 
        if input_word[idx] != input_word[-idx - 1]:
            return False
        
    return True

print(palindrome_yes_or_no("a")) # Should be true
print(palindrome_yes_or_no("aa")) # Should be true
print(palindrome_yes_or_no("aba")) # Should be true
print(palindrome_yes_or_no("tacocat")) # Should be true
print(palindrome_yes_or_no("tacoscat")) # Should be false

# ChatGPT's Answer: 
def is_palindrome(s):
    return s == s[::-1]

# Test the palindrome function
word = "radar"
if is_palindrome(word):
    print(f'{word} is a palindrome')
else:
    print(f'{word} is not a palindrome')
