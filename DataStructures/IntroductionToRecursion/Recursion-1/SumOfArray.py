"""
Given an array of length N, you need to find and return the sum of all elements of the array
Input: 3
9 8 9
Output: 26
"""


from sys import setrecursionlimit


def sum_array(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum_array(arr[1:])


setrecursionlimit(11000)
n = int(input("Enter the number of elements present in the array"))
array = list(int(i) for i in input("Enter the number of elements").strip().split(" "))
print(sum_array(array))