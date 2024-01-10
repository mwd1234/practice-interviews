# Create a Python function that takes a list of integers as input and 
# returns a new list containing only the even numbers squared. 
# For example, given [1, 2, 3, 4, 5], the function should return [4, 16].

def even_squares(input_list):
    even_holder = []
    for num in input_list: 
        if num % 2 == 0:
           even_holder.append(num*num)
    
    return even_holder

my_list = [1, 2, 3, 4, 5]
print(even_squares(my_list))

# Follow-up: What modifications would you make to the function to handle 
# negative numbers or zero in the input list?

def even_squares(input_list):
    even_holder = []
    for num in input_list: 
        if num % 2 == 0:
           even_holder.append(num*num)
    
    return list(set(even_holder))

my_list = [1, 2, 3, 4, 5, -4, 0]
print(even_squares(my_list))

# As a list comprehension

def even_squares(input_list):
    even_holder = list(set([num*num for num in input_list if num % 2 == 0]))

    return even_holder

my_list = [1, 2, 3, 4, 5, -4, 0]
print(even_squares(my_list))
