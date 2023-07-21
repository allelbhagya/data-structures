V = [0,1,2,3,4]
E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)]
UE = E + [ (j,i) for (i,j) in E] # each edge represented by two tuple (u,v) and (v,u)
size = len(V)
AList = {}
for i in range(size):
    AList[i] = []
for (i,j) in UE:
    AList[i].append(j)
print(AList)