class Dequeue:
    def __init__(self, size):
        self.size = size
        self.queue = []
        self.queue_size = len(self.queue)

    def insert_front(self, element):
        if self.size > self.queue_size:
            return -1
        if self.queue_size == 0:
            self.queue.append(element)
        else:
            self.queue.insert(0, element)

    def insert_rear(self, element):
        if self.size > self.queue_size:
            return -1
        self.queue.append(element)

    def delete_front(self):
        if self.queue_size == 0:
            return -1
        return self.queue.pop(0)

    def delete_rear(self):
        if self.queue_size == 0:
            return -1
        return self.queue.pop()

    def get_front(self):
        if self.queue_size == 0:
            return -1
        return self.queue[0]

    def get_rear(self):
        if self.queue_size == 0:
            return -1
        return self.queue[-1]