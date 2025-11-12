# Original dictionary containing students and their enrolled courses
students_dict = {
    'Stud1': ['CS1101', 'CS2402', 'CS2001'],
    'Stud2': ['CS2402', 'CS2001', 'CS1102']
}

# Function to invert the dictionary
def invert_dictionary(d):
    inverted = {}  # Create an empty dictionary for the inverted result
    for student, courses in d.items():  # Iterate through each student and their courses
        for course in courses:  # Loop through each course for the current student
            if course not in inverted:  # If course is not already a key, create it
                inverted[course] = [student]
            else:
                inverted[course].append(student)  # Add student to the existing course list
    return inverted

# Printing the original and inverted dictionaries
print("Original Dictionary:")
print(students_dict)
print("\nInverted Dictionary:")
inverted_dict = invert_dictionary(students_dict)
print(inverted_dict)

