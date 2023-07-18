class MyCircularQueue(object):

    def __init__(self, k):
        self.head = 0
        self.tail = 0
        self.size = 0
        self.k = k
        self.queue = [None]*k
        

    def enQueue(self, value):
        if self.isFull(): 
            return False
        self.queue[self.tail] = value
        self.size +=1
        self.tail = (self.tail+1)%self.k
        return True
        

    def deQueue(self):
        if self.isEmpty(): 
            return False
        self.size -=1
        self.head = (self.head+1)%self.k
        return True
        

    def Front(self):
        if self.isEmpty() : return -1
        return self.queue[self.head]
        

    def Rear(self):
        if self.isEmpty(): return False
        return self.queue[self.tail - 1]
        

    def isEmpty(self):
        if self.size == 0: return True
        return False
        

    def isFull(self):
        if self.size == self.k : return True
        return False
        

