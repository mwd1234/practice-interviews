def is_anagram(s: str, t: str) -> bool:
    s_dict = {}
    t_dict = {}
    
    for char in s.lower(): 
        s_dict[char] = s_dict.get(char, 0) + 1
    
    for char in t.lower(): 
        t_dict[char] = t_dict.get(char, 0) + 1

    return s_dict == t_dict

s = "anagram"
t = "nagaram"

print(is_anagram(s, t))