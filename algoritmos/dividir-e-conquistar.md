# Dividir para Conquistar (Divide and Conquer)

## O que é

Dividir para conquistar é uma técnica de resolução de problemas baseada em três etapas:

1. Dividir o problema em subproblemas menores.
2. Resolver cada subproblema (geralmente usando recursão).
3. Combinar os resultados para obter a solução final.

---

## Estrutura Geral

```text
resolver(problema):

    se o problema for pequeno:
        resolver diretamente

    dividir em partes menores

    resolver cada parte

    combinar os resultados
```

---

## Caso Base

Toda implementação recursiva precisa de um caso base.

É a condição que interrompe as chamadas recursivas.

Exemplo:

```python
if len(lista) <= 1:
    return lista
```

---

## Etapa 1 — Dividir

O problema original é quebrado em partes menores.

Exemplo:

```text
[8 3 6 2 7 1]

↓

[8 3 6]
[2 7 1]
```

---

## Etapa 2 — Conquistar

Cada parte é resolvida da mesma maneira.

Como os subproblemas têm a mesma estrutura do problema original, a recursão é utilizada naturalmente.

---

## Etapa 3 — Combinar

Após resolver todas as partes, seus resultados são unidos.

Dependendo do algoritmo, essa combinação pode ser simples ou exigir processamento.

---

# Exemplos clássicos

## Merge Sort

Divide o vetor pela metade.

Ordena cada metade.

Une as duas partes ordenadas.

Complexidade:

```
O(n log n)
```

---

## Quick Sort

Escolhe um pivô.

Divide os elementos em:

- menores
- iguais
- maiores

Ordena recursivamente.

Complexidade média:

```
O(n log n)
```

Pior caso:

```
O(n²)
```

---

## Busca Binária

Divide repetidamente o espaço de busca pela metade.

Complexidade:

```
O(log n)
```

---

# Vantagens

- reduz problemas grandes
- código organizado
- aproveita recursão
- algoritmos muito rápidos

---

# Desvantagens

- maior uso de memória em alguns algoritmos
- pode ser difícil combinar os resultados
- depende bastante de recursão

---

# Relação com Recursão

Nem toda recursão usa dividir para conquistar.

Mas praticamente todo algoritmo de dividir para conquistar utiliza recursão.

---

# Complexidade

Normalmente produz algoritmos entre:

```
O(log n)

O(n log n)
```

dependendo da etapa de combinação.

---

# Quando utilizar

- ordenar dados
- pesquisar em dados ordenados
- resolver problemas que podem ser quebrados em partes independentes
- processamento paralelo