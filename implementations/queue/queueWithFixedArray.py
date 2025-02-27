
class Queue:
    def __init__(self, size):
        self.size = size
        self.currentIndex = 0
        self.values = size*[None] 


    def empty(self):
        if self.values[0] == None:
            return True
        return False

    def enqueue(self, value):
        if self.currentIndex >= self.size:
            raise RuntimeError("queue is full")
        self.values[self.currentIndex] = value
        self.currentIndex+=1

    def dequeue(self):
        if len(self.values) == 0:
            raise RuntimeError("queue is empty")
        return self.values.pop(0)


    def __str__(self):
        return str(self.values) 


queue = Queue(3)
print(queue.empty())
queue.enqueue(10)
queue.enqueue(24)
queue.enqueue(415)
print(queue)
##queue.enqueue(1231)
print(queue.empty())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue)
print(queue.dequeue())