# Views e Índices

## O que são Views?

Views são tabelas virtuais criadas a partir de uma consulta (`SELECT`). Elas não armazenam os dados (na maioria dos bancos de dados), apenas a consulta que será executada sempre que a View for acessada.

As Views são utilizadas para simplificar consultas complexas, reutilizar código SQL, aumentar a segurança ao ocultar colunas sensíveis e padronizar consultas utilizadas com frequência.

### Principais comandos

Criar uma View:

```sql
CREATE VIEW pedidos_clientes AS
SELECT clientes.nome, pedidos.produto, pedidos.valor
FROM clientes
JOIN pedidos
ON clientes.id = pedidos.cliente_id;
```

Consultar:

```sql
SELECT * FROM pedidos_clientes;
```

Remover:

```sql
DROP VIEW pedidos_clientes;
```

---

## O que são Índices?

Índices são estruturas utilizadas pelo banco de dados para acelerar consultas. Funcionam de forma semelhante ao índice de um livro, permitindo localizar informações rapidamente sem percorrer toda a tabela.

Os índices são especialmente úteis em colunas utilizadas com frequência em cláusulas `WHERE`, `JOIN`, `ORDER BY` e `GROUP BY`.

### Principais comandos

Criar um índice:

```sql
CREATE INDEX idx_nome
ON clientes(nome);
```

Criar um índice composto:

```sql
CREATE INDEX idx_cliente_produto
ON pedidos(cliente_id, produto);
```

Criar um índice único:

```sql
CREATE UNIQUE INDEX idx_cpf
ON clientes(cpf);
```

Remover um índice:

```sql
DROP INDEX idx_nome;
```

---

## Boas práticas

- Utilize Views para simplificar consultas repetitivas.
- Utilize Índices apenas em colunas frequentemente consultadas.
- Evite criar índices desnecessários, pois eles aumentam o custo de operações de escrita (`INSERT`, `UPDATE` e `DELETE`).
- Lembre-se de que `PRIMARY KEY` e `UNIQUE` normalmente criam índices automaticamente.

## Conclusão

Views melhoram a organização e a reutilização de consultas, enquanto Índices melhoram o desempenho das buscas no banco de dados. Saber utilizar ambos corretamente é fundamental para desenvolver aplicações mais organizadas e eficientes.