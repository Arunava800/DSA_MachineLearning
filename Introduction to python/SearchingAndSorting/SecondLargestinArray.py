"""
You have been given a random integer array/list(ARR) of size N. You are required to find and
return the second-largest element in the array/list.
Input:
5
4 3 10 9 2
Output: 9
"""

import math
MIN_VALUE = -math.inf


def second_largest_element(arr, n):
    if n == 0:
        return MIN_VALUE
    largest = arr[0]
    second_largest = MIN_VALUE
    for i in range(len(arr)):
        if largest < arr[i]:
            second_largest = largest
            largest = arr[i]
        elif second_largest < arr[i] != largest:
            second_largest = arr[i]
    return second_largest


terms = int(input("Enter the number of elements in the array: "))
array = list(map(int, input("Enter the array: ").split()))
print(second_largest_element(array, terms))
