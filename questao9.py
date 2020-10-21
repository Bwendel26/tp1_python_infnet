# 9. Faça uma função que desenhe o triângulo
# obtido na questão 7 com a ferramenta turtle.

import turtle
from questao8 import verify_triangle

def draw_triangle(tup):
    """
    This function draw a Triangle, receiving a tuple
    and destructuring the values invariables to take
    the sides of the triangle.
    :param tup:
    :return:
    """
    x, y, z = tup[0], tup[1], tup[2]
    t_draw = turtle.Turtle()
    for index in range(3):
        t_draw.forward()
#         ENCONTRAR OS ANGULOS PARA FORMACAO DO TRIANGULO****

#MAIN
x = int(input("Please insert the X side lenght: "))
y = int(input("Please insert the Y side lenght: "))
z = int(input("Please insert the Z side lenght: "))
tup = (x, y, z)
can_draw = verify_triangle(tup)[1] #verify if the turtle can draw, if it will be a triangle
if can_draw:
    draw_triangle()
else:
    print("Cannot draw a triangle because the values of the sides does not match with the triangle rule.")