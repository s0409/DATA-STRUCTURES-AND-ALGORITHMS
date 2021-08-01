class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def reverse(self,head,k):
        if head is None:
            return None
        curr=head
        next=None
        prev=None
        count=0
        while curr is not None and count<k:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
            count+=1
        if  next is not None:
            head.next=self.reverse(next,k)
        return prev
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
llist=Linkedlist()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
llist.printList()
llist.head=llist.reverse(llist.head,3)
print()
llist.printList()

