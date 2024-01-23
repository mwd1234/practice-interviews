def most_frequent_last_names(input_list: list, freq: int) -> dict: 
    
    last_name_counts = {}

    # Count occurrences of last names
    for full_name in input_list:
        _, last_name = full_name.split()  # Split the full name into first and last names
        last_name_counts[last_name] = last_name_counts.get(last_name, 0) + 1

    # Sort the dictionary by value (frequency)
    sorted_last_names = sorted(last_name_counts.items(), key=lambda x: x[1], reverse=True)

    # Extract last names from the sorted list
    sorted_last_names = [name for name, freq in sorted_last_names]
    
    # Return the shortest k last names

    shortest_last_names = sorted(sorted_last_names, key=len)[:freq]
    return shortest_last_names



names_list = [
    "John Doe",
    "Alice Johnson",
    "   Bob    White   ",
    "David Brown   ",
    "Jane Doe ",
    "Mary Smith ",
    "Jane Smith",  
]

print(most_frequent_last_names(names_list, 2))



