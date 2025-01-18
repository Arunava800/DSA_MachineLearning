class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def take_input():
    element = [int(ele) for ele in input().split()]
    head = None
    for elements in element:
        if head is None:
            node_data = Node(elements)
            head = node_data
        else:
            curr = head
            node_data = Node(elements)
            while curr.next is not None:
                curr = curr.next
            curr.next = node_data
    return head


def print_linked_list(head):
    while head is not None:
        print(head.data, end="-->")
        head = head.next
    else:
        print("None")


def reverse_list(head):
    if not head:
        return
    curr = head
    prev = head
    next_node = head.next
    curr.next = None
    while next_node:
        curr = next_node
        next_node = next_node.next
        curr.next = prev
        prev = curr
    return curr
    pass



def next_element(head):
    new_head = reverse_list(head)
    new_head.data += 1
    curr = new_head
    while curr.next is not None:
        if curr.data > 9:
            curr.data = 0
            curr = curr.next
            curr.data += 1
        else:
            curr = curr.next
    else:
        if curr.data > 9:
            curr.data = 0
            new_node = Node(1)
            curr.next = new_node
    new_head = reverse_list(new_head)
    return new_head


ll_head = take_input()
ll_head = next_element(ll_head)
print_linked_list(ll_head)

