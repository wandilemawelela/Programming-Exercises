# Program to perform list operations
# Author: Wandile Mawelela
# Course: Introduction to Programming
# University of the People

# List of 10 employee names
employees = ["Sipho", "Wandile", "Gcina", "Sandile", "Musa",
             "Msimisi", "Sethu", "Futhi", "Fikile", "Lungile"]

# Split list into two sublists
subList1 = employees[:5]
subList2 = employees[5:]

print("SubList 1:", subList1)
print("SubList 2:", subList2)

# Add a new employee to subList2
subList2.append("Kriti Brown")
print("\nAfter adding new employee to subList2:", subList2)

# Remove the second employee from subList1
removed_employee = subList1.pop(1)
print("Removed employee from subList1:", removed_employee)
print("Updated subList1:", subList1)

# Merge both lists
mergedList = subList1 + subList2
print("\nMerged Employee List:", mergedList)

# Salary list corresponding to employees
salaryList = [35000, 42000, 50000, 47000, 38000, 52000, 45000, 48000, 39000, 41000]

# Apply 4% salary increase
salaryList = [round(s * 1.04, 2) for s in salaryList]
print("\nUpdated Salary List after 4% increase:", salaryList)

# Sort salaries and show top 3
salaryList.sort()
print("Sorted Salary List:", salaryList)
print("Top 3 Salaries:", salaryList[-3:])

