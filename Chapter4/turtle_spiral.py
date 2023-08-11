import turtle

my_turtle = turtle.Turtle()
my_win = turtle.Screen()

def draw_spiral(my_turtle, linelen):
    if linelen > 0:
        my_turtle.forward(linelen)
        my_turtle.right(90)
        draw_spiral(my_turtle, linelen-5)

if __name__ == "__main__":
    draw_spiral(my_turtle, 100)
    my_win.exitonclick()