# Create a Python program that reads a text file ('data.txt') containing integers 
# separated by commas. 
# Write a function that reads this file, converts the strings to integers, 
# calculates their sum, and handles any exceptions that may arise.

def sum_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read().strip().split(',')
            content_as_ints = [int(num) for num in content]
            print(content_as_ints)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except ValueError:
        print("Error: The file contains non-integer values.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
sum_from_file('/Users/matthew.dembinski/Documents/Development/practice-interviews/data/data.txt')