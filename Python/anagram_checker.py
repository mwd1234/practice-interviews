# Anagram Check:
# Check if two strings are anagrams of each other.

def anagram_checker(str_1: str, str_2: str):
    str_1 = str_1.replace(" ", "").lower()
    str_2 = str_2.replace(" ", "").lower()
    
    return sorted(str_1) == sorted(str_2)

print(anagram_checker("Matthew", "weMttah"))