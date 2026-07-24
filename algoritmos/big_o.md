# Big O (Notação O Grande)

## O que é?

Big O é uma notação utilizada para medir a eficiência de um algoritmo, mostrando como seu número de operações cresce conforme o tamanho da entrada (`n`) aumenta.

Ela **não mede o tempo em segundos**, mas sim o comportamento do algoritmo em grandes volumes de dados.

---

## Complexidade de Tempo

Representa a quantidade de operações executadas por um algoritmo.

Quanto menor o crescimento, mais eficiente é o algoritmo.

---

## Complexidade de Espaço

Mede a quantidade de memória utilizada pelo algoritmo durante sua execução.

---

# Principais Complexidades

| Complexidade | Descrição |
|--------------|-----------|
| **O(1)** | Tempo constante. Não depende do tamanho da entrada. |
| **O(log n)** | Logarítmica. Elimina parte do problema a cada etapa (ex.: busca binária). |
| **O(n)** | Linear. Percorre todos os elementos uma vez. |
| **O(n log n)** | Muito eficiente para algoritmos de ordenação (Merge Sort, Heap Sort, Quick Sort). |
| **O(n²)** | Quadrática. Geralmente causada por dois laços aninhados. |
| **O(2ⁿ)** | Exponencial. Cresce muito rapidamente. |
| **O(n!)** | Fatorial. Utilizada em problemas de permutação; inviável para grandes entradas. |

---

# Como identificar

## Operação constante

```python
print(lista[0])
```

**Complexidade:** `O(1)`

## Um laço

```python
for item in lista:
    print(item)
```

**Complexidade:** `O(n)`

## Dois laços aninhados

```python
for i in lista:
    for j in lista:
        print(i, j)
```

**Complexidade:** `O(n²)`

## Dois laços separados

```python
for i in lista:
    ...

for j in lista:
    ...
```

**Complexidade:** `O(n)` (n + n = 2n → O(n))

---

# Regras do Big O

- Ignore constantes (`O(2n)` → `O(n)`).
- Considere apenas o termo dominante (`O(n² + n)` → `O(n²)`).
- Laços aninhados multiplicam.
- Laços consecutivos somam.

---

# Complexidade das Estruturas de Dados

| Estrutura | Operação | Complexidade |
|-----------|----------|--------------|
| **list** | Acesso por índice | O(1) |
| | Busca | O(n) |
| | append() | O(1) amortizado |
| | Inserção/remoção no início | O(n) |
| **dict** | Buscar, inserir e remover | O(1) (caso médio) |
| **set** | Buscar, inserir e remover | O(1) (caso médio) |

---

# Resumo

- Big O mede a eficiência de um algoritmo.
- Analisa o crescimento das operações conforme a entrada aumenta.
- As complexidades mais importantes são:
  - **O(1)**
  - **O(log n)**
  - **O(n)**
  - **O(n log n)**
  - **O(n²)**
  - **O(2ⁿ)**
  - **O(n!)**
- Um bom algoritmo deve escalar bem para grandes quantidades de dados.
- Conhecer Big O ajuda a escolher algoritmos e estruturas de dados mais eficientes.