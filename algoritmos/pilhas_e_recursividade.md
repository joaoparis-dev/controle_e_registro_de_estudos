# Pilhas e Recursividade

## O que é uma pilha (Stack)

Uma pilha é uma estrutura de dados que segue o princípio **LIFO (Last In, First Out)**, ou seja:

> O último elemento que entra é o primeiro que sai.

Exemplo:

```
Empilha: A
Empilha: B
Empilha: C

Pilha:

C ← topo
B
A

Desempilhar()

B ← topo
A
```

---

## Principais operações

### Push

Adiciona um elemento no topo.

```python
pilha.append(10)
```

---

### Pop

Remove e retorna o elemento do topo.

```python
valor = pilha.pop()
```

---

### Peek (Topo)

Consulta o elemento do topo sem removê-lo.

```python
pilha[-1]
```

---

### Verificar se está vazia

```python
len(pilha) == 0
```

---

## Complexidade

| Operação | Complexidade |
|----------|--------------|
| Push | O(1) |
| Pop | O(1) |
| Peek | O(1) |

---

## Onde pilhas são utilizadas

- Desfazer (Ctrl + Z)
- Histórico do navegador
- Navegação entre telas
- Avaliação de expressões matemáticas
- Compiladores
- Chamadas de funções

---

# Recursividade

Recursividade é quando uma função chama ela mesma para resolver um problema menor.

Estrutura básica:

```python
def func():
    if caso_base:
        return

    func()
```

Toda função recursiva possui:

- Caso base
- Caso recursivo

Sem caso base ocorre recursão infinita.

---

## Exemplo

```python
def contagem(n):
    if n == 0:
        return

    print(n)
    contagem(n - 1)

contagem(5)
```

Saída:

```
5
4
3
2
1
```

---

## Fatorial

```python
def fatorial(n):
    if n == 1:
        return 1

    return n * fatorial(n - 1)
```

Chamando:

```
fatorial(4)

4 × fatorial(3)

3 × fatorial(2)

2 × fatorial(1)

1
```

Resultado:

```
24
```

---

# A pilha de chamadas (Call Stack)

Sempre que uma função é chamada, ela é colocada na pilha de chamadas.

Exemplo:

```python
def a():
    b()

def b():
    c()

def c():
    print("fim")
```

A pilha fica:

```
c()
b()
a()
main()
```

Quando `c()` termina:

```
b()
a()
main()
```

Depois:

```
a()
main()
```

Depois:

```
main()
```

É exatamente por isso que a recursividade utiliza pilhas.

---

# Vantagens da recursividade

- Código menor
- Elegante
- Resolve problemas naturalmente recursivos
- Muito usada em árvores e grafos

---

# Desvantagens

- Consome memória da pilha
- Pode ser mais lenta
- Pode causar Stack Overflow
- Nem sempre é a solução mais eficiente

---

# Quando utilizar

Recursão é excelente para:

- Árvores
- Grafos
- Backtracking
- Divide and Conquer
- DFS
- Merge Sort
- Quick Sort

Para tarefas simples (percorrer listas, contar elementos etc.), normalmente um laço é mais eficiente.

---

# Resumo

- Pilhas seguem o princípio LIFO.
- Push adiciona no topo.
- Pop remove do topo.
- A recursividade acontece quando uma função chama ela mesma.
- Toda recursão precisa de um caso base.
- Cada chamada recursiva é armazenada na Call Stack.
- Muitas estruturas e algoritmos utilizam pilhas e recursão internamente.