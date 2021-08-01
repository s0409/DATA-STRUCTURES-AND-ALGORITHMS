class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None


    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def sointersection(self,head1,head2):
        p1=head1
        p2=head2
        tail=None
        while p1 and p2:
            if p1.next > p2.next:
                p2=p2.next
            elif p2.next>p1.next:
                p1=p1.next
            else:
                if head is None:
                    head=tail=Node(p1.data)
                else:
                    tail.next=Node(p1.data)
                    tail=tail.next
                p1=p1.next
                p2=p2.next

        return head
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next



