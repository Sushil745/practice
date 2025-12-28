#take list values from user
numbers = [12, 45, 3, 98, 7, 34, 21]

count = 0

# a) print each number
print("All numbers:")
for num in numbers:
    print(num)

# b) print only numbers greater than 30
print("\nNumbers greater than 30:")
for num in numbers:
    if num > 30:
        print(num)
        count += 1

# c) count how many numbers are greater than 30
print("\nCount of numbers greater than 30:", count)
