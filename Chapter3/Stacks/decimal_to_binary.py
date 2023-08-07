#Conversor from decimal to binary using Stack
from Stack import Stack

def divide_by_2(dec_number):
    rem_stack = Stack()

    while dec_number>0:
        rem = dec_number % 2
        rem_stack.push(rem)
        dec_number = dec_number // 2
    
    bin_string = ""
    while not rem_stack.is_empty():
        bin_string += str(rem_stack.pop())
    
    return bin_string

if __name__ == "__main__":
    print(divide_by_2(345))
    print(divide_by_2(17))
    print(divide_by_2(45))
    print(divide_by_2(96))