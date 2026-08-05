# SELECT, JOIN, GROUP BY e HAVING

## SELECT

O comando `SELECT` é utilizado para consultar dados de uma tabela.

```sql
SELECT nome
FROM clientes;
```

Selecionando todas as colunas:

```sql
SELECT *
FROM clientes;
```

Selecionando múltiplas colunas:

```sql
SELECT nome, cidade
FROM clientes;
```

---

## WHERE

Filtra registros antes do agrupamento.

```sql
SELECT *
FROM pedidos
WHERE valor > 100;
```

---

## ORDER BY

Ordena os resultados.

```sql
SELECT *
FROM pedidos
ORDER BY valor DESC;
```

---

## LIMIT

Limita a quantidade de linhas retornadas.

```sql
SELECT *
FROM pedidos
LIMIT 5;
```

---

# JOIN

Une informações de tabelas relacionadas.

```sql
SELECT clientes.nome, pedidos.produto
FROM clientes
JOIN pedidos
ON clientes.id = pedidos.cliente_id;
```

## INNER JOIN

Retorna apenas registros que possuem correspondência em ambas as tabelas.

## LEFT JOIN

Retorna todos os registros da tabela da esquerda, mesmo que não possuam correspondência na tabela da direita.

---

# GROUP BY

Agrupa registros para utilização de funções de agregação.

```sql
SELECT cliente_id,
SUM(valor)
FROM pedidos
GROUP BY cliente_id;
```

---

# Funções de agregação

## COUNT

Conta registros.

```sql
COUNT(*)
```

## SUM

Soma valores.

```sql
SUM(valor)
```

## AVG

Calcula a média.

```sql
AVG(valor)
```

## MAX

Retorna o maior valor.

```sql
MAX(valor)
```

## MIN

Retorna o menor valor.

```sql
MIN(valor)
```

---

# HAVING

Filtra grupos após o agrupamento.

```sql
SELECT cliente_id,
SUM(valor)
FROM pedidos
GROUP BY cliente_id
HAVING SUM(valor) > 500;
```

---

# Ordem de execução

1. FROM
2. JOIN
3. WHERE
4. GROUP BY
5. HAVING
6. SELECT
7. ORDER BY
8. LIMIT

---

# Resumo

- SELECT consulta dados.
- WHERE filtra linhas.
- JOIN relaciona tabelas.
- GROUP BY agrupa registros.
- HAVING filtra grupos.
- COUNT conta registros.
- SUM soma valores.
- AVG calcula médias.
- MAX retorna o maior valor.
- MIN retorna o menor valor.