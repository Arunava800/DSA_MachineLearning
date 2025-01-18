"""
Write a recursive program to find the sum of the digits.
Input: 12345
Output: 15
"""


def sum_of_digits(number: int) -> int:
    if number == 0:
        return 0
    remainder = number % 10
    return remainder + sum_of_digits(number//10)


n = int(input("Enter a number: "))
print(sum_of_digits(n))
