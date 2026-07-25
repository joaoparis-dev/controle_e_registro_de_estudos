# Arrays e Listas Encadeadas

## O que são?

Arrays e listas encadeadas são estruturas de dados utilizadas para armazenar coleções de elementos. Embora ambas tenham o mesmo objetivo, elas funcionam de maneiras completamente diferentes e possuem vantagens e desvantagens dependendo da situação.

---

# Arrays

Um array armazena seus elementos em posições **contíguas na memória**.

Exemplo:

```
Índice:   0    1    2    3

        +----+----+----+----+
Array:  | 10 | 20 | 30 | 40 |
        +----+----+----+----+
```

Cada posição possui um índice, permitindo acesso direto ao elemento.

## Vantagens

- Acesso por índice em **O(1)**.
- Excelente desempenho para leitura.
- Melhor aproveitamento do cache da CPU.
- Menor consumo de memória.

## Desvantagens

- Inserções no meio custam **O(n)**.
- Remoções no meio custam **O(n)**.
- Precisa de memória contínua.
- Quando o espaço acaba, pode ser necessário criar um novo array maior e copiar todos os elementos.

---

# Array Dinâmico

A lista (`list`) do Python é um **array dinâmico**.

```python
numeros = [10, 20, 30]

numeros.append(40)
```

O método `append()` normalmente possui custo **O(1) amortizado**.

Caso a capacidade seja atingida, o Python:

1. Cria um array maior.
2. Copia todos os elementos.
3. Libera o antigo.

---

# Listas Encadeadas

Uma lista encadeada é composta por vários **nós**.

Cada nó possui:

- um valor;
- uma referência para o próximo nó.

Representação:

```
HEAD

↓

+-----+-------+
| 10  |   •---|---->
+-----+-------+

               +-----+-------+
               | 20  |   •---|---->
               +-----+-------+

                              +-----+------+
                              | 30  | NULL |
                              +-----+------+
```

Os nós podem estar em qualquer posição da memória.

---

# Head

O **head** é uma referência para o primeiro nó da lista.

```
HEAD

↓

10 → 20 → 30 → NULL
```

Sem o `head`, perde-se o acesso à lista inteira.

---

# Operações

## Acesso

Para acessar um elemento é necessário percorrer a lista.

```
HEAD

↓

10

↓

20

↓

30
```

Complexidade:

```
O(n)
```

---

## Inserção

Quando já se possui a referência ao nó correto, basta alterar os ponteiros.

Antes:

```
20 ------> 40
```

Depois:

```
20 → 30 → 40
```

Não é necessário mover elementos.

---

## Remoção

Antes:

```
20 → 30 → 40
```

Depois:

```
20 ------> 40
```

O nó removido deixa de ser referenciado.

---

# Tipos de listas encadeadas

## Simples

```
10 → 20 → 30
```

Cada nó aponta apenas para o próximo.

---

## Duplamente Encadeada

```
NULL ← 10 ⇄ 20 ⇄ 30 → NULL
```

Cada nó possui:

- anterior
- próximo

Permite percorrer a lista nos dois sentidos.

---

## Circular

```
10 → 20 → 30
↑           ↓
└───────────┘
```

O último nó aponta novamente para o primeiro.

---

# Comparação

| Operação | Array | Lista Encadeada |
|----------|-------|-----------------|
| Acesso por índice | O(1) | O(n) |
| Inserção no início | O(n) | O(1) |
| Inserção no fim | O(1)* | O(n)** |
| Inserção no meio | O(n) | O(n) |
| Remoção no meio | O(n) | O(n) |

\* O(1) amortizado em arrays dinâmicos.

\** Considerando lista simples sem ponteiro para o último nó.

---

# Quando utilizar?

## Arrays

- Muitas leituras.
- Acesso rápido por índice.
- Poucas inserções e remoções.

---

## Listas Encadeadas

- Muitas inserções e remoções.
- Tamanho da estrutura varia frequentemente.
- Não há necessidade de acesso direto por índice.

---

# Complexidades

| Operação | Array | Lista Encadeada |
|----------|-------|-----------------|
| Buscar por índice | O(1) | O(n) |
| Buscar valor | O(n) | O(n) |
| Inserir início | O(n) | O(1) |
| Inserir fim | O(1)* | O(n)** |
| Inserir meio | O(n) | O(n) |
| Remover início | O(n) | O(1) |
| Remover meio | O(n) | O(n) |

---

# Resumo

- Arrays armazenam elementos em posições contíguas da memória.
- Possuem acesso extremamente rápido (**O(1)**).
- Inserções e remoções no meio exigem deslocamento de elementos (**O(n)**).

- Listas encadeadas armazenam nós ligados por referências.
- Os elementos não precisam estar lado a lado na memória.
- Inserções e remoções são rápidas quando o nó já é conhecido (**O(1)**).
- O acesso a um elemento exige percorrer a lista (**O(n)**).

No Python, a estrutura `list` é um **array dinâmico**, e não uma lista encadeada.