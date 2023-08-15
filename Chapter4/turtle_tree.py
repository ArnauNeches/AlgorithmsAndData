import turtle
from random import randint
from math import log

my_turtle = turtle.Turtle()
my_win = turtle.Screen()

def tree(branch_len, t):
    if branch_len > 5:
        num = randint(15, 45)
        num2 = randint(12, 17)
        t.pensize(log(branch_len, 1.95))
        t.forward(branch_len)
        t.right(num)
        tree(branch_len - num2, t)
        t.left(num*2)
        tree(branch_len - num2, t)
        t.right(num)
        t.backward(branch_len)

if __name__ == "__main__":
    my_turtle.left(90)
    my_turtle.up()
    my_turtle.backward(100)
    my_turtle.down()
    my_turtle.color("green")
    tree(100, my_turtle)
    my_win.exitonclick()