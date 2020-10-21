# 8. Escreva um programa em Python que receba três valores reais X, Y e Z,
# guarde esses valores numa tupla e verifique se esses valores podem ser
# os comprimentos dos lados de um triângulo e, neste caso, retorne qual
# o tipo de triângulo formado.
#
# Para que X, Y e Z formem um triângulo é necessário que a seguinte
# propriedade seja satisfeita: o comprimento de cada lado de um triângulo
# deve ser menor do que a soma do comprimento dos outros dois lados.
# Além disso, o programa deve identificar o tipo de triângulo formado
# observando as seguintes definições:
#
#     Triângulo Equilátero: os comprimentos dos três lados são iguais.
#     Triângulo Isósceles: os comprimentos de dois lados são iguais.
#     Triângulo Escaleno: os comprimentos dos três lados são diferentes.

def verify_triangle(x, y, z):
    """
    Verify the length of the sides of 3 sides and
    return if it can be a triangle and the triangle's type.

    :param x:
    :param y:
    :param z:
    :return type_triangle:
    """
    type_triangle = ""

    if x < y + z and y < x + z and z < x + y:
        if x == y and y == z:
            type_triangle = "Equilátero"
        elif (x == y and x != z) or (x != y and x == z) or (x != z and y == z):
            type_triangle = "Isósceles"
        elif x != y and x != z and y != z:
            type_triangle = "Escaleno"
    else:
        type_triangle = "Não se encaixa nas regras para ser um triângulo!"

    return type_triangle

x = int(input("Please insert the X side lenght: "))
y = int(input("Please insert the Y side lenght: "))
z = int(input("Please insert the Z side lenght: "))
print(verify_triangle(x, y, z))