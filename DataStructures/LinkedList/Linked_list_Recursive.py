class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_list(head, i):
    if i < 0:
        return head
    if i == 0:
        head = head.next
        return head
    small_head = delete_list(head.next, i-1)
    head.next = small_head
    return head

def insert_elements():
    elements = [int(ele) for ele in input().split()]
    head = None
    for element in elements:
        if head is None:
            new_node = Node(element)
            head = new_node
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            else:
                new_node = Node(element)
                curr.next = new_node
    return head


def print_linked_list(head):
    while head.next is not None:
        print(head.data, end="---->")
        head = head.next
    else:
        print(head.data, "none", sep="--->")


ll_head = insert_elements()
print_linked_list(ll_head)
ll_head = delete_list(ll_head, 2)
print_linked_list(ll_head)
