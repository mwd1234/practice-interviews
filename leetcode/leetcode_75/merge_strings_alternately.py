# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

def merge_alternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """

    new_string = ""
    for idx, char in enumerate(word1):
        new_string += char
        if idx < len(word2):
            new_string += word2[idx]

    if len(word1) < len(word2):
        new_string += word2[idx + 1:]

    return new_string 


word1 = "abc"
word2 = "pqrxyz"

word1 = "ab"
word2 = "pqrs"

# word1 = "abcd"
# word2 = "pq"

print(merge_alternately(word1, word2))

# ChatGPT's answer: 

def mergeAlternately(word1, word2):
    merged = ""
    i, j = 0, 0

    while i < len(word1) and j < len(word2):
        merged += word1[i] + word2[j]
        i += 1
        j += 1

    # Append the remaining characters from both strings, if any
    merged += word1[i:] + word2[j:]

    return merged

# Example usage:
word1 = "abc"
word2 = "def"
result = mergeAlternately(word1, word2)
print(result)  # Output: "adbcef"
