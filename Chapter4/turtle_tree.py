import turtle
from random import randint
from math import log, floor

my_turtle = turtle.Turtle()
my_win = turtle.Screen()
total = 150

def tree(branch_len, t):
    colors = ["#239b56", "#239b56", "#186a3b", "#186a3b", "#186a3b", "#186a3b", "#9a7d0a", "#af601a", "#af601a", "#784212", "#784212"]
    if branch_len > 8:
        num = randint(15, 45)
        num2 = randint(10, 30)
        num3 = floor((branch_len / total)*10)
        t.color(colors[num3])
        t.pensize(log(branch_len, 1.7))
        t.forward(branch_len)
        t.right(num)
        tree(branch_len - num2, t)
        t.left(num*2)
        tree(branch_len - num2, t)
        t.right(num)
        t.up()
        t.backward(branch_len)
        t.down()

if __name__ == "__main__":
    my_turtle.left(90)
    my_turtle.up()
    my_turtle.backward(300)
    my_turtle.down()
    tree(total, my_turtle)
    my_win.exitonclick()