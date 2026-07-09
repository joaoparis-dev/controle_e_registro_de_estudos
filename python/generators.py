# Os generators são uma forma simples de fazer com que uma função
# retorne um valor por vez, em vez de retornar uma lista inteira.
# Isso pode ser mais eficiente no uso da memória quando há muitos dados.
# Para isso, utilizamos a palavra-chave 'yield' no lugar de 'return'.

def retornar_cada_numero():
    for i in range(0, 11):
        yield i


numero = retornar_cada_numero()

print(numero)
print(next(numero))
print(next(numero))
print(next(numero))
