def word_pattern(pattern: str, s: str) -> bool:
    # Split the string 's' into a list of words
    word_list = s.split()

    # Check if the lengths of 'pattern' and the list of words are equal
    if len(pattern) != len(word_list):
        return False
    
    pattern_to_word = {}
    word_to_pattern = {}

    # Iterate through each character in 'pattern' and its corresponding word in 's'
    for char, word in zip(pattern, word_list):
        # Check if the character already exists in the 'pattern_to_word' dictionary
        if char not in pattern_to_word:
            pattern_to_word[char] = word
        # If the character exists, make sure it maps to the same word as the current word
        elif pattern_to_word[char] != word:
            return False

        # Check if the word already exists in the 'word_to_pattern' dictionary
        if word not in word_to_pattern:
            word_to_pattern[word] = char
        # If the word exists, make sure it maps to the same character as the current character
        elif word_to_pattern[word] != char:
            return False

    # If all conditions pass, return True
    return True

# Test cases
print(word_pattern("abba", "dog cat cat dog"))  # Output: True
print(word_pattern("abba", "dog cat cat fish"))  # Output: False
print(word_pattern("aaaa", "dog cat cat dog"))   # Output: False


pattern = "abcba"
s = "dog cat duck cat dog"
print(word_pattern(pattern, s))
