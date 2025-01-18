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


import heapq as pq


def peek_value(heap):
    p_value = pq.heappop(heap)
    pq.heappush(heap, p_value)
    return p_value


def is_empty(heap):
    if len(heap) != 0:
        return False
    return True


def k_largest(li, k):
    heap = list()
    for i in range(k):
        pq.heappush(heap, li[i])
    for i in range(k, len(li)):
        if li[i] > peek_value(heap):
            pq.heappop(heap)
            pq.heappush(heap, li[i])
    ans = []
    while not is_empty(heap):
        ans.append(pq.heappop(heap))
    return ans


n = int(input())
lst = list(map(int, input().split()))
answer = k_largest(lst, n)
print(*answer, sep="\n")
