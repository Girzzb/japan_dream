# Exercise 2: Check even/odd, divisible by 5, and positive/negative
number = int(input("Enter a number: "))
# Check even/odd
parity = "even" if number % 2 == 0 else "odd"
# Check divisibility by 5
div_by_5 = "divisible by 5" if number % 5 == 0 else "not divisible by 5"
# Check positive/negative
sign = "positive" if number > 0 else "negative" if number < 0 else "zero"
# Display the result
print(f"Number {number} is {parity}, {div_by_5}, and ")

# Exercise 3: Number Guessing Game
print("Number guessing game (1-10)")
# Secret number
secret = 7
# Guess count variable
tries = 0
# Maximum number of guesses
max_tries = 5

while tries < max_tries:
    tries += 1
    guess = int(input(f"Attempt {tries}/{max_tries} (1-10): "))

    if guess == secret:
        print(f"Correct! You guessed it in {tries} tries!")
        break
    elif guess < secret:
        print("Guess higher")
    elif guess > secret:
        print("Guess lower")

if tries == max_tries and guess != secret:
    print(f"Game Over! The secret number was {secret}.")

# Exercise 4: Reverse Star Pyramid
for i in range(5, 0, -1):
    print("*" * i) 
