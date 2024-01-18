# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

ransom_note = "aa"
magazine = "aab"

def can_construct(ransom_note: str, magazine: str) -> bool:
    
    ransom_letters = {}
    magazine_letters = {}
    
    for char in ransom_note: 
        if char in ransom_letters: 
            ransom_letters[char] += 1
        else: 
            ransom_letters[char] = 1
    
    for char in magazine: 
        if char in magazine_letters: 
            magazine_letters[char] += 1
        else: 
            magazine_letters[char] = 1
    
    for k, v in ransom_letters.items(): 
        if k in magazine_letters:
            if v > magazine_letters[k]: 
                return False
        else: 
            return False
    
    return True
    
    
print(can_construct(ransom_note, magazine))