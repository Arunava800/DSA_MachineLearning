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


def print_list(head):
    while head is not None:
        print(head.data, end='-->')
        head = head.next
    else:
        print("None")


def merge_list(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    merged_head = head1 if head1.data < head2.data else head2
    curr_node1 = merged_head.next
    curr_node2 = head2 if merged_head == head1 else head1
    prev = merged_head
    while curr_node1 is not None and curr_node2 is not None:
        if curr_node1.data < curr_node2.data:
            prev = curr_node1
            curr_node1 = curr_node1.next
        else:
            prev.next = curr_node2
            prev = curr_node2
            curr_node2 = curr_node2.next

    if curr_node1 is not None:
        prev.next = curr_node1
    else:
        prev.next = curr_node2
    return merged_head

ll_head_1 = take_input()
ll_head_2 = take_input()
# print_list(ll_head_1)
# print_list(ll_head_2)
ll_head_3 = merge_list(ll_head_1, ll_head_2)
print_list(ll_head_3)