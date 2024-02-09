# There are n kids with candies. You are given an integer array candies, where each candies[i]
# represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, 
# they will have the greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.


def kids_with_candies(candies, extra_candies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
    
    return_list = []

    # for candy_amt in candies:
    #     if candy_amt + extra_candies >= max(candies):
    #         return_list.append(True)
    #     else: 
    #         return_list.append(False)

    
    for candy_amt in candies:
        return_list.append(True if candy_amt + extra_candies >= max(candies) else False)


    return return_list


candies = [2,3,5,1,3]
extra_candies = 3


candies = [4,2,1,1,2]
extra_candies = 1

candies = [12,1,12]
extra_candies = 10

print(kids_with_candies(candies, extra_candies))
    
