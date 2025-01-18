"""
You have been given a singly linked list of integers along with two integers, `M` and `N`. Traverse
the linked list such that you retain the `M` nodes, then delete the next `N` nodes. Continue
the same until the end of the linked list. Indexing starts from 1.
To put it in other words, in the given linked list, you need to delete N nodes after every
`M` elements.
"""

from Node import TakeInput as Tp


def skip_m_delete_n(head, m, n):
    if m == 0:
        head = None
        return head
    curr = head
    prev = None
    while curr is not None:
        m_count = 1
        n_count = 1
        while m_count <= m:
            prev = curr
            curr = curr.next
            m_count += 1
        while n_count <= n:
            prev.next = curr.next
            curr.next = None
            curr = prev.next
            if curr is None:
                return head
            n_count += 1
    return head


take_input = Tp()
ll = take_input.take_input()
m_ = int(input("Enter the value for m. "))
n_ = int(input("Enter the value for n. "))
ll = skip_m_delete_n(ll, m_, n_)
take_input.print_linked_list(ll)