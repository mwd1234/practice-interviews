# Write a Python function that takes a dictionary of students' names and 
# their corresponding scores, and returns the names of the top three 
# students with the highest scores.

def student_score_calc(input_dict): 
    my_cool_list = []
    for k, v in input_dict.items():
        my_cool_list.append((v,k))
        
    my_cool_list.sort(reverse=True)
    # return my_cool_list[:3] # Score + Student
    return [names[1] for names in my_cool_list[:3]] # Solely student name
    

students_scores = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'David': 95,
    'Eva': 88,
    'Frank': 79,
    'Grace': 91,
    'Hannah': 83,
    'Ian': 87,
    'Julia': 90
}


print(student_score_calc(students_scores))


# Follow-up: What adjustments would you make to handle cases where multiple students may have the same score?

def student_score_calc(input_dict, top_n): 
    my_cool_list = []
    for k, v in input_dict.items():
        my_cool_list.append((v,k))
        
    my_cool_list.sort(reverse=True)

    top_scores = sorted(set(score for score, _ in my_cool_list), reverse=True)[:top_n]

    # Extract names with the top n scores
    top_students = [tup[1] for tup in my_cool_list if tup[0] in top_scores]

    return top_students

students_scores = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'David': 95,
    'Eva': 88,
    'Frank': 79,
    'Grace': 91,
    'Hannah': 83,
    'Ian': 87,
    'Julia': 90,
    'Liam': 95,  # Another student with the same highest score as David
    'Sophia': 93  # Student with a score lower than the two highest scores
}

top_n_students = student_score_calc(students_scores, 3)
print(top_n_students)


