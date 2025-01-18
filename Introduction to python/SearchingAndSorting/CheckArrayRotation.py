"""
Write a function that returns the value of `K`, that is the index from which the array/list
has been rotated
Parameters:
    arr = Array
    n = size of the array
Input: N - Size of the array
[5, 6, 1, 2, 3, 4]
Output: K- the index of the array form which the array has been rotated
2
"""
import math


def array_rotate_check(arr, n):
    # Brute Force
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
                break
    return count


def rotate_array_check(arr, n):
    if n == 1 or n == 0:
        return 0
    max_value = -math.inf
    index = 0
    length = len(arr)-1
    for i in range(len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
            index = i
    if max_value == arr[length]:
        return 0
    else:
        return index+1


terms = int(input("Enter the length of the array: "))
array = list(map(int, input("Enter the elements in the array").split()))[:terms]
answer = rotate_array_check(array, terms)
print(answer)
