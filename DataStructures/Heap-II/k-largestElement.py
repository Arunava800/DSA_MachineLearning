"""
You are given with an integer array `k` and an array of integers that contains numbers in random order.
Write a program to find `k`- largest number from given array. You need to save them in an array and return it.
The time complexity should be O(n log k) and the space complexity should not exceed O(K).
Order of the elements is not important.
13
2 12 9 16 10 5 3 20 25 11 1 8 6
4
Output:
12
16
20
25
"""


from typing import List
import heapq


def k_largest(arr: List[int], k) -> List[int]:
    ans_ = heapq.nlargest(k, arr)
    return ans_


n = int(input())
lst = list(map(int, input().split()))
ans = k_largest(lst, n)
print(*ans, sep="\n")
