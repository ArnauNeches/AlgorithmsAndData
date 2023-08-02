#Stack implementation in python

class Stack:

    def __init__(self):
        self.items = []
    def __repr__(self):
        return "Stack("+str(self.items)+")"

    def is_empty(self):
        if self.items == []:
            return True
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    
#Write a function rev_string(my_str) that uses a stack to reverse the characters in a string.

def rev_string(my_string):
    s = Stack()
    res = ""

    for char in my_string:
        s.push(char)
    while not s.is_empty():
        res += str(s.pop())

    return res

if __name__ == "__main__":
    print(rev_string("Hola"))

    