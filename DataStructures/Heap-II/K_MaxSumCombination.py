"""
You are given two arrays/list `A` and `B` of size `N` each. You are also given an integer `k`.
It would be best to find the `k` maximum and valid sum combination from all the possible sum combination
of the array/list `A` and `B`. Sum combination adds one element from array `A` and another from array `B`.
For example:
A=[1, 3]
B= [4,2]
k = 2
Sample Output: The possible combinations can be 5(3+2), 7(3+4), 3(1+2), 5(1+4)
The two maximum sum combinations are 7 and 5.
"""


from typing import List
import heapq as pq


class Element:
    def __init__(self, value: int, idx1: int, idx2: int) -> None:
        self.value = value
        self. idx1 = idx1
        self.idx2 = idx2

    def __lt__(self, obj: object) -> bool:
        return self.value > obj.value

    def __eq__(self, obj: object) -> bool:
        return self.value == obj.value


def k_max_sum_combination(a: List[int], b: List[int], n: int, k: int) -> List[int]:
    a.sort(reverse=True)
    b.sort(reverse=True)
    ans = []
    heap = [Element(a[0] + b[0], 0, 0)]
    taken = {}
    taken[(0, 0)] = True
    for i in range(k):
        tp = pq.heappop(heap)
        ans.append(tp.value)
        idx1, idx2 = tp.idx1, tp.idx2
        if (idx1+1 < n) and not taken.get((idx1+1, idx2), False):
            pq.heappush(heap, Element(a[idx1+1]+b[idx2], idx1+1, idx2))
            taken[(idx1+1, idx2)] = True

        if (idx2 + 1) < n and not taken.get((idx1, idx2+1), False):
            pq.heappush(heap, Element(a[idx1]+b[idx2+1], idx1, idx2))
            taken[(idx1, idx2+1)] = True
    return ans


if __name__ == "__main__":
    element1 = [1, 3, 5]
    element2 = [6, 4, 2]
    print(k_max_sum_combination(element1, element2, 3, 2))
