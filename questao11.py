# 11. Faça uma função no Python que, utilizando a
# ferramenta turtle, desenhe um triângulo de lado N.
import turtle

def draw_triangle(n):
    """
    This function uses the turtle lib to draw a triangle.
    n is the length of the parameter.
    :param n:
    :return:
    """
    t_draw = turtle.Turtle()
    for index in range(3):
        t_draw.forward(n)
        t_draw.right(120)
#MAIN
n = float(input("Insert the lenght of the triangle`s side: "))
draw_triangle(n)
turtle.done()