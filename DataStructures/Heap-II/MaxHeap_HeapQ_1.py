"""
Construct a max heap using heapq
"""


import heapq as pq

arr = [2, 1, 4, 3, 5]
neg = [-1 * ele for ele in arr]
pq.heapify(neg)
print("Max heap is "+str(pq.heappop(neg)*-1))