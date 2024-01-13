# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

nums = [2,7,11,15]
target = 9
nums = [3,2,4]
target = 6
nums = [3,3]
target = 6

def two_sums(input_list: list, target: int) -> tuple:
    num_holder = {}
    
    for idx, num in enumerate(input_list):
        complement = target - num
        
        if complement in num_holder:
            return (num_holder[complement], idx)
        else: 
            num_holder[complement] = idx

print(two_sums(nums, target))