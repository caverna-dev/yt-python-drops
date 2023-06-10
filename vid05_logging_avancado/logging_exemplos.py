 #  _____       ___      ______     ______  _____  ____  _____   ______
 # |_   _|    .'   `.  .' ___  |  .' ___  ||_   _||_   \|_   _|.' ___  |
 #   | |     /  .-.  \/ .'   \_| / .'   \_|  | |    |   \ | | / .'   \_|
 #   | |   _ | |   | || |   ____ | |   ____  | |    | |\ \| | | |   ____
 #  _| |__/ |\  `-'  /\ `.___]  |\ `.___]  |_| |_  _| |_\   |_\ `.___]  |
 # |________| `.___.'  `._____.'  `._____.'|_____||_____|\____|`._____.'


# Por padrão, existem 5 níveis de criticidade.

# - DEBUG (10): Provê detalhes sobre a execução do programa, que interessam mais para os devs quando
# estão tentando identificar a causa-raiz de um problema.

# - INFO (20): Informações genéricas, que normalmente apenas indicam o estado do programa num dado momento.

# - WARNING (30): Informações que requerem atenção. Podem indicar que algo deu/dará errado.

# - ERROR (40): Informa que um erro não-catastrófico ocorreu e tipicamente contém algum contexto sobre o
# que levou ao erro

# - CRITICAL (50): Algum erro muito severo aconteceu, e o programa provavelmente será encerrado em função
# disto.


import logging
from math import radians
from funcoes_trigonometricas import seno, cosseno, tangente, cotangente
from get_logger import get_logger

logger = get_logger(
    name=__name__,
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
    file_name="trigonometria.log"
)



angulo_em_graus = 0
angulo_em_rads = radians(angulo_em_graus)


seno_do_angulo = seno(angulo_em_rads)
logger.info(f"O seno de {angulo_em_graus} graus é: {seno_do_angulo}")

cosseno_do_angulo = cosseno(angulo_em_rads)
logger.info(f"O cosseno de {angulo_em_graus} graus é: {cosseno_do_angulo}")

tangente_do_angulo = tangente(angulo_em_rads)
logger.info(f"A tangente de {angulo_em_graus} graus é: {tangente_do_angulo}")

cotangente_do_angulo = cotangente(angulo_em_rads)
logger.info(f"A co-tangente de {angulo_em_graus} graus é: {cotangente_do_angulo}")



