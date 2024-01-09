# Design a function that removes duplicates from a list and returns a new list with unique elements.

def remove_dupes(input_list): 
    return list(set(input_list))

my_list = [
    "hello",
    "I",
    "am",
    "I",
    "list",
    "list",
    "hello"
]

print(remove_dupes(my_list))


# ChatGPT's Answer: 
def remove_duplicates(input_list):
    return list(set(input_list))

# Test the remove_duplicates function
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(my_list)
print(f'Original list: {my_list}')
print(f'List with duplicates removed: {unique_list}')