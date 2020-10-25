# 14. Utilizando o código 10.1 da Etapa 2, onde utilizando
# a função onkey do turtle associamos valores às setas do
# teclado, para este exercício associe as funções obtidas
# nas questões 10, 11 e 12 às teclas ‘q’, ‘t’ e ‘c’ respectivamente.
import turtle
from questao10 import draw_square
from questao11 import draw_triangle
from questao12 import draw_circle

turtle.title("Question 14 TP1")

#MAIN
square_n = float(input("Insert the lenght of the square`s side: "))
triangle_n = float(input("Insert the lenght of the triangle`s side: "))
circle_n = float(input("Insert the lenght of the circle`s radius: "))

turtle.listen()
turtle.onkey(draw_square, 'q')
turtle.onkey(draw_triangle, 't')
turtle.onkey(draw_circle, 'c')

turtle.done()