# Desafío) Utilizando a ferramenta turtle, desenhe os ângulos
# de um círculo como indicado na figura a seguir:
# Utilize as funções da ferramenta turtle setheading e write,
# além de outras que sejam necessárias.

import turtle

grades = 345
t_draw = turtle.Turtle()
t_draw.right(15)

while grades >= 0:
    t_draw.forward(100)
    t_draw.write(str(grades) + "°")
    t_draw.backward(100)
    t_draw.right(15)
    grades -= 15

turtle.done()