class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Input linked List
def take_input():
    input_list = [int(ele) for ele in input().split()]
    head = None
    tail = None

    for curr_ele in input_list:
        if curr_ele == -1:
            break
        new_node = Node(curr_ele)
        """
        This method has a order of n^2
        if head is None:
            head = new_node
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
        """
        # Optimized code for o(n)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    return head


# Printing Linked List
def print_linked_list(head):
    # curr = head
    # while curr is not None:
    #     print(curr.data, end="-->")
    #     curr = curr.next
    # else:
    #     print("End")
    while head is not None:
        print(str(head.data)+"-->", end="")
        head = head.next
    print("None")


def length(head):
    """
    NOTE: Ordinary Solution
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count
    """
    """
    Note: 
    RECURSIVE SOLUTION
    """
    if head is None:
        return 0
    return 1 + length(head.next)




def print_i_node(head, i):
    count = 0
    while head is not None:
        if count == i:
            return head.data
        count += 1
        head = head.next
    else:
        return


def insert_node(head, pos, data):
    prev = None
    count = 0
    curr = head

    new_node = Node(data)
    if pos == 0:
        new_node.next = head
        head = new_node
        return head
    else:
        while curr.next is not None:
            if count == pos:
                new_node.next = curr
                prev.next = new_node
                break
            else:
                count += 1
                prev = curr
            curr = curr.next
        return head


def delete_linked_list(head, i):
    length_m = length(head)
    count = 0
    prev = None
    curr = head

    if i >= length_m or length_m == i:
        return head
    else:
        if count == i and prev is None:
            head = curr.next
            return head
        while curr.next is not None:
            if count == i:
                prev.next = curr.next
                return head
            else:
                count += 1
                prev = curr
                curr = curr.next
        else:
            prev.next = None
            return head



ll_head = take_input()
# print_linked_list(ll_head)
print(length(ll_head))
# print(print_i_node(ll_head, 3))
# i = int(input("position: "))
# value = int(input("Value: "))
# ll_head = insert_node(ll_head, i, value)
# print_linked_list(ll_head)
# ll_head = delete_linked_list(ll_head,0)
# print_linked_list(ll_head)