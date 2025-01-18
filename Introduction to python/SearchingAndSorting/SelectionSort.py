"""
Sort the given unsorted array of size `N` in non-decreasing order using selection sort
algorithm
Parameters:
    arr= List of elements
Input:
    N = 5
    arr = [8, 6, 2, 5, 1]
Output:
[1, 2, 5, 6, 8]
"""


def selection_sort(arr: list[int]) -> None:
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[j], arr[min_index] = arr[min_index], arr[i]

n = int(input("Enter the number of terms: "))
array = list(map(int, input("Enter the list of elements: ").split()))
selection_sort(array)
