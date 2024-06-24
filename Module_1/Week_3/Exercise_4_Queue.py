class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = list()

    def enqueue(self, param):
        if self.is_full():
            return "Queue is full"
        return self.queue.append(param)

    def is_full(self):
        return self.queue == self.capacity

    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0


queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())
print(queue1.front())
print(queue1.dequeue())
print(queue1.front())
print(queue1.dequeue())
print(queue1.is_empty())
