# 10. Faça uma função no Python que, utilizando a ferramenta turtle,
# desenhe um quadrado de lado N.
import turtle

def draw_square(n):
    """
    This function uses the turtle lib to draw a square.
    n is the length of the parameter.
    :param n:
    :return:
    """
    t_draw = turtle.Turtle()
    for index in range(4):
        t_draw.forward(n)
        t_draw.right(90)

#MAIN
n = float(input("Insert the lenght of the square`s side: "))
draw_square(n)
turtle.done()