"""
Given a singly linked list of integers, sort it using `Bubble Sort`.
Note:
    No need to print the list, it has already been taken care. Only return the new head to the
    list.
"""


from Node import TakeInput as Tp


def length_linked_list(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count


def bubble_sort(head):
    if head is None:
        return head
    length_head = length_linked_list(head)
    for i in range(length_head):
        curr = head
        curr_next = head.next
        prev = None
        while curr_next is not None:
            if curr.data > curr_next.data and prev is None:
                curr.next = curr_next.next
                curr_next.next = curr
                head = curr_next
                curr_next = curr.next
                prev = head
            elif curr.data > curr_next.data:
                prev.next = curr_next
                curr.next = curr_next.next
                curr_next.next = curr
                prev = curr_next
                curr_next = curr.next
            else:
                prev = curr
                curr = curr_next
                curr_next = curr_next.next
    return head


elements = Tp()
ll_head = elements.take_input()
ll_head = bubble_sort(ll_head)
elements.print_linked_list(ll_head)
