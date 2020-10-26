# Dado um valor N do usuário, desenhe com a ferramenta turtle a seguinte imagem:
# Para ela, a tartaruga aumenta o passo andado em um e gira 90 graus após cada movimentação.
# https://lms.infnet.edu.br/moodle/pluginfile.php/732782/mod_assign/intro/xki-DtKYmHWRInIlGVnkVLm2ujfJcIGK9U7XWQU4ERQFPHmLvDRYUtOHcgla-WyY-n4IVTjQTEJX40Y0Z4brpsdQDBflCS347NgIQJbunagwS40aK1cqb-1KAyl5_uZQjHurTYJx.jpg

import turtle

def drawContinuousLoop(numberOfrotations):
    """

    :param numberOfrotations:
    :return:
    """
    turtle.Turtle()
    turtle.pencolor("red")
    length = 2
    for n in range(numberOfrotations):
        for index in range(4):
            turtle.forward(length)
            turtle.right(90)
            length += 1

    turtle.done()

drawContinuousLoop(55)