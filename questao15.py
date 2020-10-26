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
    turtle.pencolor(corLinha)
    turtle.fillcolor(corRecheio)

    turtle.penup()

    turtle.goto(inicio)

    turtle.pendown()
    turtle.begin_fill()

    x, y = inicio

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
    desenhaPoligono((-200, 200), quadrado_maior, corRecheio="green")

    # Triangulo
    triangulo = [(200, 0), (100, 100), (0, 0)]
    desenhaPoligono((100, -100), triangulo, corRecheio="green")


def main():
    teste()
    turtle.done()

main()

'''
    Primeiramente temos a função inicial que gera pontos para um quadrado,
    com uma lista de tuplas, onde cada tupla representa uma coordenada cartesiana.
    
    A função  desenhaPoligono recebe os parâmetros para o ponto inicial, a lista
    de tuplas que definem os pontos, a cor da linha e a cor do interior do polígono.
    A segunda usa os parametros pra definir as cores mencionadas anteriormente,
    levanta a "caneta" do turtle para então com a função goto ir para posição "inicial",
    logo em seguida o loop for pega ponto por ponto para percorrer e desenhar o polígono,
    no final voltando ao ponto inicial, fechando o desenho do polígono.

    A função teste define cada um dos polígonos, e chama a função desenha poligono já com os
    parâmetros passados.
    
    Então a função main chama a função teste e logo em seguida o método turtle.done(), para que
    o turtle entenda que o desenho está finalizado.
'''