class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def take_input():
    element = [int(ele) for ele in input().split()]
    head = None
    for elements in element:
        if elements == -1:
            break
        if head is None:
            new_node = Node(elements)
            head = new_node
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            else:
                new_node = Node(elements)
                curr.next = new_node
    return head


def reverse(head):
    if head is None or head.next is None:
        return head, head
    small_head, small_tail = reverse(head.next)
    small_tail.next = head
    head.next = None
    return small_head, head


def reverse_2(head):
    if head is None or head.next is None:
        return head
    small_head = reverse(head.next)
    small_tail = head.next
    small_tail.next = head
    head.next = None
    return small_head


def print_list(head):
    while head.next is not None:
        print(head.data, end='')
        head = head.next


ll_head = take_input()
# ll_head, tail = reverse(ll_head)
# print_list(ll_head)
ll_head = reverse_2(ll_head)
print_list(ll_head)
