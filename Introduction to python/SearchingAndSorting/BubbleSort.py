"""
Bubble sort for an integer array of size N
Parameters:
    N= Size of the array
    arr = Array
Input: Unsorted Array [2, 13, 4,1,3,6,8]
Output: Sorted Array [1,2,3,4,6,8,13]
"""


def bubble_sort(arr: list[int], n: int) -> None:
    # for j in range(len(arr)):
    #     for i in range(len(arr)-1):
    # optimized code:
    for j in range(len(arr)-1):
        for i in range(len(arr)-1-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    print(arr)


terms = int(input("Enter the number of terms for the array: "))
array = list(map(int,input("Enter the elements in the array: ").split()))
bubble_sort(array, terms)