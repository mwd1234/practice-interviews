# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.




def two_sum(nums: list[int], target: int) -> list[int]:
    num_holder = {}
    compliment = 0
    
    for idx, num in enumerate(nums): 
        compliment = target - num
        if compliment in num_holder:
            return [idx, num_holder[compliment]]
        else:
            num_holder[num] = idx 

    return 

nums = [2,7,11,15]
target = 9

nums = [3,2,4]
target = 6

nums = [3,3]
target = 6

print(two_sum(nums, target))