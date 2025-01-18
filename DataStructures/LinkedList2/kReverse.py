"""
Given a singly linked list of integers, reverse the nodes of the linked list `k` at a time and
return the modified list.
`k` is a positive integer and is less than or equal to the length of the linked list. If the number
of nodes is not a multiple of `k` then the left out nodes, in the end should be reversed as well.
Given Linked list : 1 -> 2 -> 3 -> 4 -> 5
For k= 2, you should return 2->1-> 4-> 3 -> 5
For k= 3, you should return 3 -> 2 -> 1 -> 5 -> 4
"""


from Node import TakeInput as Tp


def k_reverse(head, k):
    if k == 0 or k == 1:
        return head
    current, fwd, prev = head, None, None
    count = 0
    while count < k and current is not None:
        fwd = current.next
        current.next = prev
        prev = current
        current = fwd
        count += 1
    if fwd is not None:
        head.next = k_reverse(fwd, k)
    return prev


elements = Tp()
ll_head = elements.take_input()
k_terms = int(input("Enter the number of terms: "))
ll_head = k_reverse(ll_head, k_terms)
elements.print_linked_list(ll_head)
