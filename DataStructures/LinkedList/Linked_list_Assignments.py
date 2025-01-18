class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_elements():
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


def print_linked_list(head):
    while head is not None:
        print(head.data, end="--->")
        head = head.next
    else:
        print("None")


"""
1.
********************************FIND A NODE IN A LINKED LIST********************************
You have been given a singly linked list of integers. Write a function that returns the index/
position of integers data denoted by `N` (if it exists). Return -1 otherwise.
Note:
    Assume that the indexing for the singly linked list always starts from 0.
"""


def find_node(head, n):
    count = 0
    while head is not None:
        if head.data == n:
            return count
        else:
            head = head.next
            count += 1
    return -1


"""
********************************************************************************************
"""

"""
2.
************************************APPEND LAST N TO FIRST**********************************
You have been given a singly linked list of integers along with an integer 'N'. Write a 
function to append the last 'N' nodes towards the front of the singly linked list and returns
the new head to the list.
Hints:
    Identify how many pointers you require and try traversing the to right places and connect
    nodes accordingly also don't forget to disconnect what's required else it could create
    cycles.
"""


def length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count


def append_last_n_to_first(head, n):
    curr = head
    tail = curr
    count = 1
    prev = None
    count_n = length(head) - n
    while tail.next is not None:
        tail = tail.next
    while curr.next is not None:
        if count == count_n + 1:
            tail.next = head
            prev.next = None
            head = curr
            return head
        else:
            prev = curr
            curr = curr.next
            count += 1
    return head


"""
********************************************************************************************
"""
"""
3. 
***********************************ELIMINATE DUPLICATES************************************
You have been given a singly linked list of integers where the elements are sorted in 
ascending order. Write a function that removes consecutive duplicate values such that
the given list only contains unique elements and returns the head of the updated list.

"""


def eliminate_duplicates(head):
    prev = head
    curr = prev.next
    while curr is not None:
        if prev.data == curr.data:
            curr = curr.next
            prev.next = curr
        else:
            prev = curr
            curr = curr.next
    return head


"""
*******************************************************************************************
"""

"""
4. 
*******************************PRINT REVERSED LINKED LIST***********************************
You have been given a singly linked list of integers. Write a function to print the list in
a reverse order. To explain it further, you need to start printing the data from the tail
and move towards the head of the list, printing the data at the end.
"""


def print_reverse(head):
    if head is None:
        return

    print_reverse(head.next)
    print(head.data, end=" ")


"""
*********************************************************************************************
"""

"""
5.
**************************************PALINDROME LINKED LIST********************************
You have been given a head to a singly linked list of integers. Write a function to check
whether the list given is a palindrome or not.
"""


def get_mid_list(curr):
    slow = curr
    fast = curr
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def reverse_list(curr):
    prev = None
    while curr is not None:
        next_ = curr.next
        curr.next = prev
        curr = next_
    return prev


def is_palindrome(head):
    if head is None or head.next is None:
        return False
    mid = get_mid_list(head)
    rev_head = reverse_list(mid)
    while rev_head is not None and head is not None:
        if rev_head.data != head.data:
            return False
        rev_head = rev_head.next
        head = head.next
    return True


ll_head = insert_elements()
# print_linked_list(ll_head)
# index_element = int(input("Enter the element: "))
# print(find_node(ll_head, index_element))
# pos_ele = int(input("Enter the position of the append list: "))
# ll_head = append_last_n_to_first(ll_head, pos_ele)
# ll_head = eliminate_duplicates(ll_head)
# print_linked_list(ll_head)
# print_reverse(ll_head)
check = is_palindrome(ll_head)
if check:
    print("true")
else:
    print("false")
