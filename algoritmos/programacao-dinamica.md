# Programação Dinâmica (Dynamic Programming)

## O que é?

Programação Dinâmica (DP) é uma técnica utilizada para resolver problemas que possuem:

- **Subproblemas sobrepostos**
- **Subestrutura ótima**

A ideia é evitar recalcular o mesmo problema várias vezes, armazenando resultados já obtidos.

---

## Quando usar?

Geralmente um problema pode ser resolvido com DP quando possui duas características:

### 1. Subproblemas sobrepostos

O mesmo cálculo acontece diversas vezes.

Exemplo:

```
fib(5)
├── fib(4)
│   ├── fib(3)
│   └── fib(2)
└── fib(3)
```

Observe que `fib(3)` é calculado duas vezes.

---

### 2. Subestrutura ótima

A solução do problema pode ser construída usando as soluções dos problemas menores.

---

# Memoization (Top-Down)

Consiste em resolver o problema recursivamente e guardar os resultados.

Exemplo:

```python
memo = {}

def fib(n):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
```

Complexidade:

- Tempo: O(n)
- Espaço: O(n)

---

# Tabulation (Bottom-Up)

Em vez de usar recursão, começamos pelos menores casos e construímos a resposta.

```python
def fib(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]
```

Também possui:

- Tempo: O(n)
- Espaço: O(n)

---

# Otimização de espaço

Nem sempre precisamos guardar toda a tabela.

```python
def fib(n):
    if n <= 1:
        return n

    a = 0
    b = 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b
```

Agora:

- Tempo: O(n)
- Espaço: O(1)

---

# Como identificar DP

Se durante a resolução você percebe:

- "Estou resolvendo o mesmo problema várias vezes."
- "Posso guardar resultados."

provavelmente é Programação Dinâmica.

---

# Problemas clássicos

- Fibonacci
- Mochila (Knapsack)
- Troco mínimo (Coin Change)
- Longest Common Subsequence (LCS)
- Longest Increasing Subsequence (LIS)
- Edit Distance
- House Robber
- Climbing Stairs

---

# Memoization x Tabulation

| Memoization | Tabulation |
|-------------|------------|
| Usa recursão | Usa loops |
| Top-Down | Bottom-Up |
| Mais intuitiva | Geralmente mais rápida |
| Pode sofrer stack overflow | Não usa pilha de chamadas |

---

# Vantagens

- Evita cálculos repetidos
- Reduz exponencial para polinomial em muitos problemas
- Muito utilizada em entrevistas e competições

---

# Desvantagens

- Pode consumir bastante memória
- Nem todo problema pode ser resolvido com DP

---

# Resumo

Programação Dinâmica consiste em dividir um problema em subproblemas menores, armazenar resultados intermediários e reutilizá-los, evitando trabalho repetido. As duas abordagens principais são Memoization (Top-Down) e Tabulation (Bottom-Up).