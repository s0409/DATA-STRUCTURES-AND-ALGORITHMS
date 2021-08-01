class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def reverse(self):
        prev=None
        current=self.head
        next=None
        while current is not None:
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
neww=Linkedlist()
neww.push(20)
neww.push(4)
neww.push(15)
neww.push(85)
print("given linkedlist")
neww.printList()
neww.reverse()
print("reversed",sep=" ")
neww.printList()


