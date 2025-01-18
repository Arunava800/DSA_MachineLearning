"""
You have been given an integer array/list(ARR) of size N that contains only 0 and 1.
Write a function to sort this array/list.
Parameters:
    n = size of the array
    arr = Array
Input: n = 7
arr = [0, 1, 1, 0, 1, 0, 1]
Output:
[0, 0, 0, 1, 1, 1, 1]
"""


def sort_zeroes_and_one(arr, n):
    ptr = 0
    for i in range(n):
        if arr[i] == 0:
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
    print(arr)


N = int(input("Enter the number of terms present in the array: "))
array = list(map(int, input("Enter the elements present in the array").split()))[:N]
sort_zeroes_and_one(array, N)
