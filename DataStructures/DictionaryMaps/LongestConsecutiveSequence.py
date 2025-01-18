"""
----------------------LONGEST CONSECUTIVE SEQUENCE-------------------------------------
You are given an unsorted array/list of `N` integers. Your task is to return the length of the
longest consecutive sequence.
The consecutive sequence is in the form ['NUM', 'NUM'+1, 'NUM'+2 ... 'NUM' + L], where
'NUM' is the starting integer of the sequence and 'L' + 1 is the length of the sequence.
Note: If there are any duplicates in the given array, we will count only one of them in the
consecutive sequence.
Sample Input: 1
              5
              [33,20,34,30,35]
Sample Output: 3--> [33, 34, 35]
"""


from typing import List

# sorting the unsorted list


def merge(arr1: List[int], arr2: List[int], arr: List[int]) -> List[int]:
    ptr1, ptr2, ptr_k = 0, 0, 0
    while ptr1 < len(arr1) and ptr2 < len(arr2):
        if arr1[ptr1] < arr2[ptr2]:
            arr[ptr_k] = arr1[ptr1]
            ptr1 += 1
            ptr_k += 1
        else:
            arr[ptr_k] = arr2[ptr2]
            ptr2 += 1
            ptr_k += 1
    while ptr1 < len(arr1):
        arr[ptr_k] = arr1[ptr1]
        ptr1 += 1
        ptr_k += 1
    while ptr2 < len(arr2):
        arr[ptr_k] = arr2[ptr2]
        ptr2 += 1
        ptr_k += 1
    return arr


def merge_sort(arr: List[int]) -> List[int] or None:
    if len(arr) == 1 or len(arr) == 0:
        return
    mid = len(arr) // 2
    first_half = arr[:mid]
    second_half = arr[mid:]
    merge_sort(first_half)
    merge_sort(second_half)
    sorted_array = merge(first_half, second_half, arr)
    return sorted_array


def consecutive_sequence(arr: List[int]) -> int:
    count = 0
    temp_list = list()
    nested = []
    sorted_array = merge_sort(arr)
    for i in range(len(sorted_array)):
        if i + 1 < len(sorted_array):
            if sorted_array[i+1] == sorted_array[i] + 1:
                if sorted_array[i] not in temp_list:
                    temp_list.append(sorted_array[i])
            elif sorted_array[i-1] == sorted_array[i] - 1:
                if sorted_array[i] not in temp_list:
                    temp_list.append(sorted_array[i])
                    nested.append(temp_list)
                    temp_list =[]
        else:
            if sorted_array[i-1] == sorted_array[i] - 1:
                temp_list.append(sorted_array[i])
                nested.append(temp_list)
                temp_list =[]
            else:
                nested.append(temp_list)
    for i in range(len(nested)):
        if len(nested[i]) > count:
            count = len(nested[i])
    return count


array = list(map(int, input().split()))
print(consecutive_sequence(array))
