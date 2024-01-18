# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

def majority_element(nums: list[int]) -> int:
    num_holder = {}
    for num in nums: 
        if num in num_holder: 
            num_holder[num] += 1
        else: 
            num_holder[num] = 1
    
    for k, v in num_holder.items():
        if v > len(nums) / 2: 
            return k

nums = [2,2,1,1,1,2,2]
nums = [3,2,3]
print(majority_element(nums))