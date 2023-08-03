#Function to check if parenthses are checked, extended to (), [] and {}
from Stack import Stack

def extended_par_checked(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    
    if balanced and s.is_empty():
        return True
    else:
        return False
    
def matches(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)

print(extended_par_checked("[[[{}{}{}(()())]]]"))
print(extended_par_checked("[[[[[]]]]"))