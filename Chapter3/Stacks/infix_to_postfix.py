#function to convert from infix notation to postfix notation
from Stack import Stack 

def infix_to_postfix(infix_expr):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()
    
    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        elif token in "+*^-/":
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)
        else:
            raise ValueError("Invalid value in the expression")

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return " ".join(postfix_list)

if __name__ == "__main__":
    print(infix_to_postfix("A * B + C * D"))
    print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )")) 
    print(infix_to_postfix("5 * 3 ^ ( 4 - 2 )"))  
    print(infix_to_postfix("( A + B ) * ( C + D ) * ( E + F )"))
    print(infix_to_postfix("A + ( ( B + C ) * ( D + E ) )"))
    print(infix_to_postfix("A + ( ( B ´ C ) * ( D + E ) )"))