"""
You will be given `Q` queries. You need to implement a queue two stacks according to those
queries. Each query wil belong to one of these three types:
1. `X`: Enqueue element `X` into the end of the nth queue. Returns true after the element
    is enqueued.
2. Dequeue the element at the front of the nth queue. Returns -1 if the queue is empty,
    otherwise, returns the dequeue element.
Note:
    Enqueue means adding an element to the end of the queue, while Dequeue means
    removing the element from the front of the queue.

"""


class Queue:
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def enqueue(self, x):
        self.stk1.append(x)

    def dequeue(self):
        element = 0
        while len(self.stk1) > 1:
            self.stk2.append(self.stk1.pop())
        if len(self.stk1) == 1:
            element = self.stk1.pop()
        while len(self.stk2) != 0:
            self.stk1.append(self.stk2.pop())
        return element


q = Queue()
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
q.enqueue(4)
q.enqueue(7)
print(q.dequeue())