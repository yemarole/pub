# #Raw Code Concept
# number = 0
# if number % 2:
#     print("Number is even")
# else:
#     print("Number is odd")

# #Make it into a terminal program
# def check_even_odd(number):
#     if number % 2 == 0:
#         print("Number is even")
#     else:
#         print("Number is odd")


# # Example usage
# if __name__ == "__main__":
#     num = int(input("Enter a number: "))
#     check_even_odd(num)

# # If_else statement
# fav_food = [1, 2, 4]
# if fav_food == []:
#     print("The favourite food list is empty")
# else:
#     print("The favourite food list is not empty")

# # While loop
# i = 1
# while i < 5:
#     print(i)
#     i *= 2

import random

number = random.randint(1, 10)  # Generate a random number between 1 and 10 (inclusive)

# Allow the user three attempts to guess the number
for _ in range(3):

    # Get a guess from the user
    guess = int(input("Guess a number: "))

    # Check if the guess is correct
    if guess == number:
        print("Correct!")
        break  # Exit the loop if the guess is correct
    elif guess < number:
        print("Try a higher number")
    else:
        print(
            "Try a lower number"
        )  # Prompt the user to try again if the guess is incorrect
else:  # If the loop completes three iterations without a correct guess, print "Game over"
    print("Game over, the number was", number)
