"""
-----------------------------  STACK IMPLEMENTATION----------------------------------------
"""


class Stack:
    def __init__(self):
        self.__data = []

    def is_empty(self):
        if len(self.__data) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.__data)

    def push(self, new_data):
        self.__data.append(new_data)

    def pop(self):
        return self.__data.pop()

    def peek(self):
        return self.__data[-1]


s = Stack()
s.push(10)
s.push(30)
s.push(40)
print(s.peek())
while not s.is_empty():
    print(s.pop())