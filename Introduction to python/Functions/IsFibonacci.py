def is_fibonacci(n):
    # Base cases: 0 and 1 are part of the Fibonacci series
    if n == 0 or n == 1:
        return True

    # Initialize the first two numbers of the Fibonacci series
    a, b = 0, 1

    # Generate Fibonacci numbers until the next number is greater than or equal to N
    while b < n:
        # Update the values of a and b by swapping them and calculating the next Fibonacci number
        a, b = b, a + b

    # Check if the given number is equal to the current Fibonacci number
    return b == n

# Example usage:
number_to_check = 4
result = is_fibonacci(number_to_check)
print(f"{number_to_check} is {'a Fibonacci number' if result else 'not a Fibonacci number'}")
