# Given an integer array nums and an integer k, return true if there are two distinct 
# indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    num_holder = {}

    for idx, num in enumerate(nums): 
        if num in num_holder and idx - num_holder[num] <= k: 
            return True
        num_holder[num] = idx



nums = [1,2,3,1]
k = 3

print(contains_nearby_duplicate(nums, k))