# Type Hints são anotações que indicam quais tipos de dados
# devem ser utilizados em variáveis, parâmetros e retornos de funções.
# Elas deixam o código mais legível e ajudam a IDE a identificar erros,
# mas não impedem que outros tipos sejam usados durante a execução.

def calcular_area(base: float, altura: float) -> float:
    return base * altura


area = calcular_area(5.5, 4.0)

print(f"A área é {area}")
