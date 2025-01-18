class Stack:
    def __init__(self):
        self.__data = []

    def push(self, element):
        self.__data.append(element)

    def size(self):
        return len(self.__data)

    def is_empty(self):
        return self.size() == 0

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return
        return self.__data.pop()

    def top(self):
        if self.is_empty():
            print("Stack is empty")
            return
        return self.__data[len(self.__data)-1]


s = Stack()
print(s.is_empty())
s.push(15)
s.push(20)
s.push(25)
print(s.pop())
