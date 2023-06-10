import logging
from math import sin, cos, tan
from get_logger import get_logger

logger = get_logger(
    name=__name__,
    level=logging.ERROR,
    format="%(name)s - %(levelname)s: %(message)s",
    file_name="funcoes.log"
)

def seno(x):
    return sin(x)

def cosseno(x):
    return cos(x)

def tangente(x):
    return tan(x)

def cotangente(x):
    try:
        return 1/tangente(x)
    except ZeroDivisionError:
        logger.error("cotangente de 0 tende ao infinito.")