# Árvores

## O que são árvores?

Uma árvore é uma estrutura de dados hierárquica formada por nós conectados por arestas.

Diferente de um grafo comum, uma árvore:

- Não possui ciclos.
- Todos os nós estão conectados.
- Existe apenas um caminho entre dois nós.

Exemplo:

        A
      / | \
     B  C  D
    / \     \
   E   F     G

A é a raiz da árvore.

---

# Componentes de uma árvore

## Raiz (Root)

É o primeiro nó da árvore.

```
A
```

---

## Nó (Node)

Cada elemento da árvore.

```
A B C D E...
```

---

## Aresta (Edge)

Ligação entre dois nós.

```
A ---- B
```

---

## Pai (Parent)

Nó acima.

```
A
|
B

A é pai de B.
```

---

## Filho (Child)

Nó abaixo.

```
A
|
B

B é filho de A.
```

---

## Folha (Leaf)

Nó sem filhos.

```
    A
   / \
  B   C

B e C são folhas.
```

---

## Altura

Maior distância da raiz até uma folha.

```
A
|
B
|
C

Altura = 2
```

---

## Profundidade

Quantidade de arestas da raiz até determinado nó.

```
A
|
B
|
C

Profundidade de C = 2
```

---

# Tipos de árvores

## Árvore Genérica

Cada nó pode possuir qualquer quantidade de filhos.

```
      A
   / / \ \
  B C  D E
```

---

## Árvore Binária

Cada nó possui no máximo dois filhos.

```
      A
     / \
    B   C
```

Filho esquerdo e filho direito.

---

## Árvore Binária Completa

Todos os níveis são preenchidos, exceto talvez o último.

```
      A
     / \
    B   C
   / \  /
  D  E F
```

---

## Árvore Binária Cheia

Todo nó possui exatamente dois filhos ou nenhum.

```
      A
     / \
    B   C
   /\   /\
  D E  F G
```

---

## Árvore Binária Balanceada

A diferença de altura entre os lados esquerdo e direito é pequena.

Isso mantém operações rápidas.

---

# Percursos (Tree Traversal)

## Pré-Ordem (Preorder)

Raiz → Esquerda → Direita

```
A
/ \
B C

Resultado:
A B C
```

---

## Em Ordem (Inorder)

Esquerda → Raiz → Direita

```
A
/ \
B C

Resultado:
B A C
```

Em Árvores Binárias de Busca gera os valores ordenados.

---

## Pós-Ordem (Postorder)

Esquerda → Direita → Raiz

```
A
/ \
B C

Resultado:
B C A
```

---

## Percurso por Nível (Level Order)

Visita por camadas utilizando fila.

```
A
/ \
B C
/ \
D E

Resultado:

A
B C
D E
```

---

# Árvores Binárias de Busca (BST)

Possuem uma regra importante:

Valores menores ficam à esquerda.

Valores maiores ficam à direita.

Exemplo:

```
        8
      /   \
     3     10
    / \      \
   1   6      14
      / \     /
     4   7   13
```

Buscar um número é muito mais rápido do que em uma lista comum.

---

# Complexidade

BST balanceada:

Busca
O(log n)

Inserção
O(log n)

Remoção
O(log n)

BST desbalanceada:

Busca
O(n)

---

# Aplicações

- Sistemas de arquivos
- DOM do HTML
- Banco de dados
- Compiladores
- Árvores de decisão
- Inteligência Artificial
- Índices de banco de dados

---

# Resumo

✓ Estrutura hierárquica.

✓ Possui raiz.

✓ Não possui ciclos.

✓ Nós ligados por arestas.

✓ Muito usada para buscas eficientes.

✓ BST organiza os dados em ordem.

✓ Percursos principais:

- Pré-ordem
- Em ordem
- Pós-ordem
- Por nível