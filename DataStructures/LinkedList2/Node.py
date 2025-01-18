class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class TakeInput:
    @staticmethod
    def take_input():
        elements = [int(element) for element in input().split()]
        head = None
        for ele in elements:
            if ele == -1:
                break
            if head is None:
                new_node = Node(ele)
                head = new_node
            else:
                curr = head
                while curr.next is not None:
                    curr = curr.next
                new_node = Node(ele)
                curr.next = new_node
        return head

    @staticmethod
    def print_linked_list(head):
        while head is not None:
            print(head.data, end="-->")
            head = head.next
        else:
            print("None")
