
# 1. Escreva uma função em Python que some todos os números ímpares de 1 até um dado N,
# inclusive. O número N deve ser obtido do usuário. Ao final, escreva o valor do
# resultado desta soma

def odd_sum(top_number):
    """
    Function that returns the odd
    numbers between 1 and the gived number.
    :param top_number:
    :return int sum:
    """
    sum = 0
    for current_number in range(top_number + 1):
        if (current_number % 2 != 0):
            sum += current_number

    return sum

#MAIN

number = int(input("Give a integer number: "))
print(odd_sum(number))