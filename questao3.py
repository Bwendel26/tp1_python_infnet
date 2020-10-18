# 3. Escreva uma função em Python que calcule o fatorial de um dado
# número N usando um for. O fatorial de N=0 é um. O fatorial de N é
# (para N > 0): N x (N-1) x (N-2) x … x 3 x 2 x 1. Por exemplo, para N=5
# o fatorial é: 5 x 4 x 3 x 2 x 1 = 120. Se N for negativo, exiba uma
# mensagem indicando que não é possível calcular seu fatorial.

def calc_fat(number):
    """
    This func returns the fatorial of the number(parameter).
    :param number:
    :return int fatorial:
    """
    fatorial = 0
    if number == 0:
        fatorial = 1
    elif number > 0:
        fatorial = 1
        for current_number in range(number, 0, -1):
            fatorial *= current_number

    else:
        fatorial = "It`s not possible to calc this fatorial; Negative number."

    return fatorial
#MAIN
number = int(input("Please insert a number: "))
print(calc_fat(number))
