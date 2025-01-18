"""
Given two integers M and N, calculate and return their multiplication using recursion.
You can only use subtraction and addition for your calculation. No other operators are allowed.
Input: 2 5
Output: 10
"""

from sys import setrecursionlimit


def multiply(f_number, s_number):
    if f_number == 0 or s_number == 0:
        return 0
    if s_number > 0:
        small_ans = multiply(f_number, s_number - 1)
        return small_ans + f_number
    else:
        small_ans = multiply(f_number, s_number + 1)
        return small_ans - f_number


setrecursionlimit(1100)
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
print(multiply(first_number, second_number))
