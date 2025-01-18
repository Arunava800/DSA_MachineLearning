"""
For a given singly linked list of integers, arrange the nodes such that all the even numbers
nodes are placed after all the  odd number nodes. The relative order of the odd and even terms
should remain unchanged.
1. Don't create a new linked list
2. just change the data, instead  rearrange the provided list
"""
from Node import TakeInput as Tp


def even_after_odd(head):
    if head is None or head.next is None:
        return head
    curr = head
    o_head = None
    o_tail = None
    e_head = None
    e_tail = None
    while curr is not None:
        if o_head is None and curr.data % 2 != 0:
            o_head = curr
            o_tail = curr
            curr = curr.next
        elif e_head is None and curr.data % 2 == 0:
            e_head = curr
            e_tail = curr
            curr = curr.next
        elif o_head is not None and curr.data % 2 != 0:
            o_tail.next = curr
            o_tail = o_tail.next
            curr = curr.next
        elif e_head is not None and curr.data % 2 == 0:
            e_tail.next = curr
            e_tail = e_tail.next
            curr = curr.next
    else:
        if o_head is not None and e_head is not None:
            e_tail.next = None
            o_tail.next = e_head

    if head.data % 2 == 0 and o_head is None:
        head = e_head
    else:
        head = o_head
    return head

elements = Tp()
insert_element = elements.take_input()
# display_element = elements.print_linked_list(insert_element)
ll_head = even_after_odd(insert_element)
elements.print_linked_list(ll_head)
