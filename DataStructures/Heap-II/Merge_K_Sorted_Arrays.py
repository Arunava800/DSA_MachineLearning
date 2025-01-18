"""
You have been given `k` different arrays/lists, which are sorted individually in ascending order. You need
to merge all the given array/list such that the output array/list should be sorted in ascending order.
Sample input:
1
2
3
3 5 9
4
1 2 3 8
Sample Output:
1 2 3 3 5 8 9
"""


from typing import List
import heapq as pq


class Element:
    def __init__(self, value: int, idx: int) -> None:
        self.value = value
        self.idx = idx

    def __lt__(self, o: object) -> bool:
        return self.value < o.value

    def __eq__(self, obj: object) -> bool:
        return self.value == obj.value


def merge_k_sorted_elements(k_arrays: List[List[int]], k: int) -> List[int]:
    ans = []
    ptr = [0 for _ in range(k)]
    heap = [Element(k_arrays[i][0], i) for i in range(k)]
    pq.heapify(heap)
    while len(heap) > 0:
        tp: Element = pq.heappop(heap)
        ans.append(tp.value)
        arr_idx = tp. idx
        if ptr[arr_idx] + 1 < len(k_arrays[arr_idx]):
            ptr[arr_idx] += 1
            pq.heappush(heap, Element(k_arrays[arr_idx][ptr[arr_idx]], arr_idx))
    return ans


if __name__ == "__main__":
    print(merge_k_sorted_elements([[2, 4, 5, 6], [1, 3], [1, 2, 7]], 3))
