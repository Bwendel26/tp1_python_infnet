# Baseando no código criado na questão anterior, crie uma função
# na qual dado um N obtido através do usuário, sua tartaruga gire
# 90 + N graus. Teste para 1, 4 e 10 para obter as figuras a seguir.
# https://lms.infnet.edu.br/moodle/pluginfile.php/732782/mod_assign/intro/btubfaACLC_uTGBvm81TaPCvjXmOcXVyetvBevb6N3sm9c77sdOxuKitz0BYhzSQWCts7Es6P2biie9le3fkyvqxpMWXHvhSFF8gIAb_oj6SxDuJ1zaxZmk8ubtuMZD4T0wIAo6B.jpg
# https://lms.infnet.edu.br/moodle/pluginfile.php/732782/mod_assign/intro/whapTV7ioZNu3r9GBqurYTpPZbpsdKLnhM9HYL4L2tXHZNVtn5JINIB-tvM1SoXDlycMf1UXmhwVoyOeu21cJyib4uyuQLMj8ic3430osE-glXju-KpnvY3lImw_Y3Kd2T2btRfi.jpg
# Teste quais outras figuras você pode gerar com o mesmo código, apenas alterando o ângulo.

import turtle

def drawContinuousLoop(numberOfRotations, rotationDegrees):
    """

    :param numberOfrotations:
    :return:
    """
    turtle.Turtle()
    turtle.pencolor("red")
    length = 2
    for n in range(numberOfRotations):
        for index in range(4):
            turtle.forward(length)
            turtle.right(90 + rotationDegrees)
            length += 1

    turtle.done()

drawContinuousLoop(55, 1)