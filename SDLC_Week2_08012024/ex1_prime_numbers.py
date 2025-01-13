# "Write a Python program to find all prime numbers within a given range.


def is_prime(num):
    """
    Check if a number is prime.

    Parameters:
    num (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def find_primes_in_range(start, end):
    """
    Find all prime numbers within a given range.

    Parameters:
    start (int): The starting number of the range.
    end (int): The ending number of the range.

    Returns:
    list: A list of prime numbers within the range.
    """
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


# Main program
def main():
    # Input: Range from the user
    start = int(input("Enter the starting number of the range: "))
    end = int(input("Enter the ending number of the range: "))

    # Find prime numbers in the range
    primes = find_primes_in_range(start, end)

    # Display the result
    if primes:
        print(
            f"Prime numbers between {start} and {end} are: {', '.join(map(str, primes))}"
        )
    else:
        print(f"There are no prime numbers between {start} and {end}.")


# Run the program
if __name__ == "__main__":
    main()
