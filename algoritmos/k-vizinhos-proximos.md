# K-Nearest Neighbors (KNN)

## O que é

O K-Nearest Neighbors (KNN) é um algoritmo de aprendizado supervisionado utilizado para:

- Classificação
- Regressão

Seu funcionamento é extremamente simples:

> Um novo dado recebe a classificação dos exemplos mais próximos dele.

Por isso ele é conhecido como algoritmo baseado em instâncias (Lazy Learning), pois não cria um modelo durante o treinamento.

---

# Como funciona

1. Escolha um valor para K.
2. Calcule a distância entre o novo ponto e todos os exemplos do conjunto de treinamento.
3. Encontre os K vizinhos mais próximos.
4. Faça a votação (classificação) ou a média (regressão).

---

# Exemplo

Imagine os seguintes dados:

Frutas:

Maçã:
- Vermelha
- Peso 150g

Laranja:
- Laranja
- Peso 170g

Nova fruta:

- Vermelha
- Peso 160g

Se K = 3:

Os três vizinhos mais próximos podem ser:

- Maçã
- Maçã
- Laranja

Resultado:

A fruta será classificada como Maçã.

---

# O que significa o K

O K representa quantos vizinhos serão considerados.

Exemplo:

K = 1

Apenas o vizinho mais próximo decide.

K = 5

Os cinco vizinhos votam.

---

# Escolha do valor de K

K pequeno:

Vantagens:
- Mais sensível aos dados
- Captura detalhes

Desvantagens:
- Muito sensível a ruídos

K grande:

Vantagens:
- Mais estável
- Menos afetado por ruídos

Desvantagens:
- Pode generalizar demais.

---

# Distâncias

As mais utilizadas são:

## Distância Euclidiana

É a distância em linha reta entre dois pontos.

É a mais utilizada.

---

## Distância Manhattan

Soma das diferenças absolutas entre as coordenadas.

Muito usada quando o movimento ocorre em grades.

---

## Distância Minkowski

Generaliza Euclidiana e Manhattan.

---

# KNN para classificação

Cada vizinho vota.

A classe com maior quantidade de votos vence.

---

# KNN para regressão

Em vez de votar, calcula-se a média dos valores dos vizinhos.

---

# Vantagens

- Fácil de entender
- Fácil de implementar
- Não exige treinamento complexo
- Funciona bem em bases pequenas

---

# Desvantagens

- Lento em bases grandes
- Consome bastante memória
- Sensível à escala dos dados
- Sensível à escolha do K

---

# Normalização

Como o algoritmo utiliza distância, é importante normalizar os dados.

Exemplo:

Idade:
20–60

Salário:
1000–100000

Sem normalização, o salário domina o cálculo da distância.

---

# Complexidade

Treinamento:

O(1)

Predição:

O(n)

onde n é o número de exemplos.

---

# Aplicações

- Reconhecimento de padrões
- Recomendação
- Diagnóstico médico
- Detecção de fraudes
- Classificação de imagens
- Sistemas de recomendação

---

# Resumo

- É um algoritmo supervisionado.
- Usa os vizinhos mais próximos.
- O parâmetro K define quantos vizinhos serão consultados.
- Pode ser usado para classificação e regressão.
- Utiliza medidas de distância.
- Funciona melhor com dados normalizados.