""" Reverse a String
Write a function reverse_string(s) that takes a string s and returns the string reversed.

Count Unique Elements
Write a function count_unique(numbers) that takes a list of integers and returns the count of unique integers.

Sum Even Numbers
Write a function sum_even(n) that calculates the sum of all even numbers up to and including n. """

def reverse_string(s):
    """
    Reverses the input string.

    Args:
        s (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    return s[::-1]

# Example usage
print(reverse_string("hello"))  # Output: "olleh"

def count_unique(numbers):
    """
    Counts the number of unique elements in a list of integers.

    Args:
        numbers (list): List of integers.

    Returns:
        int: Count of unique integers.
    """
    return len(set(numbers))

# Example usage
print(count_unique([1, 2, 2, 3, 4, 4]))  # Output: 4

def sum_even(n):
    """
    Calculates the sum of all even numbers up to and including n.

    Args:
        n (int): The upper limit.

    Returns:
        int: Sum of even numbers.
    """
    return sum(x for x in range(2, n + 1, 2))


if __name__ == "__main__":
    # Test reverse_string
    print(reverse_string("Python"))  # Output: "nohtyP"

    # Test count_unique
    print(count_unique([1, 1, 2, 3, 5, 5]))  # Output: 4

    # Test sum_even
    print(sum_even(7))  # Output: 12 (2 + 4 + 6)
