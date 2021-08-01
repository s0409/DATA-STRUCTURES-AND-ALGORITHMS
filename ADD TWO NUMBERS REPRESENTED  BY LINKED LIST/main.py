#FUNCTION FOR ADD TWO NUMBERS REPRESENTED BY LINKEDLIST
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def reverse(self):
        prev=None
        curr=head
        next=None
        while curr is None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev
    def addtwolist(self,first,second):
        first=sel.reverse(first)
        second=self.reverse(second)
        sumlist=None
        carry=0
        while first is not None or second is not None or carry>0:
            newVal=carry
            if first is not None:
                newVal+=first.data
            if second is not None:
                newVal+=second.data
            carry=newVal//10
            newVal=newVal%10
            newNode=Node(newVal)
            newNode.next=sumlist
            sumlist=newNode
            if first:
                first=first.next
            if second:
                second=second.next
        return sumlist
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
