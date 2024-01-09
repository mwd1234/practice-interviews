# Write a Python function that calculates the factorial of a given number

def calc_factorial(input_num):
    # 5! = 5x4x3x2x1
    # Get every number in descending order down to 2
    # Check if number is 0 or 1 since they equal 1
    
    num_holder = 1
    
    if input_num == 0 or input_num == 1: 
        return 1
    
    for i in range(1, input_num + 1): 
        num_holder = i*num_holder
        
    return num_holder

print(calc_factorial(5))

# ChatGPT's Answer: 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test the factorial function
number = 5
print(f'The factorial of {number} is {factorial(number)}')
