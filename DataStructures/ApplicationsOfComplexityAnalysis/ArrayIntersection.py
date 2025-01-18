"""
You have been given two arrays/lists (Arr1 and Arr2) of size M and N, respectively. You need
to print their intersection. An intersection for this problem can be defined as when both the
array/list contain a particular value or when there is a common value that exists in both
array/list.
Note:
    Input array/list can contain duplicate elements.
    The intersection elements would be printed in ascending order
Sample input:
    2
    6
    2 6 9 5 4 3
    4
    2 3 4 7
Sample output:
2 3 4 7
"""


def partition(array, si, ei):
    c = 0
    pivot = array[si]
    for i in range(si, ei + 1):
        if array[i] < pivot:
            c += 1
    array[si + c], array[si] = array[si], array[si + c]
    pivot_index = si + c
    i = si
    j = ei
    while i < j:
        if array[i] < pivot:
            i += 1
        elif array[j] >= pivot:
            j -= 1
        else:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    return pivot_index


def quick_sort(array, si, ei):
    if si > ei:
        return
    pivot_index = partition(array, si, ei)
    quick_sort(array, si, pivot_index - 1)
    quick_sort(array, pivot_index + 1, ei)
    return array


def intersection(arr1, arr2, m1, n2):
    i = 0
    j = 0
    while i < m and j < n:
        if arr1[i] == arr2[j]:
            print(arr1[i], end=" ")
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1


m = int(input("Enter the size of first array"))
n = int(input("Enter the size of second array"))
array1 = list(map(int, input(f"Enter {m} elements").split()))[:m]
array2 = list(map(int, input(f"Enter {n} elements").split()))[:n]
sorted_array_1 = quick_sort(array1, 0, len(array1) - 1)
sorted_array_2 = quick_sort(array2, 0, len(array2) - 1)
intersection(sorted_array_1, sorted_array_2, m, n)
