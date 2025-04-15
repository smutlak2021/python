class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

        
class LinkedList:
    def __init__(self, data):
        self.head = None
        self.tail = None
        self.data = data

    def traversal(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        print("Null")

    def search(self, key):
        current = self.head
        while current:
            if(current.data ==key):
                return True
        return False

    def insert(self, data):
        if self.head is None:
            self.head = self.tail = Node(data)

