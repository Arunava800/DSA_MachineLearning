"""
Program to find teh power of a number.
Take 'N' and 'x' from the user  and print the answer as (x^N).

"""


def power_n(x, n):
    if n == 0:
        return 1
    return x * power_n(x, n-1)


base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
power = power_n(base, exponent)
print(power)
