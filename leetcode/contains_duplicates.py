# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

def contains_dupes(input_list): 
    return len(input_list) != len(set(input_list))

nums = [1,2,3,1]
nums = [1,2,3,4]
nums = [1,1,1,3,3,4,3,2,4,2]
nums = [3,1]

print(contains_dupes(nums))