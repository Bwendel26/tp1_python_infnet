# 5. Trabalhar com tuplas é muito importante!
# Crie 4 funções nas quais:
#  Dada uma tupla e um elemento, verifique se o elemento existe na tupla e retorne o indice do mesmo
#  Dada uma tupla, retorne 2 tuplas onde cada uma representa uma metade da tupla original.
#  Dada uma tupla e um elemento, elimine esse elemento da tupla.
#  Dada uma tupla, retorne uma nova tupla com todos os elementos invertidos.

#  Dada uma tupla e um elemento, verifique se o elemento existe na tupla e retorne o indice do mesmo
def tup_index(tuple, element):
    # The tuple method index already make it.
    """

    :param tuple:
    :param element:
    :return:
    """
    index = None

    for i in range(len(tuple)):
        if element == tuple[i]:
            index = i

    if index == None:
        index = "This element does not exists in this tuple."

        return index
# tup = (1, 2, 3, "a")
# print(tup_index(tup, "a"))
# NOT WORKING...

#  Dada uma tupla, retorne 2 tuplas onde cada uma representa uma metade da tupla original.
def slice_tup(tuple):
    """

    :param tuple:
    :return:
    """
    tup_middle = len(tuple) // 2
    tup1 = (tuple[0: tup_middle + 1])
    tup2 = (tuple[tup_middle + 1:])
    return tup1, tup2
#MAIN
# tuple = (1, 2 , 3, 4, 5)
# print(slice_tup(tuple))

#  Dada uma tupla e um elemento, elimine esse elemento da tupla.
def remove_el_tup(tuple, element):
    """

    :param tuple:
    :param element:
    :return:
    """
    el_index = 0
    last_el = False
    for index in range(len(tuple)):
        if element == tuple[index]:
            el_index = index
            if index + 1 == len(tuple):
                last_el = True

    if last_el:
        new_tuple = (tuple[:index])

    else:
        new_tuple = (tuple[:index] + tuple[index + 1:]) #erro

    return new_tuple
#MAIN
# tuple = (1, 2, 3, 4)
# tuple2 = (5)
# print(tuple + tuple2)
# print(remove_el_tup(tuple, 1))

#  Dada uma tupla, retorne uma nova tupla com todos os elementos invertidos.

def invert_tup(tuple):
    """

    :param tuple:
    :return:
    """
    new_tup = (tuple[::-1])
    return new_tup

# tuple = (1, 2, 3)
# print(invert_tup(tuple))