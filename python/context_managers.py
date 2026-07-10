from contextlib import contextmanager

# Um context manager controla o comportamento de um bloco with.
# Ao entrar no bloco, o Python executa __enter__().
# Ao sair do bloco (com ou sem erro), executa __exit__().

class Exemplo:
    def __enter__(self):
        print("rodando bloco enter")
        return self

    def funcao_principal(self):
        self.soma = 1+1
        return self.soma

    def __exit__(self, exc_type, exc, tb):
        print("rodando bloco exit")

with Exemplo() as e:
    print(e.funcao_principal())

# O __exit__() sempre será executado ao sair do bloco with,
# mesmo que uma exceção seja lançada.

# Context managers são muito utilizados para garantir a liberação
# de recursos, como fechar arquivos, conexões com banco de dados,
# sockets e locks, mesmo quando ocorre uma exceção.

# Outra forma de implementar um context manager é utilizando
# o decorator @contextmanager e a instrução yield.
#
# O código antes do yield equivale ao __enter__().
# O código depois do yield equivale ao __exit__().



@contextmanager
def exemplo():

    print("Entrando")

    yield

    print("Saindo")

with exemplo():
    print("dentro")