"""
Given an array of length N and an integer x, you need to find and return the last index
of integer x present in the array. Return - 1 if it is not present in the array. Last index
means  - if x is present multiple times in the array, return the index at which the index
comes last in the array.
You should start traversing array from 0 and not N-1
Do this recursively. Indexing in the array starts from 0
"""


def last_index(arr, x, si):
    length = len(arr)
    if si == 0:
        return -1
    if arr[si] == x:
        return si
    return last_index(arr, x, si-1)


def last_index_copy(arr, x):
    length = len(arr)
    if length == 0:
        return -1
    smaller_list = arr[1:]
    output = last_index_copy(smaller_list, x)
    if output != -1:
        return output + 1
    else:
        if arr[0] == x:
            return 0
        else:
            return -1


a = [1, 4, 5, 4, 8]
print(last_index_copy(a, 4))
