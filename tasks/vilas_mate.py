
# Calculate Student Total and Percentage

# Accept student details
name = input("Enter Student Name: ")

# Accept marks of three subjects
subject1 = float(input("Enter marks of Subject 1: "))
subject2 = float(input("Enter marks of Subject 2: "))
subject3 = float(input("Enter marks of Subject 3: "))

# Calculate total marks
total = subject1 + subject2 + subject3

# Calculate percentage
percentage = total / 3

# Display student result
print("\n----- Student Result -----")
print("Student Name:", name)
print("Subject 1 Marks:", subject1)
print("Subject 2 Marks:", subject2)
print("Subject 3 Marks:", subject3)
print("Total Marks:", total)
print("Percentage:", round(percentage, 2), "%")
