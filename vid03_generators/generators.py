#                                  _
#                                 | |
#   __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ ___
#  / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__/ __|
# | (_| |  __/ | | |  __/ | | (_| | || (_) | |  \__ \
#  \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|  |___/
#   __/ |
#  |___/
#

import random

def lista_coordenadas_aleatorias(qty_coordenadas, max_valor):
    """
    Retorna uma lista de coordenadas aleatorias obtidas
    entre 0 e um valor máximo para X (eixo horizontal)
    e Y (eixo vertical).
    """
    coordenadas = [] # cada elemento sera uma tupla com uma coordenada x,y
    for _ in range(0, qty_coordenadas):
        coord_aleatoria = (
            random.randint(0, max_valor),
            random.randint(0, max_valor)
        )
        coordenadas.append(coord_aleatoria)
    return coordenadas


def generator_coordenadas_aleatorias(qty_coordenadas, max_valor):
    """
    Retorna um generator que produz coordenadas aleatorias obtidas
    entre 0 e um valor maximo de X (eixo horizontal)
    e Y (eixo vertical)
    """
    for _ in range(0, qty_coordenadas):
        yield (
            random.randint(0, max_valor),
            random.randint(0, max_valor)
        )


# coords_list = lista_coordenadas_aleatorias(10000000, 10000)
coords_generator = list(generator_coordenadas_aleatorias(10000000, 10000))


