"""
Implement a Queue data structure specifically to integer data using a singly linked list.
The common data members should be private.
You need to implement the following public functions:
1. Constructor:
    It initializes the data members as required.
2. enqueue(data):
    This function should take one argument of type integer. It enqueues the element into the
    queue and returns nothing.
3. dequeue():
    It dequeues/ removes the element from the front of the queue and in turn, returns the
    element being dequeued or removed. In case the queue is empty, it returns -1
4. front():
    It returns the element being kept at the front of the queue. In case the queue is empty, it
    returns -1.
5. get_size():
    It returns the size of the queue at any given instance of time
6. is_empty():
    It returns a boolean value indicating whether the queue is empty or not.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0
        self.__front = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
            self.__front = self.__head
        else:
            self.__tail.next = new_node
            self.__tail = self.__tail.next
        self.__count += 1

    def dequeue(self):
        if self.__head is None:
            return -1
        element = self.__front.data
        self.__front = self.__head.next
        self.__head = self.__head.next
        self.__count -= 1
        return element

    def front(self):
        return self.__front.data

    def get_size(self):
        return self.__count

    def is_empty(self):
        return self.__count == 0


linked_q = Queue()
linked_q.enqueue(3)
linked_q.enqueue(5)
linked_q.enqueue(10)
linked_q.enqueue(30)
linked_q.enqueue(90)
print(linked_q.get_size())
print(linked_q.dequeue())
print(linked_q.get_size())
while linked_q.is_empty() is False:
    print(linked_q.dequeue())
print(linked_q.is_empty())