# random integer (1-100), find biggest and smallest
import random

numbers = []

for i in range(8):
    numbers.append(random.randint(1, 100))

print("Numbers:", numbers)

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Biggest number:", largest)
print("Smallest number:", smallest)
