# Utilizando a ferramenta turtle, desenhe uma série
# de quadrados um do lado do outro como indicada na
# figura a seguir:

import turtle

t = turtle.Turtle()
t.backward(300)

for index in range(4):
    for index in range(4):
        t.forward(100)
        t.right(90)
    t.forward(100)

turtle.done()
