# Introdução ao Machine Learning

## O que é Machine Learning?

Machine Learning (Aprendizado de Máquina) é uma área da Inteligência Artificial que permite que computadores aprendam padrões a partir de dados, em vez de serem programados com regras específicas para cada situação.

Em vez de dizer exatamente como resolver um problema, fornecemos exemplos para que o algoritmo descubra sozinho os padrões existentes.

Exemplo:

* Programação tradicional:

  * Regras + Dados → Resposta

* Machine Learning:

  * Dados + Respostas → Modelo
  * Modelo + Novos dados → Resposta

---

# Quando utilizar Machine Learning?

Machine Learning é útil quando:

* Existem muitos dados disponíveis.
* É difícil criar regras manualmente.
* O problema envolve padrões complexos.
* O sistema precisa melhorar com a experiência.

Exemplos:

* Detecção de spam.
* Recomendação de filmes.
* Reconhecimento facial.
* Diagnóstico médico.
* Previsão de preços.
* Tradução automática.

---

# Tipos de aprendizado

## Aprendizado supervisionado

O algoritmo aprende utilizando exemplos que já possuem a resposta correta.

Exemplo:

| Entrada          | Saída    |
| ---------------- | -------- |
| Foto de gato     | Gato     |
| Foto de cachorro | Cachorro |

Depois de aprender, o modelo consegue classificar novas imagens.

---

## Aprendizado não supervisionado

Nesse caso, não existem respostas prontas.

O algoritmo tenta descobrir grupos ou padrões naturalmente presentes nos dados.

Exemplos:

* Agrupar clientes semelhantes.
* Encontrar comunidades em redes sociais.
* Descobrir padrões de compra.

---

# K-Nearest Neighbors (KNN)

O livro utiliza o algoritmo **K-Nearest Neighbors (KNN)** como primeira introdução ao Machine Learning.

A ideia é simples:

1. Receber um novo dado.
2. Encontrar os **K vizinhos mais próximos**.
3. Observar a categoria predominante.
4. Classificar o novo dado.

Exemplo:

```
Novo filme

↓

5 vizinhos mais próximos

↓

4 gostam de ação
1 gosta de romance

↓

Classificação: Ação
```

Quanto maior a semelhança entre os exemplos, maior a chance de pertencerem à mesma categoria.

---

# Como medir distância?

Para descobrir quais pontos são mais próximos, normalmente utilizamos uma métrica de distância.

A mais conhecida é a **Distância Euclidiana**, que mede a distância em linha reta entre dois pontos.

Quanto menor a distância, maior a semelhança entre os dados.

---

# Escolhendo o valor de K

O valor de **K** representa quantos vizinhos serão considerados.

### K muito pequeno

* Pode sofrer influência de ruídos.
* Gera classificações instáveis.

### K muito grande

* Pode considerar exemplos pouco relacionados.
* A precisão pode diminuir.

O valor ideal depende do problema e geralmente é encontrado por meio de testes.

---

# Extração de características (Features)

O computador não entende diretamente textos, imagens ou sons.

Cada objeto precisa ser transformado em números chamados **features**.

Exemplos:

Para recomendar filmes:

* Duração.
* Gênero.
* Ano.
* Nota média.
* Número de avaliações.

Para reconhecer frutas:

* Cor.
* Peso.
* Tamanho.
* Formato.

A qualidade dessas características influencia diretamente o desempenho do modelo.

---

# Treinamento e previsão

O processo de Machine Learning geralmente segue estas etapas:

1. Coletar dados.
2. Preparar os dados.
3. Treinar o modelo.
4. Avaliar os resultados.
5. Fazer previsões em novos dados.

O treinamento utiliza exemplos conhecidos para que o algoritmo aprenda padrões.

Depois disso, o modelo pode fazer previsões sobre dados nunca vistos anteriormente.

---

# Limitações

Machine Learning não é uma solução para todos os problemas.

Algumas limitações incluem:

* Necessidade de grandes quantidades de dados.
* Dados de baixa qualidade geram modelos ruins.
* Possibilidade de vieses.
* Alto custo computacional em alguns casos.
* Nem sempre o modelo explica claramente suas decisões.

---

# Conceitos importantes

* **Dataset:** conjunto de dados utilizado no treinamento.
* **Features:** características utilizadas pelo algoritmo.
* **Modelo:** resultado do treinamento.
* **Treinamento:** processo de aprendizado.
* **Predição:** resposta produzida pelo modelo.
* **Classificação:** prever categorias.
* **Regressão:** prever valores numéricos.

---

# Resumo

O capítulo apresenta uma visão geral do Machine Learning, mostrando como computadores podem aprender padrões a partir de dados em vez de seguir regras fixas.

O principal algoritmo apresentado é o **K-Nearest Neighbors (KNN)**, que classifica novos exemplos analisando seus vizinhos mais próximos.

Também são introduzidos conceitos essenciais como aprendizado supervisionado, aprendizado não supervisionado, features, treinamento, previsão e as limitações dos modelos de aprendizado de máquina.

Este capítulo encerra o livro mostrando uma das aplicações mais modernas dos algoritmos estudados e serve como ponto de partida para estudos mais avançados em Inteligência Artificial e Ciência de Dados.
