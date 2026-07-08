# Usamos *args e **kwargs quando o parâmetro da nossa função precisa aceitar uma quantidade variável de argumentos.
# O * faz com que os argumentos posicionais recebidos sejam agrupados em uma tupla, facilitando seu processamento dentro da função.
numeros = (1, 2, 2, 5)


def soma(*args):
    return sum(args)


resultado = soma(*numeros)

print(resultado)

# Já o **kwargs funciona de forma parecida, mas em vez de agrupar os argumentos em uma tupla,
# ele agrupa os argumentos nomeados em um dicionário.
# exemplo de uso de **kwargs

dicionario = { 
    "numero_1": 1,
    "numero_2": 2,
    "numero_3": 3
}


def ksoma(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave} somado a si mesmo é: {valor + valor}")

ksoma(**dicionario)
