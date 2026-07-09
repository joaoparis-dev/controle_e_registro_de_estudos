# Um decorator permite adicionar comportamentos a uma função sem alterar
# seu código original. Neste exemplo, vou criar um decorator que mede
# quanto tempo uma função leva para ser executada.
import time


def medir_tempo(funcao):
    def wrapper(*args, **kwargs):
        tempo_inicial = time.time()
        funcao(*args, **kwargs)
        tempo_final = time.time()

        print(f"o tempo de execucao foi de {tempo_final - tempo_inicial}s ")
    return wrapper


@medir_tempo
def soma(a, b):
    print(a+b)


soma(2, 4)
