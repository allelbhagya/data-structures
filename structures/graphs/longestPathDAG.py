# longest path in an unweighted Directed Acyclic Graph (DAG) algorithm is used to find the maximum length path in a DAG

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,value):
        self.queue.append(value)
    def isEmpty(self):
        return(self.queue==[])
    def dequeue(self):
        v = None
        if not self.isEmpty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return v
    def __str__(self):
        return(str(self.queue))
    
def longestpathlist(AList):
    (indegree,lpath) = ({},{})
    zerodegreeQ = Queue()
    for u in AList.keys():
        (indegree[u], lpath[u]) = (0,0)
    for u in AList.keys():
        for v in AList[u]:
            indegree[v] = indegree[v]+1
    for u in AList.keys():
        if indegree[u] == 0:
            zerodegreeQ.enqueue(u)
    
    while(not zerodegreeQ.isEmpty()):
        curr_vertex = zerodegreeQ.dequeue()
        indegree[curr_vertex] = indegree[curr_vertex] - 1

        for adj_vertex in AList[curr_vertex]:
            indegree[adj_vertex] = indegree[adj_vertex]- 1
            lpath[adj_vertex] = max(lpath[adj_vertex], lpath[curr_vertex]+1)
            if indegree[curr_vertex] ==0:
                zerodegreeQ.enqueue(adj_vertex)
    return(lpath)


AList={0: [2, 3, 4], 1: [2, 7], 2: [5], 3: [5, 7], 4: [7], 5: [6], 6: [7], 7: []}
print(longestpathlist(AList))