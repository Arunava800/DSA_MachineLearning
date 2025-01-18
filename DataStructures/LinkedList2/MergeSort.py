"""
Given a singly linked list of integers, sort it using merge sort.
No need to print the list, it has already been taken care only return the new head of the list
"""


from Node import TakeInput as Tp
from sys import setrecursionlimit
setrecursionlimit(10000)


def mid_element(head):
    slow = head
    fast = head
    if head is None:
        return head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.data < head2.data:
        new_head = head1
        new_tail = head1
        head1 = head1.next
    else:
        new_head = head2
        new_tail = head2
        head2 = head2.next
    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            new_tail.next = head1
            new_tail = new_tail.next
            head1 = head1.next
        else:
            new_tail.next = head2
            new_tail = new_tail.next
            head2 = head2.next
    if head1 is not None:
        new_tail.next = head1
    if head2 is not None:
        new_tail.next = head2
    return new_head


def merge_sort(head):
    if head is None or head.next is None:
        return head
    mid = mid_element(head)
    half1 = head
    half2 = mid.next
    mid.next = None
    half1 = merge_sort(half1)
    half2 = merge_sort(half2)
    final_head = merge(half1, half2)
    return final_head

elements = Tp()
ll_head = elements.take_input()
ll_head = merge_sort(ll_head)
elements.print_linked_list(ll_head)