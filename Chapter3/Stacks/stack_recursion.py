#We will implement the function that converts from decimal to other bases using stacks
from Stack import Stack

r_stack = Stack()

def to_str(n, base):
    convert_string = "0123456789ABCDEF"

    while n > 0:
        if n < base:
            r_stack.push(convert_string[n])
        else:
            r_stack.push(convert_string[n % base])
        n = n // base

    res = ""
    while not r_stack.is_empty():
        res = res + str(r_stack.pop())

    return res

if __name__ == "__main__":
    print(to_str(255,16))