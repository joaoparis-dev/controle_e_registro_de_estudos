# Iterators, assim como generators, devolvem um valor por vez e se lembram de onde pararam.
# Para acessar o próximo item de um iterator, utilizamos a função next().

# Neste exemplo criamos uma classe que implementa um iterator
# por meio dos métodos especiais __iter__() e __next__().

class Contador:
    def __init__(self, max=0):
        self.max = max
        self.numero = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.numero <= self.max:
            valor = self.numero
            self.numero += 1
            return valor
        raise StopIteration


contador = Contador(5)


print(contador)
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))


# tambem podemos usar um objeto iteravel com o for
contador = Contador(5)
for numero in contador:
    print(numero)

# isso nos leva a curiosidade de saber como um for funciona internamente:
# O for primeiro chama iter(objeto) para obter um iterator.
# Depois chama next(iterator) repetidamente até que seja lançada
# a exceção StopIteration.

contador = Contador(5)

while True:
    try:
        numero = next(contador)
        print(numero)
    except StopIteration:
        print("acabaram os numeros")
        break
