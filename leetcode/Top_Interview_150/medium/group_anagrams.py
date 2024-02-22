# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def group_anagrams(strs: list[str]) -> list[list[str]]:

    anagrams = {}

    # Iterate through each string in the array
    for s in strs:
        # Sort the characters of the string to create a key
        sorted_s = ''.join(sorted(s))
        anagrams_list = anagrams.get(sorted_s, [])
        anagrams_list.append(s)
        anagrams[sorted_s] = anagrams_list

    # Return the values of the dictionary, which are lists of grouped anagrams
    return list(anagrams.values())



strs = ["eat","tea","tan","ate","nat","bat"]

print(group_anagrams(strs))
