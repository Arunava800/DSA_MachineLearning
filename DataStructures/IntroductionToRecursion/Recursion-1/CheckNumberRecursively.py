"""
Given an array of length N and an integer x, you need to find if x is present in the array or
not.
Input:
3
9 8 9
8
Output: True
"""

from sys import setrecursionlimit


def check_number(arr, x):

    if len(arr) == 0:
        return False
    if arr[0] == x:
        return True
    return check_number(arr[1:], x)


setrecursionlimit(11000)
num = int(input("Enter the number of elements: "))
array = list(int(i) for i in input().strip().split(" "))
element = int(input("Enter the elements to be searched: "))

if check_number(array, element):
    print("True")
else:
    print("False")
