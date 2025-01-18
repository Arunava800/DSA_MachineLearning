"""
Given a singly linked list of integers and an integer n, find and return the index for the
first occurrence of `n` in the linked list. -1 otherwise.
"""

from Node import TakeInput as Tp


def print_linked_list(head):
    while head is not None:
        print(head.data)
        head = head.next


def find_element(head, n):
    if head is None:
        return -1
    if head.data == n:
        return 0
    small_ans = find_element(head.next, n)
    if small_ans == -1:
        return -1
    return 1 + small_ans


insert_element = Tp()
ll_head = insert_element.take_input()
print_linked_list(ll_head)
data = int(input("Enter the element: "))
print(find_element(ll_head, data))
