"""
Program to find the factorial of a number using recursion
"""


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


number = int(input("Enter the number to find the factorial of the number"))
fact = factorial(number)
print(fact)
