# "Implement a program to check whether a given string is a palindrome or not."


def reverse_string(input_str):
    """
    Reverse a given string without using built-in reverse functions.

    Parameters:
    input_str (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    reversed_str = ""
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str


def is_palindrome(input_str):
    """
    Check whether a given string is a palindrome.

    Parameters:
    input_str (str): The string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_str = input_str.replace(" ", "").lower()

    # Reverse the cleaned string
    reversed_str = reverse_string(cleaned_str)

    # Compare the cleaned string with its reverse
    return cleaned_str == reversed_str


# Main program
def main():
    # Input: String from the user
    input_str = input("Enter a string: ")

    # Reverse the string using the custom function
    reversed_str = reverse_string(input_str)

    # Check if the string is a palindrome
    if is_palindrome(input_str):
        palindrome_result = "is a palindrome"
    else:
        palindrome_result = "is not a palindrome"

    # Display the results
    print(f"Original string: {input_str}")
    print(f"Reversed string: {reversed_str}")
    print(f"The string '{input_str}' {palindrome_result}.")


# Run the program
if __name__ == "__main__":
    main()
