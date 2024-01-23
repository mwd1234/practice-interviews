def generate_pyramid_numbers(target_values):
    pyramid = []
    current_number = 1
    total_values = 0

    # Continue generating rows until the total values reach or exceed the target
    while total_values < target_values:
        row = list(range(current_number, current_number + len(pyramid) + 1))

        pyramid.append(row)

        # Update the current number by adding the length of the generated row
        current_number += len(row)

        # Update the total values count by adding the length of the generated row
        total_values += len(row)

    return pyramid


def extract_last_numbers(pyramid):
    last_numbers = [row[-1] for row in pyramid]
    return last_numbers


def decode_message(message_file: str):
    number_word_dict = {}

    # Read the contents of the file and extract the number/word pairs
    with open(message_file, 'r') as file:
        num_lines = len(file.readlines())

        file.seek(0)  # Reset the file pointer to the beginning
        for line in file:
            # Split each line into number and word
            parts = line.strip().split()
            
            
            if len(parts) >= 2:
                number_word_dict[int(parts[0])] = parts[1]
            else: 
                raise ValueError("Invalid format: Each line must contain at least two parts.")

        # Creates a pyramid list based on criteria
        pyramid = generate_pyramid_numbers(num_lines)
        # Creates a list of the last number per each pyramid row
        last_numbers = extract_last_numbers(pyramid)

    # Extract the words corresponding to the last numbers in each row
    decoded_words = [number_word_dict[number] for number in last_numbers]

    # Join the words to form the decoded message
    decoded_message = ' '.join(decoded_words)

    return decoded_message

# Example usage:


message_file_path = '/Users/matthew.dembinski/Documents/Development/practice-interviews/data/coding_assessment.txt'
decoded_message = decode_message(message_file_path)

# # Print the pyramid
# for row in pyramid:
#     print(row)

# Print the decoded message
print("Decoded Message:", decoded_message)











