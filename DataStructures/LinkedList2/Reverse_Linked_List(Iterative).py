class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def insert():
    elements = [int(ele) for ele in input().split()]
    head = None
    for element in elements:
        if element == -1:
            break
        if head is None:
            new_node = Node(element)
            head = new_node
        else:
            curr = head
            new_node = Node(element)
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
    return head


def print_linked_list(head):
    while head is not None:
        print(head.data, end="-->")
        head = head.next
    print(None)


def reverse_linked_list(head):
    curr = head
    prev = None
    while curr is not None:
        r_next = curr.next
        curr.next = prev
        prev = curr
        curr = r_next
    head = prev
    return head


def mid_point(head):
    slow, fast = head, head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow.data


ll_head = insert()
print_linked_list(ll_head)
# ll_head = reverse_linked_list(ll_head)
# print_linked_list(ll_head)
print(mid_point(ll_head))

