# # Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longestCommonPrefix(strs: list[str]) -> str:

    for i in range(len(strs[0])):
        # Check if the character at index i is the same in all strings
        for string in strs[1:]:
            if i >= len(string) or string[i] != strs[0][i]:
                return strs[0][:i]
    
    return strs[0]

strs = ["flower","flow","flight"]

print(longestCommonPrefix(strs))