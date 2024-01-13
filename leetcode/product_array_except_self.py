# Given an integer array nums, return an array answer such that answer[i] is equal to the product 
# of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

def product_except_self(nums: list[int]) -> list[int]:
    product_holder = []
    for idx, num in enumerate(nums): 
        product_holder_val = 1
        if idx == 0: 
            product = nums[idx + 1:]
        else: 
            product = nums[0:idx] + nums[idx + 1:]
    
        for num in product:
            product_holder_val *= num
    
        product_holder.append(product_holder_val)
    
    return product_holder

    
    
nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
print(product_except_self(nums))

# ChatGPT's Answer: 

def product_except_self(nums):
    n = len(nums)

    # Initialize two arrays to store products to the left and right of each element.
    left_products = [1] * n
    right_products = [1] * n

    # Calculate products to the left of each element.
    left_product = 1
    for i in range(1, n):
        left_product *= nums[i - 1]
        left_products[i] = left_product

    # Calculate products to the right of each element.
    right_product = 1
    for i in range(n - 2, -1, -1):
        right_product *= nums[i + 1]
        right_products[i] = right_product

    # Multiply left and right products to get the final result.
    result = [left_products[i] * right_products[i] for i in range(n)]

    return result

# Example usage:
nums = [1, 2, 3, 4]
result = product_except_self(nums)
print(result)