class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def take_input():
    element = [int(ele) for ele in input().split()]
    head = None
    for elements in element:
        if head is None:
            data_node = Node(elements)
            head = data_node
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            data_node = Node(elements)
            curr.next = data_node
    return head


def print_linked_list(head):
    while head is not None:
        print(head.data, end="-->")
        head = head.next
    else:
        print("None")


def alternate_node_elements(head):
    curr = head
    if head.next is None:
        return head
    else:
        curr_next = head.next
    while curr is not None:
        prev = curr
        curr = curr_next.next
        prev.next = curr
        if curr is not None:
            curr_next = curr.next
        if curr_next is None:
            curr = curr_next

    return head


ll_head = take_input()
print_linked_list(ll_head)
ll_head = alternate_node_elements(ll_head)
print_linked_list(ll_head)


# 229 286 271 229 155 170 105 150 167 225 -1

