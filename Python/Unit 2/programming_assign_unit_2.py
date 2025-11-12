# Function to calculate and print the circumference of a circle
# Formula: circumference = 2 * π * r
# Here π is approximated as 3.14159

def print_circum(radius):
    circum = 2 * 3.14159 * radius  # calculate circumference
    print(circum)  # print the result

# Call the function with different radius values
print_circum(23)  # radius = 23 → output: 144.51314
print_circum(19)  # radius = 19 → output: 119.38044
print_circum(7)   # radius = 7  → output: 43.98226

