# 17. Escreva uma função que receba uma string e
# um número inteiro x e rotacione a string x
# posições para a esquerda. Assuma que a string
# tem pelo menos x caracteres.

# Isto é, utilizando como entradas a string
# “aeiou” e o inteiro 3, o resultado da sua
# função deve ser “ouaei”.

def rotatingString(rotationsNumber, string):
    """

    :param rotationsNumber:
    :param string:
    :return:
    """
    result = ""
    stringLen = len(string)

    if rotationsNumber == stringLen:
        result = string

        return result
    else:
        if rotationsNumber > stringLen:
            rotationsNumber = rotationsNumber % stringLen

        initialPart = string[rotationsNumber:]
        finalPart = string[:rotationsNumber]
        result = initialPart + finalPart

        return result
#MAIN

print(rotatingString(3, "aeiou"))