# Tabelas Hash

## O que são

Uma tabela hash é uma estrutura de dados que armazena pares **chave → valor**, permitindo buscas, inserções e remoções muito rápidas.

Em média, todas essas operações possuem complexidade **O(1)**.

Exemplo:

```text
"João"  -> 21
"Maria" -> 35
"Carlos"-> 18
```

Ao procurar pela chave `"Maria"`, a tabela retorna rapidamente o valor `35`.

---

## Como funciona

Uma tabela hash utiliza uma **função hash**.

Essa função transforma uma chave em um índice do vetor onde o valor será armazenado.

Exemplo:

```text
hash("João") = 5
hash("Maria") = 12
hash("Carlos") = 2
```

Então os valores são armazenados nas posições correspondentes.

---

## Função Hash

Uma boa função hash deve:

* ser rápida;
* distribuir bem as chaves;
* minimizar colisões.

Quanto melhor a distribuição, melhor será o desempenho da tabela.

---

## Colisões

Uma colisão acontece quando duas chaves diferentes geram o mesmo índice.

Exemplo:

```text
hash("Ana") = 4
hash("João") = 4
```

Ambos desejam ocupar a mesma posição.

---

## Como resolver colisões

### Encadeamento (Chaining)

Cada posição da tabela guarda uma lista encadeada.

Exemplo:

```text
Índice 4

Ana
 ↓
João
 ↓
Carlos
```

É o método mais simples e muito utilizado.

---

### Endereçamento Aberto

Quando ocorre uma colisão, procura-se outra posição livre na tabela.

Algumas estratégias:

* Linear Probing
* Quadratic Probing
* Double Hashing

---

## Fator de Carga

O fator de carga mede o quanto a tabela está ocupada.

```
Fator de carga = número de elementos / tamanho da tabela
```

Quanto maior esse valor, maiores as chances de colisões.

---

## Redimensionamento (Resize)

Quando a tabela fica muito cheia:

* cria-se uma tabela maior;
* recalculam-se os índices de todos os elementos;
* os dados são reinseridos.

Esse processo é chamado de **rehashing**.

---

## Complexidade

| Operação | Complexidade média |
| -------- | ------------------ |
| Busca    | O(1)               |
| Inserção | O(1)               |
| Remoção  | O(1)               |

Pior caso (muitas colisões):

```
O(n)
```

---

## Vantagens

* Extremamente rápida.
* Ideal para buscas.
* Muito utilizada em bancos de dados, caches e dicionários.

---

## Desvantagens

* Pode desperdiçar memória.
* Sofre com colisões.
* Não mantém os elementos ordenados.

---

## Aplicações

* Dicionários (`dict` em Python)
* `HashMap` em Java
* Objetos em JavaScript
* Caches
* Índices de bancos de dados
* Sistemas de autenticação
* Contagem de frequência de elementos

---

## Resumo

As tabelas hash utilizam uma função hash para transformar uma chave em um índice de um vetor, permitindo buscas extremamente rápidas. Quando ocorrem colisões, elas podem ser resolvidas por encadeamento ou endereçamento aberto. Em média, inserções, buscas e remoções possuem complexidade **O(1)**, tornando essa estrutura uma das mais importantes da computação.
