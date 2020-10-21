# 13. Usando a função obtida na questão 10, desenhe n quadrados
# um dentro de outro como mostrado na figura:

import turtle

def draw_square_loop(n):
    """
    This function uses the turtle lib to draw a square loop.
    n is the quantity of squares in this loop..
    :param n:
    :return:
    """
    initial_val = 250

    t_draw = turtle.Turtle()
    for qtt_square in range(n):
        for side in range(4):
            t_draw.forward(initial_val)
            t_draw.right(90)
        t_draw.penup()
        t_draw.forward(initial_val * 0.125)
        t_draw.right(90)
        t_draw.forward(initial_val * 0.125)
        t_draw.left(90)
        t_draw.pendown()
        initial_val *= 0.75

    turtle.done()
#MAIN
n = int(input("Insert the number of squares to draw: "))
draw_square_loop(n)