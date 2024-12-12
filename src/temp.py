
# Function to calculate the average of a list
def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers) if numbers else 0

# Function to sort the list in ascending order
def sort_numbers(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                # Swap the numbers
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

# Function to find the maximum number
def find_max(numbers):
    max_num = numbers[0] if numbers else None
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Function to find the minimum number
def find_min(numbers):
    min_num = numbers[0] if numbers else None
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

# Example data
numbers = [12, 3, 5, 7, 19, 10, 21, 15]

# Perform the operations
average = calculate_average(numbers)
sorted_numbers = sort_numbers(numbers[:])  # Passing a copy to preserve original list
max_number = find_max(numbers)
min_number = find_min(numbers)

# Print results
print("Original numbers:", numbers)
print("Average:", average)
print("Sorted numbers:", sorted_numbers)
print("Maximum number:", max_number)
print("Minimum number:", min_number)
