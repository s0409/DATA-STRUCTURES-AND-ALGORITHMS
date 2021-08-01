class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):

        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def detectloop(self):
        s = set()
        temp = self.head
        while temp:
            if temp in s:
                return True
            s.add(temp)
            temp = temp.next
        return False


llist = LinkedList()

llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
llist.head.next.next.next.next = llist.head
if llist.detectloop():
    print("loop found")
else:
    print("no loop")
