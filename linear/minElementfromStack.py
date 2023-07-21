#https://practice.geeksforgeeks.org/problems/get-minimum-element-from-stack/1?page=1&category[]=Stack&sortBy=submissions

class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        self.s.append(x)

    def pop(self):
        if self.isEmpty():
            return -1
        else:
            return self.s.pop()
        
    def isEmpty(self):
        return(len(self.s)==0)

    def getMin(self):
        if not self.isEmpty():
            minEle = self.s[0]
            for i in self.s[1:]:
                if i<minEle:
                    minEle = i
            return minEle
        else:
            return -1
