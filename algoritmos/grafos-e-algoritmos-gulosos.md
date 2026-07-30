# Grafos, Busca em Largura, Algoritmo de Dijkstra e Algoritmos Gulosos

## Grafos

Um **grafo** é uma estrutura de dados formada por:

- Vértices (nós)
- Arestas (ligações entre os vértices)

Exemplo:

A → B → C

ou

A ----- B
 \     /
   \ /
    C

Grafos são usados para representar:

- Redes sociais
- GPS
- Internet
- Sistemas de recomendação
- Redes de computadores

---

## Tipos de grafos

### Grafo direcionado

As ligações possuem direção.

A → B

É possível ir de A para B, mas não necessariamente voltar.

---

### Grafo não direcionado

As conexões funcionam nos dois sentidos.

A ----- B

---

### Grafo ponderado

Cada aresta possui um custo.

A --5--> B

Esse custo pode representar:

- distância
- tempo
- dinheiro
- consumo de combustível

---

## Busca em Largura (Breadth First Search - BFS)

A Busca em Largura percorre um grafo visitando primeiro todos os vizinhos próximos antes de avançar para níveis mais distantes.

Ela utiliza uma **Fila (Queue)**.

Fluxo:

1. Coloca o nó inicial na fila.
2. Remove o primeiro da fila.
3. Visita todos os vizinhos.
4. Coloca os vizinhos na fila.
5. Repete até a fila ficar vazia.

Exemplo:

```
A
| \
B  C
|   \
D    E
```

Ordem:

```
A
B
C
D
E
```

---

## Quando usar BFS

Quando todas as arestas possuem o mesmo custo.

Exemplo:

- menor quantidade de conexões entre duas pessoas
- menor número de estações de metrô
- menor quantidade de passos

Complexidade:

```
O(V + E)
```

onde

- V = vértices
- E = arestas

---

# Algoritmo de Dijkstra

O algoritmo de Dijkstra encontra o caminho de menor custo em um grafo com pesos positivos.

Exemplo:

```
A --5--> B
A --2--> C
C --3--> B
```

Melhor caminho:

```
A → C → B

2 + 3 = 5
```

Mesmo que exista uma ligação direta, outro caminho pode possuir menor custo.

---

## Como funciona

Enquanto houver nós não processados:

1. Escolhe o nó com menor custo conhecido.
2. Atualiza os custos dos vizinhos.
3. Marca o nó como processado.
4. Repete.

Esse processo é conhecido como **relaxamento das arestas**.

---

## Dijkstra NÃO funciona quando existem pesos negativos.

Exemplo:

```
A → B = 4
B → C = -10
```

Nesses casos é necessário utilizar algoritmos específicos, como Bellman-Ford.

---

## Complexidade

Com fila de prioridade:

```
O((V + E) log V)
```

---

# Algoritmos Gulosos (Greedy)

Um algoritmo guloso sempre toma a melhor decisão naquele momento.

Ele **não analisa todas as possibilidades futuras**.

Objetivo:

Encontrar uma boa solução rapidamente.

---

## Ideia principal

A cada etapa:

Escolha a melhor opção disponível.

Nunca volte atrás.

---

## Quando funcionam

Funcionam quando o problema possui:

- Propriedade gulosa
- Subestrutura ótima

Nem todo problema atende essas propriedades.

---

## Exemplos clássicos

- Seleção de atividades
- Mochila fracionária
- Codificação de Huffman
- Algoritmo de Prim
- Algoritmo de Kruskal

---

## Vantagens

- Simples
- Muito rápidos
- Pouco consumo de memória

---

## Desvantagens

Nem sempre encontram a solução ótima.

Em alguns problemas apenas produzem uma aproximação.

---

# Comparação

| Algoritmo | Resolve |
|-----------|----------|
| BFS | Menor caminho sem pesos |
| Dijkstra | Menor caminho com pesos positivos |
| Guloso | Boa solução fazendo escolhas locais |

---

# Resumo

- Grafos representam conexões.
- BFS encontra o menor caminho quando todos os custos são iguais.
- Dijkstra encontra o menor caminho considerando pesos positivos.
- Algoritmos gulosos fazem sempre a melhor escolha local e são extremamente eficientes quando o problema possui estrutura adequada.