# Program to display your name and perform string operations

# Input name from user
name = input("Please enter your name: ")

# Input number of characters to display
chars = int(input("Enter the number of characters to display: "))

# Validate that chars is not more than the name length
if chars > len(name):
    print("The number entered exceeds the length of your name.")
    print("Displaying the full name instead.\n")
    chars = len(name)

# Display n characters from the left
print("First", chars, "characters:", name[:chars])

# Count vowels (case-insensitive)
vowel_count = sum(1 for ch in name.lower() if ch in "aeiou")
print("Number of vowels:", vowel_count)

# Display the reversed name
print("Reversed name:", name[::-1])

