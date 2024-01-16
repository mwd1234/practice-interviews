# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that 
# each unique element appears only once. The relative order of the elements should be kept the same. 
# Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were
# present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.

nums = [0,0,1,1,1,2,2,3,3,4]

def remove_duplicates(nums: list[int]) -> int:
    
    # counter = len(nums) - len(list(set(nums)))   
    
    unique_counter = 1
    for num in range(1, len(nums)): 
        if nums[num] != nums[num - 1]: 
            nums[unique_counter] = nums[num]
            unique_counter += 1
            
    return unique_counter

print(remove_duplicates(nums))
