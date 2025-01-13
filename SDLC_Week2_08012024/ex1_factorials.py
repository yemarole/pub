# Exercise 1: Create variables that consist of names of your fav Cars.

# → Choose Favorite Cars: Decide on the names of your favorite cars that you want to store in
# variables eg: Rolls-Royce, BMW, Tesla, Audi etc.


# → Assign Names to Variables: Create variable “My_Fav_Cars” and assign the corresponding
# name to each variable.

# → Follow Naming Conventions: Ensure that the variable names adhere to Python's naming
# conventions, which typically involve using lowercase letters and underscores for variable
# names.

my_fav_cars = ["BMW", "Audi", "Polestar"]
# print(my_fav_cars)

# Exercise 2: Create variables that consist of the names of your fav Actors.

# → Choose Favorite Actors: Decide on the names of your favorite actors that you want to
# store in variables eg: Ryan Gosling, Timothee Chalamet, Tom Cruise, Leonardo DiCaprio
# etc

# → Assign Names to Variables: Create variable “My_Fav_Actors” and assign the
# corresponding name to each variable.

# → Follow Naming Conventions: Ensure that the variable names adhere to Python's naming
# conventions, which typically involve using lowercase letters and underscores for variable
# names.

my_fav_actors = ["Johnny Depp", "Denzel Washington", "Leo Di Caprio"]
# print(my_fav_actors)


# "Write a Python function to calculate the factorial of a given number."
def factorial(n):
    """
    Calculate the factorial of a given number.

    Parameters:
    n (int): The number to calculate the factorial for.

    Returns:
    int: The factorial of the given number.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


# Main program
def main():
    # Input: Number from the user
    try:
        num = int(input("Enter a non-negative integer to calculate its factorial: "))

        # Calculate the factorial using the custom function
        fact = factorial(num)

        # Display the result
        print(f"The factorial of {num} is: {fact}")
    except ValueError as e:
        print(f"Error: {e}")


# Run the program
if __name__ == "__main__":
    main()
