"""
Construct a max heap using Wrapper class
"""

import heapq as pq


class MaxWrapper:
    def __init__(self, value):
        self.value = value

    def __lt__(self, obj: object) -> bool:
        return self.value > obj.value

    def __eq__(self, obj: object) -> bool:
        return self.value == obj.value

    def get_value(self):
        return self.value


arr = [2, 1, 4, 3, 5]
wrapped_arr = list(map(lambda item: MaxWrapper(item), arr))
pq.heapify(wrapped_arr)
print("Max element is: "+str(pq.heappop(wrapped_arr).get_value()))
