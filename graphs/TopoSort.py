class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,item):
        self.queue.append(item)
    def isEmpty(self):
        return(self.queue==[])
    def dequeue(self):
        item=None
        if not self.isEmpty():
            item = self.queue[0]
            self.queue= self.queue[1:]
        return item
    def __str__(self):
        return(str(self.queue))
    

def topoSort(AList):
    (indegree,toposortlist) = ({},[])
    zerodegreeQ = Queue()
    for u in AList.keys():
        indegree[u] = 0
    
    for u in AList.keys():
        if indegree[u] == 0:
            zerodegreeQ.enqueue(u)
    
    while(not zerodegreeQ.isEmpty()):
        curr_vertex = zerodegreeQ.dequeue()
        toposortlist.append(curr_vertex)
        indegree[curr_vertex] = indegree[curr_vertex] - 1
        for adj_vertex in AList[curr_vertex]:
            indegree[adj_vertex] = indegree[adj_vertex] -1
            if indegree[adj_vertex] == 0:
                zerodegreeQ.enqueue(adj_vertex)
    return(toposortlist)
    

AList = {0: [2, 3, 4], 1: [2, 7], 2: [5], 3: [5, 7], 4: [7], 5: [6], 6: [7], 7: []}
print(topoSort(AList))
