# Implement a Python function that takes a list of integers and returns 
# the maximum product of three integers in the list.

def max_product(input_list: list, prod_of_n: int):
    max_prod = 1
    input_list.sort(reverse=True)
    
    for num in input_list[:prod_of_n]: 
        max_prod *= num
    
    return max_prod

print(max_product([1, 2, 3, 4, 5], 3))

# Follow-up: How would you modify your function to handle cases 
# where negative integers are present in the list? 
# Can you optimize its time complexity?

# ChatGPT's Answers: 

def max_product(input_list: list, prod_of_n: int):
    if len(input_list) < prod_of_n:
        return "Invalid input: List length is less than prod_of_n"

    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')

    for num in input_list:
        if num > max1:
            max3, max2, max1 = max2, max1, num
        elif num > max2:
            max3, max2 = max2, num
        elif num > max3:
            max3 = num

        if num < min1:
            min2, min1 = min1, num
        elif num < min2:
            min2 = num

    pos_prod = max1 * max2 * max3
    neg_pos_prod = min1 * min2 * max1

    return max(pos_prod, neg_pos_prod) if prod_of_n == 3 else pos_prod

# Example usage:
print(max_product([1, 2, 3, 4, 5], 3))


def max_product(input_list: list, prod_of_n: int):
    if len(input_list) < prod_of_n:
        return "Invalid input: List length is less than prod_of_n"

    top_integers = [float('-inf')] * prod_of_n  # Initialize a list to hold the top prod_of_n integers

    for num in input_list:
        for i, top_num in enumerate(top_integers):
            if num > top_num:
                top_integers[i+1:] = top_integers[i:-1]  # Shift elements to the right
                top_integers[i] = num
                break

    max_product = 1
    for num in top_integers:
        max_product *= num

    return max_product

# Example usage:
print(max_product([1, 5, 3, 4, 2], 3))

