# Procedures e Transactions

## Stored Procedures

Uma **Stored Procedure** é um conjunto de comandos SQL armazenado no próprio banco de dados, podendo ser executado sempre que necessário através do comando `CALL`.

### Vantagens

- Reutilização de código.
- Melhor organização.
- Mais segurança.
- Redução do tráfego entre aplicação e banco.
- Facilidade de manutenção.

### Sintaxe

```sql
DELIMITER //

CREATE PROCEDURE listar_clientes()
BEGIN
    SELECT * FROM clientes;
END //

DELIMITER ;
```

Executando:

```sql
CALL listar_clientes();
```

---

## Parâmetros

### IN

Recebe um valor de entrada.

```sql
IN id_cliente INT
```

### OUT

Retorna um valor.

```sql
OUT total INT
```

### INOUT

Recebe e devolve um valor.

```sql
INOUT numero INT
```

---

## Variáveis

Dentro de procedures podem ser declaradas variáveis com `DECLARE`.

```sql
DECLARE total INT;
```

Também é possível armazenar resultados de consultas usando `SELECT ... INTO`.

---

## Estruturas de Controle

### IF

```sql
IF idade >= 18 THEN
    SELECT 'Maior';
ELSE
    SELECT 'Menor';
END IF;
```

### CASE

```sql
CASE
    WHEN nota >= 7 THEN
        SELECT 'Aprovado';
    ELSE
        SELECT 'Reprovado';
END CASE;
```

### Loops

- `WHILE`
- `REPEAT`
- `LOOP`

Permitem repetir comandos dentro da procedure.

---

# Transactions

Uma **Transaction** é um conjunto de operações executadas como uma única unidade.

Ou todas as operações são concluídas com sucesso ou nenhuma alteração é mantida.

## Principais comandos

### Iniciar

```sql
START TRANSACTION;
```

### Confirmar alterações

```sql
COMMIT;
```

### Cancelar alterações

```sql
ROLLBACK;
```

---

## Exemplo

```sql
START TRANSACTION;

UPDATE contas
SET saldo = saldo - 500
WHERE id = 1;

UPDATE contas
SET saldo = saldo + 500
WHERE id = 2;

COMMIT;
```

Caso ocorra algum erro:

```sql
ROLLBACK;
```

---

## ACID

Toda transação deve obedecer às propriedades ACID:

- **Atomicidade:** tudo ou nada.
- **Consistência:** mantém os dados válidos.
- **Isolamento:** transações não interferem entre si.
- **Durabilidade:** após o `COMMIT`, os dados permanecem gravados.

---

## SAVEPOINT

Permite criar um ponto intermediário para retorno durante uma transação.

```sql
START TRANSACTION;

UPDATE clientes
SET saldo = saldo - 100;

SAVEPOINT ponto1;

UPDATE clientes
SET saldo = saldo - 200;

ROLLBACK TO ponto1;

COMMIT;
```

---

## Quando utilizar Procedures

- Automatizar tarefas.
- Relatórios.
- Regras de negócio.
- Processamentos em lote.
- Validações.

## Quando utilizar Transactions

- Transferências bancárias.
- Compras online.
- Controle de estoque.
- Sistemas financeiros.
- Qualquer operação composta por várias alterações dependentes.

---

## Resumo

- Procedures armazenam lógica SQL reutilizável dentro do banco.
- Transactions garantem que várias operações sejam executadas com segurança.
- `COMMIT` confirma alterações.
- `ROLLBACK` desfaz alterações.
- ACID garante confiabilidade e integridade dos dados.