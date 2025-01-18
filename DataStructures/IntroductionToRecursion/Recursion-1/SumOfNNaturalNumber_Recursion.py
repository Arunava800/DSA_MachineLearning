"""
Find the sum of first N natural numbers
"""


def addition(n):
    if n == 0:
        return 0
    else:
        return n + addition(n-1)


number = int(input("Enter the number: "))
summ = addition(number)
print(summ)