# Escreva um programa em Python que calcule o fatorial
# de um dado número N usando um while. Use as mesmas
# especificações do item anterior.

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
        while number > 0:
            fatorial *= number
            number -= 1
    else:
        fatorial = "It`s not possible to calc this fatorial; Negative number."

    return fatorial
#MAIN
number = int(input("Please insert a number: "))
print(calc_fat(number))
