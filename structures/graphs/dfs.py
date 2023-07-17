class Stack:
    def __init__(self):
        self.stack = []
    def Push(self, v):
        self.stack.append(v)
    def isempty(self):
        return(self.stack == [])
    def Pop(self):
        v = None
        if not self.isempty():
            v = self.stack.pop()
            return v
        
def DFS(AList, start):
    visited = {}
    for each_vertex in AList.keys():
        visited[each_vertex] = False
    s = Stack()
    s.Push(start)
    while(not s.isempty()):
        current = s.Pop()
        if visited[current] == False:
            visited[current] = True
            for adj_vertex in AList[current]:
                if (not visited[adj_vertex]):
                    s.Push(adj_vertex)
    return visited
AList ={0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: [], 5:[]}
print(DFS(AList,0))