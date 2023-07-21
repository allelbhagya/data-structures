class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,v):
        self.queue.append(v)
    def isempty(self):
        return(self.queue==[])
    def dequeue(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return v


def BFS(AList, start):
    visited = {}
    for each_vertex in  AList.keys():
        visited[each_vertex] = False
    q = Queue()
    visited[start] = True
    q.enqueue(start)

    while (not q.isempty()):
        current = q.dequeue()
        for adj_vertex in AList[current]:
            if(not visited[adj_vertex]):
                visited[adj_vertex] = True
                q.enqueue(adj_vertex)
    return(visited)

AList = {0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: [], 5:[]}
print(BFS(AList,0))