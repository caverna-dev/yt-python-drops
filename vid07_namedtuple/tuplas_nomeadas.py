 #                                 _ _               _
 #                                | | |             | |
 #  _ __   __ _ _ __ ___   ___  __| | |_ _   _ _ __ | | ___
 # | '_ \ / _` | '_ ` _ \ / _ \/ _` | __| | | | '_ \| |/ _ \
 # | | | | (_| | | | | | |  __/ (_| | |_| |_| | |_) | |  __/
 # |_| |_|\__,_|_| |_| |_|\___|\__,_|\__|\__,_| .__/|_|\___|
 #                                            | |
 #                                            |_|

# - é uma extensão de 'tuple', mantendo as mesmas características básicas:
#     - ordem
#     - imutabilidade
#     - permite duplicação
# - define-se nomes para cada um dos elementos que devem existir dentro da namedtuple
# - em vez de obter itens através de um índice (posição), usa-se o nome definido
# - pelo fato de namedtuples serem tupes, é perfeitamente possível continuar usando o índice para acessar
#   um elemento.
# - um comportamento parecido com dicionárions, mas garantindo ordem e imutabilidade





# Cenário:
# Um programa que controla uma fila de atendimento a clientes.
# Cada cliente é representado por uma tupla contendo dados do
#  - Nome
#  - Sobrenome
#  - Idade
#  - Posicao na fila de atendimento



# Implementação com tuples
# cliente_a = ("Morty", "Smith", 15, 17)
# print(cliente_a)
# print(f"Nome: {cliente_a[0]}")
# print(f"Sobrenome {cliente_a[1]}")
# print(f"Idade: {cliente_a[2]}")
# print(f"Posição: {cliente_a[3]}")




# Implementação com namedtuples
from collections import namedtuple

Customer = namedtuple("Cliente", ["nome", "sobrenome", "idade", "posicao"])
cliente_b = Customer("Jerry", "Smith", 40, 10)
print(cliente_b)
print(f"Nome: {cliente_b.nome}")
print(f"Sobrenome {cliente_b.sobrenome}")
print(f"Idade: {cliente_b.idade}")
print(f"Posição: {cliente_b.posicao}")


#### Traçando um paralelo entre namedtuples e classes em python
class Cliente:
    def __init__(self, nome, sobrenome, idade, pos):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.posicao = pos

    def __str__(self):
        return f"Cliente(nome='{self.nome}', sobrenome='{self.sobrenome}', idade={self.idade}, posicao={self.posicao})"

cliente_c = Cliente("Jerry", "Smith", 40, 10)
print(cliente_c)
print(f"Nome: {cliente_c.nome}")
print(f"Sobrenome {cliente_c.sobrenome}")
print(f"Idade: {cliente_c.idade}")
print(f"Posição: {cliente_c.posicao}")