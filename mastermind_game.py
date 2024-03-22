import random

colors = ["White", "Red", "Blue", "Pink", "Orange", "Green"]
code_length = 3
max_attempts = 10

code = random.choices(colors, k=code_length)
attempts = 0

print("Welcome to the Mastermind Game!")
print("Available colors: {}".format(", ".join(colors)))
print("Code length: {}, Max attempts: {}".format(code_length, max_attempts))

while attempts < max_attempts:
    guess = input("Attempt {}/{}, enter your guess: ".format(attempts + 1, max_attempts)).strip().split()
    if len(guess) != code_length or not all(color in colors for color in guess):
        print("Invalid guess! Make sure you have exactly three colors.")
        continue

    correct_position = sum(g == c for g, c in zip(guess, code))
    correct_color = sum(min(guess.count(c), code.count(c)) for c in set(code))
    correct_color -= correct_position

    print("{} colors placed correctly!".format(correct_position))
    print("{} correct colors placed in wrong positions!".format(correct_color))

    if correct_position == code_length:
        print("\nCongratulations! You won.")
        exit()

    attempts += 1

print("\nYou have lost! The code was {}".format(code))
