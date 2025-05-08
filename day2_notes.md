## Day 2: Python

- Exercise 2: Using % to check even/odd and divisible by 3
- Ternary operator: shorter than if/else

## Day 2: Python

- Completed the exercise to check even/odd and divisible by 5!
- Gained a better understanding of % and ternary operator
- Issue: [ternary]

# Exercise 2: Check even/odd, divisible by 3, and positive/negative

number = int(input("Enter a number: ")) # Get number from user

# Check even/odd

parity = "even" if number % 2 == 0 else "odd"

# Check divisible by 3

div_by_3 = "divisible by 3" if number % 3 == 0 else "not divisible by 3"

# Check positive/negative

sign = "positive" if number > 0 else "negative" if number < 0 else "zero"

# Display result

print(f"{number} is {parity}, {div_by_3}, and {sign}")

number = int(input("Enter a number: "))
parity = "even" if number % 2 == 0 else "odd"
div_by_5 = "divisible by 5" if number % 5 == 0 else "not divisible by 5"
sign = "positive" if number > 0 else "negative" if number < 0 else "zero"
print(f"Number {number} is {parity} and {div_by_5} by 5")

## print("Number guessing game (1-10)")

# Secret number

secret = 7

# Guess count variable

tries = 0

# Maximum number of guesses

max_tries = 5

while tries < max_tries:

    # Increment tries
    tries += 1

    # Get user's guess
    guess = int(input(f"Attempt {tries}/{max_tries} (1-10): "))

    # Check the guessed number
    if guess == secret:
        print(f"Correct! You guessed it in {tries} tries!")
        break
    elif guess < secret:
        print("Guess higher!")
    else:
        print("Guess lower!")

# If all attempts are used and still incorrect

if tries == max_tries and guess != secret:
print(f"Game Over! The secret number was {secret}.")

## Day 2: Python

- Exercise 3: Number guessing game
  - Used while loop, if/elif/else, and break
  - Issue: Forgot condition for guess > secret
  - Learned: Counting tries and loop control

## Day 2: Git

- Pushed day2.py to GitHub
- Commands: git add, git commit, git push

## Day 2: Python

- Exercise 4: Reverse Star Pyramid

  - Used for loop and string multiplication to print a reverse pyramid
  - Learned range(start, stop, step) with negative step

  ## Day 2: Git

- Pushed day1.py, day2.py, day1_notes.md, day2_notes.md to GitHub
- Used English comments for professional portfolio
- Commands: git init, git add, git commit, git push
- Issues:
  - Got "not a git repository" error, fixed with git init
  - Got "src refspec main does not match any" error, fixed by using branch main
  - Set up Personal Access Token with 30-day expiration, japan_dream access
