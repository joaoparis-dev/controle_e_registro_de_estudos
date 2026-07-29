# Grafos e Filas

## Filas (Queue)

Uma fila é uma estrutura de dados que segue o princípio **FIFO (First In, First Out)**, ou seja, o primeiro elemento que entra é o primeiro a sair.

### Operações principais

* `enqueue()` → adiciona um elemento no final da fila.
* `dequeue()` → remove o elemento do início.
* `peek()` → consulta o primeiro elemento sem removê-lo.
* `isEmpty()` → verifica se a fila está vazia.

### Complexidade

| Operação | Complexidade |
| -------- | ------------ |
| Enqueue  | O(1)         |
| Dequeue  | O(1)         |
| Peek     | O(1)         |

### Aplicações

* Impressoras
* Atendimento por ordem de chegada
* Escalonamento de processos
* Busca em largura (BFS)
* Sistemas de mensagens

---

# Grafos

Um **grafo** é uma estrutura formada por **vértices (nós)** e **arestas (ligações)**.

Exemplo:

```
A ---- B
|      |
|      |
C ---- D
```

## Componentes

* Vértices
* Arestas

## Tipos de grafos

### Grafo não direcionado

As conexões funcionam nos dois sentidos.

```
A ----- B
```

### Grafo direcionado

As conexões possuem direção.

```
A ----> B
```

### Grafo ponderado

Cada aresta possui um peso.

```
A --5--> B
```

## Representações

### Lista de adjacência

Mais eficiente para grafos esparsos.

```python
grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}
```

### Matriz de adjacência

Uma matriz informa se existe ligação entre dois vértices.

## Percursos

### BFS (Busca em Largura)

* Utiliza **fila**
* Explora os vizinhos antes de aprofundar

Muito utilizada para encontrar o menor caminho em grafos sem peso.

### DFS (Busca em Profundidade)

* Utiliza pilha (ou recursão)
* Explora um caminho até o fim antes de voltar

Muito usada para exploração, detecção de ciclos e ordenação topológica.

## Complexidade

Usando lista de adjacência:

* BFS → O(V + E)
* DFS → O(V + E)

Onde:

* V = número de vértices
* E = número de arestas

## Onde grafos aparecem

* Google Maps
* Redes sociais
* Internet
* Jogos
* Sistemas de recomendação
* GPS
* Redes de computadores
* Dependências entre tarefas

## O que aprendi

* Como funciona uma fila utilizando o modelo FIFO.
* As operações fundamentais de uma fila.
* O conceito de grafos, vértices e arestas.
* Diferença entre grafos direcionados e não direcionados.
* O que são grafos ponderados.
* Como representar grafos por lista e matriz de adjacência.
* A diferença entre BFS e DFS.
* Como filas são utilizadas na busca em largura.
