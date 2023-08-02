#We will create a funtion to check if parentheses are balanced (Closed after been oponed)

from Stack import Stack


def par_checker(symbol_string):
 s = Stack()
 index = 0
 while index < len(symbol_string):
    symbol = symbol_string[index]
    if symbol == "(":
        s.push(symbol)
    elif symbol == ")":
        if s.is_empty():
           return False
        s.pop()
    index = index + 1

 if s.is_empty():
    return True
 else:
    return False
 
print(par_checker('()(())'))