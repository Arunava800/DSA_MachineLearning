"""
a = [2,5, 1, 3, 6, 2, 4, 3, 5]
k = 4
Find 4 smallest element of the array
"""

import heapq


def find_k_smallest(arr, k):
    heapq.heapify(arr)
    ans = []
    for i in range(k):
        ans.append(heapq.heappop(arr))
    return ans


n = int(input("Enter the number of elements"))
array = list(map(int, input().split()))
smallest_array = find_k_smallest(array, n)
print(smallest_array)