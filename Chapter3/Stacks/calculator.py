#function that combines infix to postfix and postfix evaluation
from infix_to_postfix import infix_to_postfix
from postfix_evaluation import postfix_eval

def calculator():
    stop = False
    expr = []
    while not stop:

        value = input("Next expression value: ")
        expr.append(value)
        print("Expression right now: " + " ".join(expr))

        finish = input("Would you like to finish? [y/n]: ")
        if finish == "y":
            stop = True

    expression = " ".join(expr)
    print(infix_evaluation(expression))


def infix_evaluation(infix_expr):
    return postfix_eval(infix_to_postfix(infix_expr))

if __name__ == "__main__":
    calculator()