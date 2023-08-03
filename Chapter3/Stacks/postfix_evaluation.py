#function to evaluate and process expressions in postfix notation
from Stack import Stack

def postfix_eval(postfic_expr):
    operand_stack = Stack()
    token_list = postfic_expr.split()

    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
        
    return operand_stack.pop()
    
def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "^":
        return op1 ** op2
    
if __name__ == "__main__":
    print(postfix_eval('7 8 + 3 2 + /'))
    print(postfix_eval('2 5 * 4 7 + +'))
    print(postfix_eval("5 3 4 2 - ^ *"))