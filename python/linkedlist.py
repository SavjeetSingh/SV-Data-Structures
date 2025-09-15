"""lets build linked lists!"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print("LinkedList:", " -> ".join(map(str, elements)))

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.display()  # Output: LinkedList: 1 -> 2 -> 3
    ll.prepend(0)
    ll.display()  # Output: LinkedList: 0 -> 1 -> 2 -> 3
    ll.delete_with_value(2)
    ll.display()  # Output: LinkedList: 0 -> 1 -> 3
    print(ll.find(3))  # Output: True
    print(ll.find(2))  # Output: False