class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None
    
    def insertFront(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def insertEnd(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current
    def delNode(self, data):
        if self.isEmpty():
            return 
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                break
            current = current.next
    def printList(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

DLL = DoublyLinkedList()
for i in range(10,21,2):
    DLL.insertEnd(i)
for i in range(-10, -21,-2):
    DLL.insertFront(i)
DLL.printList()
