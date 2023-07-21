class Queue:

    def __init__(self):
        self.queue = []
    
    def enqueue(self,item):
        self.queue.append(item)

    def isEmpty(self):
        return(len(self.queue)==0)
    
    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
    def display(self):
        print(self.queue)
    
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(1)
q.enqueue(2)
q.display()
print(q.dequeue())
q.display()