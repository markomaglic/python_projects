def reverse_string(s):
    """
    Reverses the input string.

    Args:
        s (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    return s[::-1]

def count_unique(numbers):
    """
    Counts the number of unique elements in a list of integers.

    Args:
        numbers (list): List of integers.

    Returns:
        int: Count of unique integers.
    """
    return len(set(numbers))

def return_unique(numbers):
    return set(numbers)

def sum_even(n):
    """
    Calculates the sum of all even numbers up to and including n.

    Args:
        n (int): The upper limit.

    Returns:
        int: Sum of even numbers.
    """
    return sum(x for x in range(2, n + 1, 2))

def write_and_read_file():
    """
    Writes a string to a file, then reads and returns the content.

    Returns:
        str: Content of the file.
    """
    # Step 1: Write to the file
    with open("greeting.txt", "w") as file:
        file.write("Hello, TestDome!")

    # Step 2: Read from the file
    with open("greeting.txt", "r") as file:
        content = file.read()

    return content

def factorial_recursive(n):
    """
    Calculates the factorial of a number using recursion.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: Factorial of n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def filter_and_sum_evens(numbers):
    """
    Filters even numbers from a list and returns their sum.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The sum of even numbers in the list.
    """
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:  # Check if the number is even
            even_sum += num
    return even_sum


if __name__ == "__main__":
    # Test reverse_string
    print(reverse_string("Python"))  # Output: "nohtyP"

    # Test count_unique
    print(count_unique([1, 1, 2, 3, 5, 5]))  # Output: 4

    # Test sum_even
    print(sum_even(7))  # Output: 12 (2 + 4 + 6)

    #Test return_unique
    print(return_unique([1, 1, 2, 3, 5, 5]))

    #Test write_and_read_file
    result = write_and_read_file()
    print(result)  # Output: "Hello, TestDome!"

    #Test factorial
    print(factorial_recursive(5))  # Output: 120
