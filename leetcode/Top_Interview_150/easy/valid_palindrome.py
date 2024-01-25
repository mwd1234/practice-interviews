# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

def pali_checker(s: str) -> bool:

    no_spaces = "".join(char for char in s if char.isalnum()).lower()

    if no_spaces == no_spaces[::-1]:
        return True

    return False


s = "A man, a plan, a canal: Panama"
print(pali_checker(s))