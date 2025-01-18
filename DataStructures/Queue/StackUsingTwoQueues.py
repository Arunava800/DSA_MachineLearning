"""
Implement a stack data structure specifically to store integer data using two Queues. You
have to implement it in such a way that the push operation is done in O(1) time and the pop
operation are done in O(n) time. There should be two data members, both being Queues to store
data internally. You may use the inbuilt Queue.
1. Constructor
    It initializes the data members as required.
2. push(data)
    This function should take one argument of type integer. It pushes the element into the
    stack and returns nothing.
3. Pop()
    It pops the element from the top of the stack and in turn, returns the element being
    popped or deleted. In case the stack is empty, it returns -1.
4. top()
    It returns the element being kept at the top of the stack. In case the stack is empty
    it returns -1.
5. Size()
    It returns the size of the stack at any given instance of time.
6. isEmpty()
    It returns a boolean value indicating whether the stack is empty or not.
"""


class Stack:
    def __init__(self):
        self.__q1 = []
        self.__q2 = []
        self.__count = 0
        self.__front = 0

    def push(self, data):
        self.__q1.append(data)
        self.__count += 1

    def pop(self):
        element = 0
        if self.__count == 0:
            return -1
        while len(self.__q1) > 1:
            self.__q2.append(self.__q1[0])
            self.__q1.pop(0)
        if len(self.__q1) == 1:
            element = self.__q1[0]
            self.__q1.pop()
            self.__front = 0
            self.__count -= 1
        while len(self.__q2) > 0:
            self.__q1.append(self.__q2[self.__front])
            self.__q2.pop(0)
        return element

    def top(self):
        return self.__q1[-1]

    def get_size(self):
        return self.__count

    def is_empty(self):
        return self.__count == 0


s = Stack()
s.push(17)
s.push(23)
s.push(11)
while s.is_empty() is False:
    print(s.pop())
