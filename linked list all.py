class Node:
    def  __init__(self,value):
        self.value = value
        self.next = None
class LL():
    def __init__(self):
        self.head = None
    def reverselist(self):
        x1 = None
        current = self.head
        while current:
            mainnode = current.next
            # for making current.next to himself current
            current.next = x1
            x1 = current
            # then change poniter to forward
            current = mainnode
        self.head = x1
            
        pass
    def push(self,data):
        Node1 = Node(data)
        Node1.next  = self.head
        self.head = Node1

    def printList(self):
        temp = self.head
        while temp:
            print(f"{temp.value} ")
            temp= temp.next
pp = LL()

pp.push(3)
pp.push(5)
pp.push(8)

pp.printList()
pp.reverselist()
pp.printList()