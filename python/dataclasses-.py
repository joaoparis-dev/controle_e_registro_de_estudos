
# dataclasses: uma forma de representar entidades focadas no armazenamento de dados.
# Uma classe feita com @dataclass já vem com os métodos __init__, __repr__ e __eq__ gerados automaticamente.
# Isso reduz muito código repetitivo e melhora a legibilidade.
# no codigo a seguir irei criar uma classe com dataclass


from dataclasses import dataclass


"""@dataclass
class Pessoa:
    nome: str
    idade: int
    cidade: str


p1 = Pessoa("joao", 20, "osasco")

print(p1)"""

# a saida desse codigo é Pessoa(nome='joao', idade=20, cidade='osasco') isso mostra que essa classe tem um metodo repr

"""p2 = Pessoa("joao", 20, "osasco")

print(p1 == p2)"""

# ja a saida True mostra que nessa classe tambem existe um metodo eq

# O método __post_init__ é executado automaticamente logo após o __init__
# gerado pela dataclass, permitindo realizar validações ou inicializações adicionais.
@dataclass
class Pessoa_adulta:
    nome: str
    idade: int
    cidade: str

    def __post_init__(self):
        if self.idade < 18:
            raise ValueError("A idade deve ser maior ou igual a 18 anos.")
        
pa=Pessoa_adulta("joao", 17, "osasco")