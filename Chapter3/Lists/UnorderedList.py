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
        self.tail = None

    def is_empty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

        if self.tail == None:
            self.tail = temp

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

    def append(self, item):
        temp = Node(item)
        
        if self.is_empty():
            self.head = temp
            self.tail = temp
        else:
            self.tail.set_next(temp)
            self.tail = temp

    def index(self, item):
        found = False
        counter = 0
        current = self.head

        while not found:
            if current.get_data() == item:
                found = True
            if current.get_next() == None and not found:
                return False
            current = current.get_next()
            counter +=1
        
        return counter-1 

    def insert(self, index, item):
        temp = Node(item)

        if index <= 0 or self.head is None:
            temp.set_next(self.head)
            self.head = temp

            if self.head.get_next() is None:
                self.tail = temp
        else:
            previous = None
            current = self.head
            count = 0

            while current is not None and count < index:
                previous = current
                current = current.get_next()
                count += 1

            if current is None:
                previous.set_next(temp)
                self.tail = temp
            else:
                previous.set_next(temp)
                temp.set_next(current)
    
    def pop(self):
        if self.head is None:
            raise IndexError("pop from empty list")

        current = self.head
        previous = None

        while current.get_next() is not None:
            previous = current
            current = current.get_next()

        if previous is None:
            self.head = None
            self.tail = None
        else:
            previous.set_next(None)
            self.tail = previous

        return current.get_data()
    
    def pop(self):
        if self.head is None:
            raise IndexError("pop from empty list")

        current = self.head
        previous = None

        while current.get_next() is not None:
            previous = current
            current = current.get_next()

        if previous is None:
            self.head = None
            self.tail = None
        else:
            previous.set_next(None)
            self.tail = previous

        return current.get_data()

    def pop(self, index=None):
        if self.head is None:
            raise IndexError("pop from empty list")

        if index is None:
            return self.pop()

        if index == 0:
            data = self.head.get_data()
            self.head = self.head.get_next()
            if self.head is None:
                self.tail = None
            return data

        current = self.head
        previous = None
        count = 0

        while current is not None and count < index:
            previous = current
            current = current.get_next()
            count += 1

        if current is None:
            raise IndexError("pop index out of range")

        data = current.get_data()
        previous.set_next(current.get_next())

        if current == self.tail:
            self.tail = previous

        return data




if __name__ == "__main__":
    nlist = UnorderedList()
    nlist.add(3)
    nlist.add(7)
    nlist.append(1)
    nlist.add(5)
    print(nlist.index(5))