# Create student dictionary
student = {
    "Name": "Rahul",
    "Roll Number": 101,
    "Course": "B.Tech CSE",
    "Marks": 85
}

# 1. Display all student details
print("Student Details:")
print(student)

# 2. Add student's city
student["City"] = "Delhi"

# 3. Update marks
student["Marks"] = 92

# 4. Display all keys
print("\nKeys:")
print(student.keys())

# Display all values
print("\nValues:")
print(student.values())

# 5. Iterate through dictionary
print("\nKey-Value pairs:")

for key, value in student.items():
    print(key, ":", value)