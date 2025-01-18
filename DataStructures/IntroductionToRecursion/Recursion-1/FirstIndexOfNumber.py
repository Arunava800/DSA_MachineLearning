"""
Given a list, find the first occurrence of the number
"""

import random


def first_occurrence(arr, si, x):
    if si == len(arr) or si == len(arr)-1:
        return -1
    if arr[si] == x:
        return si
    return first_occurrence(arr, si+1, x)


def first_occurrence_copy(arr, x):
    length = len(arr)
    if length == 0:
        return -1
    if arr[0] == x:
        return 0
    ans = first_occurrence_copy(arr[1:], x)

    if ans == -1:
        return -1
    else:
        return ans + 1



a = [i for i in range(random.randint(1, 100))]
print(a)
print(len(a))
n = int(input("Enter the element: "))
# print(first_occurrence(a, 0, n))
print(first_occurrence_copy(a, n))
