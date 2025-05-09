# Exercise 1: Calculate Average of a List
numbers = [4, 8, 15, 16, 23, 42]
total = sum(numbers)  # Sum all numbers
count = len(numbers)  # Count numbers
average = total / count  # Calculate average
print(f"The average is {average}.\n")  # Print result

# Exercise 2: Find Maximum in a List (Using Loop)
numbers = [7, 2, 9, 4, 6, 1, 3, 8, 5]
max_num = numbers[0]  # Start with first number
for num in numbers:
    if num > max_num:
        max_num = num  # Update if larger
print(f"The maximum is {max_num}\n")

# Exercise 2: Find Maximum in a List (Using max())
numbers = [7, 2, 9, 4, 6, 1, 3, 8, 5]
max_num = max(numbers)  # Find maximum using max()
print(f"The maximum is: {max_num}\n")

# Alternative using loop (for understanding):
# max_num = numbers[0]
# for num in numbers:
#     if num > max_num:
#         max_num = num

# Exercise 3: Count Character Frequency
text = "banana"
freq = {}  # Empty dictionary
for char in text:
    if char in freq:
        freq[char] += 1  # Increment count
    else:
        freq[char] = 1  # Start count at 1
print(f"Character frequency: {freq}\n")

# Exercise 4: Count Word Frequency
words = ["apple", "banana", "apple", "cherry"]
word_count = {}  # Empty dictionary to store word counts
for word in words:
    if word in word_count:
        word_count[word] += 1  # Increment count
    else:
        word_count[word] = 1  # Start count at 1
for key, value in word_count.items():
    print(f"{key}: {value}")  # Print word and its frequency
    print(f"{key}: {value}")
    print()  # Newline

# Exercise 5: Function to Calculate Average
def calculate_average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    count = len(numbers)
    return total / count
# Test the function
test_numbers = [4, 8, 15, 16, 23, 42]
avg = calculate_average(test_numbers)
print(f"The average is:{avg}\n")

# Exercise 6: Function to Find Maximum
def find_maximum(numbers):
    if not numbers:
        return None  # Return None for empty list
    max_num = max(numbers)  # Find maximum using max()
    return max_num  # Return maximum value

test_numbers = [7, 2, 9, 4, 6, 1, 3, 8, 5]
max_val = find_maximum(test_numbers)
print(f"The maximum is: {max_val}\n")