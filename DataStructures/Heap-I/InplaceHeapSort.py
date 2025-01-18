"""
Given an integer array of size `N`, sort this array (in decreasing order) using heap sort.
Note: Space complexity should be O(1).
Sample Input: 2 6 8 5 4 3
Sample Output: 8 6 5 4 3 2

"""


from typing import List


def down_heap(arr: List[int], i: int, n: int):
    parent_index = i
    left_child = 2 * parent_index + 1
    right_child = 2 * parent_index + 2
    while left_child < n:
        min_index = parent_index
        if arr[min_index] < arr[left_child]:
            min_index = left_child
        if right_child < n and arr[min_index] < arr[right_child]:
            min_index = right_child
        if min_index == parent_index:
            return
        arr[min_index], arr[parent_index] = arr[parent_index], arr[min_index]
        parent_index = min_index
        left_child = 2 * parent_index + 1
        right_child = 2 * parent_index + 2


def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        down_heap(arr, i, n)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        down_heap(arr, 0, i)
    return arr


elements = int(input())
array = list(map(int, input().split()))[:elements]
sorted_heap = heap_sort(array)
for ele in array[::-1]:
    print(ele, end=' ')