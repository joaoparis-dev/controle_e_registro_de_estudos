# Busca e Ordenação

## Busca Linear

Percorre todos os elementos até encontrar o valor.

### Complexidade

- Melhor caso: O(1)
- Caso médio: O(n)
- Pior caso: O(n)

### Vantagens

- Muito simples
- Funciona em listas não ordenadas

### Desvantagens

- Ineficiente para listas grandes

---

## Busca Binária

Divide o vetor ao meio a cada comparação.

**Pré-requisito:** o vetor deve estar ordenado.

### Complexidade

- Melhor caso: O(1)
- Média: O(log n)
- Pior: O(log n)

### Funcionamento

1. Encontra o elemento do meio.
2. Se for o procurado, termina.
3. Se o valor procurado for menor, busca na metade esquerda.
4. Se for maior, busca na metade direita.

---

# Algoritmos de Ordenação

## Bubble Sort

Compara elementos vizinhos e troca quando necessário.

Após cada passagem, o maior elemento "borbulha" para o final.

### Complexidade

- Melhor: O(n)
- Médio: O(n²)
- Pior: O(n²)

### Vantagens

- Muito simples
- Fácil de implementar

### Desvantagens

- Muito lento para grandes volumes de dados

---

## Selection Sort

Procura o menor elemento e o coloca na posição correta.

### Complexidade

- Melhor: O(n²)
- Médio: O(n²)
- Pior: O(n²)

### Características

- Poucas trocas
- Muitas comparações

---

## Insertion Sort

Mantém uma parte da lista ordenada.

Cada novo elemento é inserido na posição correta.

### Complexidade

- Melhor: O(n)
- Médio: O(n²)
- Pior: O(n²)

### Vantagens

- Muito eficiente para listas pequenas
- Excelente quando os dados já estão quase ordenados

---

# Comparação

| Algoritmo | Melhor | Médio | Pior |
|-----------|---------|--------|-------|
| Busca Linear | O(1) | O(n) | O(n) |
| Busca Binária | O(1) | O(log n) | O(log n) |
| Bubble Sort | O(n) | O(n²) | O(n²) |
| Selection Sort | O(n²) | O(n²) | O(n²) |
| Insertion Sort | O(n) | O(n²) | O(n²) |

---

# Quando usar

- Busca Linear → listas pequenas ou não ordenadas.
- Busca Binária → listas ordenadas.
- Bubble Sort → aprendizado.
- Selection Sort → quando o número de trocas deve ser reduzido.
- Insertion Sort → listas pequenas ou quase ordenadas.