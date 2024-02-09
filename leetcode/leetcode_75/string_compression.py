# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, 
# be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    counter = 1
    new_list = []

    for idx, char in enumerate(chars):
        if idx < len(chars) - 1:
            if char == chars[idx + 1]:
                counter += 1
            else: 
                if counter > 1: 
                    new_list.append(char)
                    while counter > 10: 
                        new_list.append(1)
                        counter -= 10

                    new_list.append(counter)

                else: 
                    new_list.append(char)

                counter = 1
        else:
            if counter > 1: 
                new_list.append(char)
                while counter > 10: 
                    new_list.append(1)
                    counter -= 10

                new_list.append(counter)
            else: 
                new_list.append(char)

    return new_list, len(new_list)
    
chars = ["a","a","b","b","c","c","c"]

# chars = ["a"]

# chars = ["a","b","b","b","b","b","b","b","b","b","b","b", "b"]

print(compress(chars))

