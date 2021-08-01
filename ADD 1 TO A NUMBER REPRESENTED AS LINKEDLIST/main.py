class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self,new_data):

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        prev = None
        curr = self.head
        next = head.next

        while curr is not None:
            next = prev.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    def addOne(self,head):
        self.head = self.reverse(head)
        curr = self.head
        carry = 1
        while(carry):
            curr.data +=1
            if curr.data < 10:
                return self.reverse(head)
            else:
                curr.data = 0
            if curr.next is None:
                break
            else:
                curr = curr.next
        curr.next = Node(1)
        return self.reverse(head)
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp=temp.next

head = LinkedList()
head = push(1)
head.next = push(9)
head.next.next = push(9)
head.next.next.next = push(9)

print("List is: ", end="")
printList(head)

head = addOne(head)

print("\nResultant list is: ", end="")
printList(head)
