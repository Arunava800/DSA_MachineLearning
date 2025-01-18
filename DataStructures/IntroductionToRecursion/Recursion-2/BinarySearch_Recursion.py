"""
Binary Search using Recursion
"""


def binary_search(a, x, si, ei):
    if si > ei:
        return -1
    mid = (si + ei)//2
    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return binary_search(a, x, si, mid - 1)
    else:
        return binary_search(a, x, mid + 1, ei)


li = [1, 2, 3, 4, 5, 6, 7, 9]
print(binary_search(li, 7, 0, len(li)))
