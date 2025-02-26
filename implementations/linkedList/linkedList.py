class LinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        if self.head == None:
            self.head = LinkedNode(value)
            return
        node = self.head

        while node.next:
            node = node.next
        node.next = LinkedNode(value)
        return

    def size(self):
        size = 0
        node = self.head
        while node:
            size+=1
            node = node.next
        return size


    def empty(self):
        return self.head == None

    def value_at(self, index):
        node = self.head
        for i in range(index+1):
            if i == index:
                return node.value
            node = node.next

    def push_front(self, value):
        nodeToAdd = LinkedNode(value)
        nodeToAdd.next = self.head
        self.head = nodeToAdd

    def pop_front(self):
        if self.head:
            nodeToPop = self.head
            self.head = nodeToPop.next
            return nodeToPop.value
        return None

    def pop_back(self):
        node = self.head
        while node.next.next:
            node = node.next
        value = node.next.value
        node.next = None
        return value

    def front(self):
        return self.head.value if self.head else None

    def back(self):
        if not self.head:
            return None
        node = self.head
        while node.next:
            node = node.next
        return node.value

    def insert(self, index, value):
        node  = self.head
        for i in range(index-1):
            node = node.next
        nodeAfterInsertion = node.next
        insertedNode = LinkedNode(value)
        node.next = insertedNode
        node.next.next = nodeAfterInsertion
        

    def erase(self, index):
        node = self.head
        for _ in range(index-1):
            node = node.next
        node.next = node.next.next
    
    def value_n_from_end(self, n):
        node = self.head
        for _ in range(self.size() - n):
            node = node.next
        return node.value

    def reverse(self):
        node = self.head
        prev = None
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
        self.head = prev

    def remove_value(self,value):
        node = self.head
        while node.next.value != value:
            node = node.next
        node.next = node.next.next






    def __str__(self):
        listString = ""
        node = self.head
        while node:
            listString += f"[{node.value}] --> "
            node = node.next
        listString += "end"
        return listString

    

linkedList = LinkedList()
print(linkedList.back())
linkedList.append(1)
linkedList.append(2)
linkedList.append(3)
linkedList.append(4)
print(linkedList.size())
print(linkedList.empty())
print(linkedList.value_at(2))

linkedList.push_front(10)
print(linkedList.size())

print(linkedList)
print(linkedList.pop_front())
print(linkedList)
print(linkedList.pop_back())
print(linkedList)

print(linkedList.back())

linkedList.insert(2, 50)
print(linkedList)

linkedList.erase(2)
print(linkedList)

print(linkedList.value_n_from_end(1))

linkedList.reverse()
print(linkedList)

linkedList.remove_value(2)
print(linkedList)