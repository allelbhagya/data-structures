class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLL:

    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head is None
    
    def insertFront(self, data):
        new_node = Node(data)
        if self.isEmpty():
            new_node.next = new_node # will be pointing to itself
            self.head = new_node
        else:
            current = self.head
            while current.next is not self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insertEnd(self, data):
            new_node = Node(data)
            if self.isEmpty():
                new_node.next = new_node
                self.head = new_node
            else:
                current = self.head
                while current.next is not self.head:
                    current = current.next
                current.next = new_node
                new_node.next = self.head
        
    def delNode(self, data):
            if self.isEmpty():
                return 
            if self.head.data == data:
                current = self.head
                while current.next is not self.head:
                    current = current.next
                if self.head == self.head.next:
                    self.head = None
                else:
                    current.next = self.head.next
                    self.head = self.head.next
            else:
                current = self.head
                prev = None
                while current.next is not self.head:
                    if current.data == data:
                        prev.next = current.next
                        break
                    if current.data == data:
                        prev.next = self.head
    def display(self):
            current = self.head
            while True:
                print(current.data)
                current = current.next
                if current == self.head:
                    break
        


cll = CircularLL()
for i in range(1,11):
    cll.insertEnd(i)
cll.display()