"""
For a given queue containing all integer data, reverse the first k elements. You have been
required to make desired changes in the input queue itself.
Example:
    10 20 30 40 50 60 70 80 90
    k= 4
    Output:
      40 30 20 10 50 60 70 80 90
"""

import queue

# ------------------UTILITY FUNCTIONS--------------------------------------------------


def is_empty(stack):
    return len(stack) == 0


def top(stack):
    return stack[len(stack)-1]
# --------------------------------------------------------------------------------------


def reverse_k_elements(i_queue, k):
    if i_queue.empty() or k > i_queue.qsize():
        return i_queue
    if k <= 0:
        return i_queue
    stack = list()
    for i in range(k):
        stack.append(i_queue.get())
    while not is_empty(stack):
        i_queue.put(stack.pop())
    for i in range(i_queue.qsize()-k):
        i_queue.put(i_queue.get())
    return i_queue

