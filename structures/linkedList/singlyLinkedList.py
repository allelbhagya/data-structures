class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    
class LinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self,data):
        new_node = Node(data)
        if(self.head):
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
    def insertFront(self,data):
        new_node = Node(data)
        first = self.head
        new_node.next = first
        self.head = new_node
    
    def insertMiddle(self, value, data):
        new_node = Node(data)
        current = self.head
        while current.next:
            if current.next.data == value:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    def deleteNode(self, key):

        current = self.head
        if (current is not None) and (current.data ==key):
            self.head = current.next
            return 
        while (current is not None):
            if current.data == key:
                break
            prev = current
            current = current.next
        prev.next = current.next


    def printList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

singlyLL = LinkedList()
for i in range(1,11):
    singlyLL.insertEnd(i)

singlyLL.insertFront(10)
singlyLL.insertMiddle(5, 100)
singlyLL.deleteNode(5)
singlyLL.printList()
