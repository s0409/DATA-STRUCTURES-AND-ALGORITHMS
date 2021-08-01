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
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return 1
        return 0

    def removeloop(self):
        fast = self.head.next
        slow = self.head
        while fast != slow:
            if fast is None and fast.next is None:
                return
            fast = fast.next.next
            slow = slow.next
        size = 1
        fast = fast.next
        while fast != slow:
            fast = fast.next
            size += 1

        slow = self.head
        fast = self.head
        for _ in range(size-1):
            fast = fast.next
        while fast.next != slow:
            fast = fast.next
            slow = slow.next
        fast.next = None


llist = LinkedList()
llist.push(10)
llist.push(4)
llist.push(15)
llist.push(20)
llist.push(50)
llist.head.next.next.next.next.next = llist.head.next.next

llist.removeloop()

print("Linked List after removing loop")
llist.printlist()
