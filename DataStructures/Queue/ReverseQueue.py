"""
You have been given a queue that can store integers as the data. You are required to write
a function that reverses the populated queue itself without using any other data structures.
Sample Input:
    1 2 3 4 5 10
Sample Output: 10 5 4 3 2 1
"""


from queue import Queue


def reverse_queue(i_queue):
    if i_queue.qsize() <= 1:
        return
    front = i_queue.get()
    reverse_queue(i_queue)
    i_queue.put(front)


q = Queue()
while True:
    data = int(input())
    if data == -1:
        break
    q.put(data)

reverse_queue(q)
