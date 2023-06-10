#     _______   ___    __   _    __
#    / ____/ | / / |  / /  | |  / /___ ___________
#   / __/ /  |/ /| | / /   | | / / __ `/ ___/ ___/
#  / /___/ /|  / | |/ /    | |/ / /_/ / /  (__  )
# /_____/_/ |_/  |___/     |___/\__,_/_/  /____/

import os
import random

# lendo variáveis de ambiente
# home_var = os.environ.get('HOME')
# print(f"O diretório HOME do usuário é: {home_var}")


# definindo uma variável de ambiente
# usuarios_online = random.randint(0, 1000000)
# os.environ["ONLINE_USERS"] = str(usuarios_online)
# print(f"O numero de usuarios online é: {os.environ.get('ONLINE_USERS')}")


#carregando variáveis para o ambiente a partir de um arquivo .env
from dotenv import load_dotenv
load_dotenv("credenciais_locais.env")
print(os.environ.get('DB_NAME'))
print(os.environ.get('DB_USER'))
print(os.environ.get('DB_PASSWD'))

