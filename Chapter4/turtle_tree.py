import turtle

my_turtle = turtle.Turtle()
my_win = turtle.Screen()

def tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(30)
        tree(branch_len - 15, t)
        t.left(60)
        tree(branch_len - 15, t)
        t.right(30)
        t.backward(branch_len)

if __name__ == "__main__":
    my_turtle.left(90)
    my_turtle.up()
    my_turtle.backward(100)
    my_turtle.down()
    my_turtle.color("green")
    tree(75, my_turtle)
    my_win.exitonclick()