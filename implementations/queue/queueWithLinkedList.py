class LinkedNode:
    def __init__(self, value):
        self.val = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, value):
        node = LinkedNode(value)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def dequeue(self):
        if self.head:
            self.head = self.head.next
        return None

    def empty(self):
        if self.head:
            return False
        else: return True


    def __str__(self):
        string = ""
        node = self.head
        while node:
            string += f"[{node.val}] -> "
            node = node.next
        string += "end"
        return string

queue = Queue()
print(queue.empty())
queue.enqueue(10)
queue.enqueue(24)
queue.enqueue(12)
queue.enqueue(415)
print(queue)
print(queue.dequeue())
print(queue)
print(queue.empty())