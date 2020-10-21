# 12. Faça uma função no Python que, utilizando
# a ferramenta turtle, desenhe um círculo de raio N.

import turtle

def draw_circle(n):
    """
    This function uses the turtle lib to draw a circle.
    n is the radius of the parameter.
    :param n:
    :return:
    """
    t_draw = turtle.Turtle()
    t_draw.circle(n)
    turtle.done()
#MAIN
n = float(input("Insert the lenght of the circle`s radius: "))
draw_circle(n)