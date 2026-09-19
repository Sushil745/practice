# Create the tuple
marks = (78, 85, 90, 67, 88)

# 1. Display first and last values
print("First value:", marks[0])
print("Last value:", marks[-1])

# 2. Display values from index 1 to 3
print("Values from index 1 to 3:", marks[1:4])

# 3. Find highest and lowest marks
print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))

# 4. Convert tuple into a list
marks_list = list(marks)
print("List:", marks_list)

# 5. Add 95 to the list
marks_list.append(95)
print("Updated list:", marks_list)

# 6. Convert updated list back into a tuple
marks = tuple(marks_list)
print("Updated tuple:", marks)