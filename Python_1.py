# Import the random module to generate random numbers
import random

# Create an empty list to store the random numbers
numbers = []

# Generate 100 random numbers between 0 and 1000
for i in range(100):
    # Append a random integer between 0 and 1000 to the list
    numbers.append(random.randint(0, 1000))

# Create a copy of the original list to sort it manually
sorted_numbers = numbers.copy()

# Implement a sorting algorithm
for i in range(len(sorted_numbers)):
    # Loop through the list up to the unsorted portion
    for j in range(0, len(sorted_numbers) - i - 1):
        # Compare adjacent elements
        if sorted_numbers[j] > sorted_numbers[j + 1]:
            # Swap elements if they are in the wrong order
            temp = sorted_numbers[j]
            sorted_numbers[j] = sorted_numbers[j + 1]
            sorted_numbers[j + 1] = temp

# Initialize variables to calculate sum and count of even numbers
even_sum = 0
even_count = 0

# Initialize variables to calculate sum and count of odd numbers
odd_sum = 0
odd_count = 0

# Iterate through the sorted list to separate even and odd numbers
for num in sorted_numbers:
    # Check if the number is even
    if num % 2 == 0:
        # Add to even sum
        even_sum += num
        # Increment even count
        even_count += 1
    else:
        # Add to odd sum
        odd_sum += num
        # Increment odd count
        odd_count += 1

# Calculate the average of even numbers (avoid division by zero)
even_avg = even_sum / even_count if even_count != 0 else 0

# Calculate the average of odd numbers (avoid division by zero)
odd_avg = odd_sum / odd_count if odd_count != 0 else 0

# Print the sorted list
print("Sorted list:", sorted_numbers)

# Print the average of even numbers
print("Average of even numbers:", even_avg)

# Print the average of odd numbers
print("Average of odd numbers:", odd_avg)