"""
Given a number `n`, find the fibonacci to nth terms
"""


def fibonacci_recursion(n):
    if n == 0 or n == 2:
        return 0
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)


number = int(input("Enter the number: "))
n_fib = fibonacci_recursion(number)
print(n_fib)
