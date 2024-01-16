# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the 
# array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.


def can_jump(nums: list[int]) -> bool: 
    max_reach = 0 
    
    first_jump = nums[0]    
    if first_jump > len(nums): 
        return True

    for i, num in enumerate(nums): 
        if i > max_reach:
            return False
        
        max_reach = max(max_reach, i + num)
        
        if max_reach >= len(nums) - 1: 
            return True    
    
    return False

nums = [2,3,1,1,4]
nums = [3,2,1,0,4]

print(can_jump(nums))