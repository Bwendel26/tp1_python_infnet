import turtle

def geraPontos(i):
    """
    Gera pontos para quadrados de qualquer tamanho
    :param i:
    :return:
    """
    lista = [(i, 0), (i, i), (0, i), (0, 0)]
    return lista

def desenhaPoligono(inicio, pontos, corLinha="black", corRecheio="white"):
    turtle.pencolor(lineColour)
    turtle.fillcolor(fillColour)

    turtle.penup()

    turtle.goto(inicio)

    turtle.pendown()
    turtle.begin_fill()

    x, y = start

    for ponto in pontos:
        dx, dy = ponto
        turtle.goto(x + dx, y + dy)
    turtle.goto(inicio)

    turtle.end_fill()
    turtle.penup()


def teste():
    # Primeiro quadrado
    quadrado = [(50, 0), (50, 50), (0, 50), (0, 0)]
    desenhaPoligono((200, 200), quadrado)

    # Segundo quadrado
    quadrado_maior = geraPontos(100)
    desenhaPoligono((-200, 200), quadrado_maior, cor="green")

    # Triangulo
    triangulo = [(200, 0), (100, 100), (0, 0)]
    desenhaPoligono((100, -100), triangulo, cor="green")


def main():
    teste()
    turtle.done()

main()

'''
    
'''