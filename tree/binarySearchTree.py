class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def inorder(self, current=None):
        if current is not None:
            self.inorder(current.left)
            print(str(current.value) + " -> ", end=' ')
            self.inorder(current.right)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        if key < current.value:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert_recursive(current.left, key)
        else:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert_recursive(current.right, key)

    def minValueNode(self, current):
        while current.left is not None:
            current = current.left
        return current

    def deleteNode(self, current, key):
        if current is None:
            return current

        if key < current.value:
            current.left = self.deleteNode(current.left, key)
        elif key > current.value:
            current.right = self.deleteNode(current.right, key)
        else:
            if current.left is None:
                temp = current.right
                current = None
                return temp
            elif current.right is None:
                temp = current.left
                current = None
                return temp

            temp = self.minValueNode(current.right)
            current.value = temp.value
            current.right = self.deleteNode(current.right, temp.value)
        return current

BST = BinarySearchTree()
for i in range(1, 11):
    BST.insert(i)
BST.inorder(BST.root)
