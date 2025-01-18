"""
Two integer arrays of size N and M are given. The intersection elements is to be printed
in the order they appear in the array/list
Parameters:
    N= Array of size N
    M = Array of size M
Input:
N = [2 6 8 5 4 3]
M= [2 3 4 7]
Output: 2 4 3
"""

import math


def intersections(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                print(arr2[j], end=" ")
                arr2[j] = math.inf
                break


terms_n = int(input("Enter the number of terms for the first array: "))
terms_m = int(input("Enter the number of terms for the second array: "))
array1 = list(map(int, input("Enter the elements of the first array: ").split()))
array2 = list(map(int, input("Enter the elements of the second array: ").split()))
intersections(array1, array2)
