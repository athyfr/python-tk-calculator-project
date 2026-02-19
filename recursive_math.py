# Recursive algorithms are implemented in this file

# Defined to be accurate based on en.wikipedia.org/wiki/Factorial
# Since negative factorials are not possible, -1 is returned in those
#   cases to indicate an error.
def factorial(n: int) -> int:
    # If n is negative, return -1 to indicate error.
    if n < 0:
        raise ValueError("Negative number does not have a factorial.")
    if n != int(n):  # Supports duck-typing (e.g. integral float)
        raise ValueError("Factorial function only supports integers.")
    # If n is 0 or 1, return 1, as that is correct in that case.
    if n == 0 or n == 1:
        return 1

    # Calculate factorial using recursion
    factorial: int = 1

    for i in range(2, n + 1):
        factorial *= i

    return factorial
