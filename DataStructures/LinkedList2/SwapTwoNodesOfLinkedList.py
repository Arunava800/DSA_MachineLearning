"""
You have been given a singly linked list of integers along with two integers, `i`, and `j`.
Swap the nodes that are present at the `i-th`  and `j-th` positions and return the new head
to the list.
Note:
    1. Remember, you need to swap the nodes, not only the data.
    2. Indexing starts from 0.
    3. No need to print the list, it has already been taken care.
"""

from Node import TakeInput as Tp


def swap_nodes(head, i, j):
    curr = head
    prev = None
    count = 0
    start_index, end_index, start_prev, end_prev = None, None, None, None
    if head is None:
        return head
    while curr is not None:
        if i > j:
            if count == j:
                start_index = curr
                start_prev = prev
            if count == i:
                end_index = curr
                end_prev = prev
        else:
            if count == i:
                start_index = curr
                start_prev = prev
            if count == j:
                end_index = curr
                end_prev = prev
        prev = curr
        curr = curr.next
        count += 1
    if start_prev is None:
        end_prev.next = start_index
        temp = start_index.next
        start_index.next = end_index.next
        end_index.next = temp
        head = end_index
    elif start_index == end_prev:
        start_prev.next = end_index
        start_index.next = end_index.next
        end_index.next = start_index
        start_prev.next = end_index
    else:
        start_prev.next = end_index
        temp = start_index.next
        start_index.next = end_index.next
        end_index.next = temp
        end_prev.next = start_index
    return head


elements = Tp()
ll_head = elements.take_input()
pos1 = int(input("Enter the value for position1"))
pos2 = int(input("Enter the value for position2"))
ll_head = swap_nodes(ll_head, pos1, pos2)
elements.print_linked_list(ll_head)
