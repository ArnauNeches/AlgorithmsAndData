#UnorderedList class implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next
    def set_next(self, next):
        self.next = next 

class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count
    
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
               current = current.get_next()
        return found
    
    def remove(self, item):
        previous = None
        current = self.head
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        
        if previous == None:
            self.head == current.get_next()
        else:
            previous.set_next(current.get_next)

    
                