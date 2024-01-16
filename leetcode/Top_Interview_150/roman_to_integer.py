# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, 
# which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
# Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
# The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

def roman_int_converter(s: str) -> int: 
    running_total = 0

    for idx, char in enumerate(s): 
        if char == "I" and idx < len(s) -1: 
            if s[idx + 1] in ["V", "X"]:
                running_total -= 1
            else: 
                running_total += 1
                
        elif char == "X" and idx < len(s) -1: 
            if s[idx + 1] in ["L", "C"]:
                running_total -= 10
            else: 
                running_total += 10
        
        elif char == "C" and idx < len(s) -1: 
            if s[idx + 1] in ["D", "M"]:
                running_total -= 100
            else: 
                running_total += 100
        else: 
            if char == "I":
                running_total += 1
            if char == "V":
                running_total += 5
            if char == "X":
                running_total += 10
            if char == "L":
                running_total += 50
            if char == "C":
                running_total += 100
            if char == "D":
                running_total += 500
            if char == "M":
                running_total += 1000
        
    return running_total

print(roman_int_converter(s = "MCMXCIV"))


def roman_int_converter(s: str) -> int: 
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    running_total = 0
    for idx in range(len(s) - 1): 
        current_value = roman_to_int[s[idx]]
        next_value = roman_to_int[s[idx + 1]]
        
        if current_value >= next_value:
            running_total += current_value
        else: 
            running_total -= current_value
    
    running_total += roman_to_int[s[-1]]
    
    return running_total

print(roman_int_converter(s = "III"))

