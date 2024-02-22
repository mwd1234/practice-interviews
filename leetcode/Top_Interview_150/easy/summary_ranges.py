# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
# That is, each element of nums is covered by exactly one of the ranges, and there is 
# no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b

def summary_ranges(nums: list[int]) -> list[str]:
    if len(nums) == 0: 
        return []
    
    range_list = []
    output = []
    
    # instantiate with [[0,0]]
    range_list.append([nums[0], nums[0]])

    for idx in range(1, len(nums)): 
        # compare second element in list + 1 to see if it's contiguous 
        if nums[idx] == range_list[len(range_list) - 1][1] + 1: 
            # update the second element if it is
            range_list[len(range_list) - 1][1] = nums[idx]
        else: 
            # make a new list of nums[idx]
            range_list.append([nums[idx], nums[idx]])

    # This is the format LeetCode expects
    for ranges in range_list:
        if ranges[0] == ranges[1]: 
            output.append(str(ranges[0]))
        else: 
            output.append(f"{ranges[0]}->{ranges[1]}")

    # LeetCode expected return ["0","2->4","6","8->9"]
    return output


nums = [0,2,3,4,6,8,9]

print(summary_ranges(nums))