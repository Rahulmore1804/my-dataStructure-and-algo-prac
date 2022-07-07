
class node:
    def __init__(self,value):
        self.value = value
        self.next = None
class grp:
    def __init__(self,numberOfVertices):
        self.NumberOfVertices = numberOfVertices
        self.addressofvertices  = [None] *  self.NumberOfVertices

    def edge(self,sorce,target):
        Newnode = node(target)
        Newnode.next = self.addressofvertices[sorce]
        self.addressofvertices[sorce] = Newnode

        Newnode = node(sorce)
        Newnode.next = self.addressofvertices[target]
        self.addressofvertices[target] = Newnode
    
    def printlist(self):
        for i in range(self.NumberOfVertices):
            temp = self.addressofvertices[i]
            while temp:
                print(temp.value)
                temp = temp.next
            print('\n')

k = 5
gg = grp(k)
gg.edge(0,1)
gg.edge(0,4)
gg.edge(1,2)
gg.edge(1,3)
gg.edge(1,4)
gg.edge(2,3)
gg.edge(3,4)
gg.printlist()


        
        