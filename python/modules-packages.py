"""# Módulos e Packages

# módulo é qualquer arquivo Python (.py) que contém funções, classes ou variáveis e pode ser reutilizado em outros arquivos através do import.

# Isso ajuda a organizar melhor o código e evita repetições.

```python
# calculadora.py

def soma(a, b):
    return a + b
```

```python
import calculadora

print(calculadora.soma(2, 3))
```

# package é uma pasta que reúne vários módulos relacionados, permitindo organizar projetos maiores em diferentes arquivos.

```
projeto/

├── main.py
└── utilidades/
    ├── __init__.py
    ├── calculadora.py
    └── texto.py
```

```python
from utilidades.calculadora import soma

print(soma(2, 3))
```

# o arquivo **init**.py serve para indicar que a pasta é um package e também pode ser utilizado para inicializar ou facilitar importações.

# também podemos importar apenas funções específicas ou criar apelidos para os módulos.

```python
from calculadora import soma

print(soma(2, 3))
```

```python
import calculadora as calc

print(calc.soma(2, 3))
```
"""