# 📚 Diário de Estudos — 06/09/2026

## 🧠 Conteúdo estudado

Hoje estudei **programação assíncrona em Python**, com foco nos conceitos de `async` e `await` e na sua utilização em aplicações backend, especialmente com **FastAPI**.

---

## 🔹 Async/Await

Aprendi que `async` e `await` são recursos utilizados para implementar **programação assíncrona** em Python.

A programação assíncrona permite que uma aplicação aproveite melhor o tempo durante operações de espera, principalmente em tarefas de **I/O**, como:

* Requisições HTTP;
* Consultas ao banco de dados;
* Comunicação com APIs externas;
* Operações de rede;
* Leitura e escrita de arquivos.

A ideia principal é que, enquanto uma tarefa está esperando uma operação terminar, outras tarefas podem ser executadas.

---

## 🔹 `async def`

Aprendi que uma função pode ser declarada como assíncrona utilizando:

```python
async def minha_funcao():
    ...
```

Uma função criada com `async def` é uma **coroutine function** e, quando chamada, produz uma coroutine que pode ser aguardada com `await`.

---

## 🔹 `await`

O `await` é utilizado para aguardar uma operação assíncrona:

```python
async def main():
    resultado = await alguma_funcao()
```

Durante uma espera assíncrona, o controle pode ser devolvido ao **event loop**, permitindo que outras tarefas sejam executadas.

---

## 🔹 Event Loop

Estudei o conceito de **event loop**, que é responsável por coordenar a execução das tarefas assíncronas.

De forma simplificada:

```text
              EVENT LOOP
                  │
        ┌─────────┼─────────┐
        ↓         ↓         ↓
     Tarefa A  Tarefa B  Tarefa C
        │         │         │
      await     executa    await
        │         │         │
        └─────────┴─────────┘
                  │
              continua
```

O event loop verifica quais tarefas podem continuar executando e coordena suas pausas e retomadas.

---

## 🔹 `asyncio`

Conheci o módulo `asyncio`, utilizado para trabalhar com programação assíncrona em Python.

Exemplo:

```python
import asyncio


async def tarefa():
    print("Começou")

    await asyncio.sleep(3)

    print("Terminou")


asyncio.run(tarefa())
```

Também aprendi a diferença entre:

```python
time.sleep(3)
```

e:

```python
await asyncio.sleep(3)
```

O `time.sleep()` é bloqueante, enquanto `asyncio.sleep()` permite que o event loop execute outras tarefas durante a espera.

---

## 🔹 Concorrência

Estudei como executar tarefas de maneira concorrente utilizando `asyncio.gather()`:

```python
await asyncio.gather(
    tarefa_a(),
    tarefa_b()
)
```

Isso permite que operações independentes sejam realizadas de maneira concorrente.

Exemplo:

```text
Tarefa A ─────────────┐
                      ├── resultado
Tarefa B ─────────────┘
```

Também aprendi que **concorrência não é a mesma coisa que paralelismo**.

* **Concorrência:** tarefas progridem de forma intercalada.
* **Paralelismo:** tarefas são realmente executadas simultaneamente em diferentes recursos de processamento.

---

## 🔹 I/O-bound vs CPU-bound

Um dos conceitos mais importantes estudados foi a diferença entre:

### I/O-bound

Tarefas que passam grande parte do tempo esperando:

* Banco de dados;
* APIs;
* Rede;
* Arquivos;
* Sockets.

Esse é um cenário onde `async/await` pode trazer grandes benefícios.

### CPU-bound

Tarefas que exigem muito processamento da CPU.

Nesse caso, `async/await` sozinho não resolve o problema. Dependendo da situação, podem ser necessários processos separados, workers, multiprocessing ou otimizações de algoritmo.

---

## 🔹 `asyncio.gather()`

Aprendi que `asyncio.gather()` pode ser utilizado quando existem várias operações independentes:

```python
usuario, produtos = await asyncio.gather(
    buscar_usuario(),
    buscar_produtos()
)
```

Isso é útil quando não existe dependência entre as operações.

Por exemplo:

```text
buscar usuário ───────┐
                      ├── resultados
buscar produtos ──────┘
```

Por outro lado, quando uma operação depende do resultado de outra, elas devem continuar sendo executadas sequencialmente.

---

## 🔹 `asyncio.create_task()`

Também conheci:

```python
asyncio.create_task()
```

que permite agendar uma coroutine para execução concorrente.

Exemplo:

```python
task = asyncio.create_task(
    buscar_usuario()
)

usuario = await task
```

---

# 🚀 Async/Await no FastAPI

A parte mais importante para meu aprendizado de backend foi entender como `async/await` se relaciona com o **FastAPI**.

Um endpoint pode ser declarado assim:

```python
@app.get("/users")
async def get_users():
    return {"users": []}
```

O FastAPI possui suporte nativo a código assíncrono.

Isso é especialmente importante quando a API precisa realizar operações de I/O, como consultar bancos de dados ou acessar APIs externas.

---

## 🔹 Operações bloqueantes

Aprendi que não basta simplesmente colocar `async` em uma função.

Por exemplo:

```python
@app.get("/teste")
async def teste():
    time.sleep(5)

    return {"ok": True}
```

Apesar de o endpoint ser `async`, `time.sleep()` é uma operação bloqueante.

Uma alternativa assíncrona seria:

```python
@app.get("/teste")
async def teste():
    await asyncio.sleep(5)

    return {"ok": True}
```

Também aprendi que as bibliotecas utilizadas precisam oferecer suporte assíncrono quando quero manter uma cadeia de execução realmente assíncrona.

---

# 🗄️ Async e SQLAlchemy

Como estou trabalhando com **FastAPI, PostgreSQL e SQLAlchemy**, também estudei a aplicação de programação assíncrona no acesso ao banco.

Conheci conceitos como:

```python
AsyncSession
```

e operações como:

```python
result = await session.execute(...)
```

Uma arquitetura possível é:

```text
Router
   ↓
Service
   ↓
Repository
   ↓
AsyncSession
   ↓
PostgreSQL
```

A ideia é que as operações assíncronas sejam propagadas pela cadeia quando necessário.

---

# 🏗️ Aplicação na arquitetura da API

Um exemplo conceitual:

```python
@router.get("/users")
async def get_users(service):
    return await service.get_users()
```

Service:

```python
class UserService:

    async def get_users(self):
        return await self.repository.get_users()
```

Repository:

```python
class UserRepository:

    async def get_users(self):
        result = await self.session.execute(
            select(User)
        )

        return result.scalars().all()
```

Assim, a execução pode seguir:

```text
Router
  │
  │ await
  ↓
Service
  │
  │ await
  ↓
Repository
  │
  │ await
  ↓
Database
```

---

# 🎯 Principais aprendizados

Hoje aprendi:

* O que é programação assíncrona;
* O funcionamento de `async def`;
* O funcionamento de `await`;
* O conceito de coroutine;
* O papel do event loop;
* O uso do módulo `asyncio`;
* A diferença entre código síncrono e assíncrono;
* A diferença entre `time.sleep()` e `asyncio.sleep()`;
* O conceito de concorrência;
* A diferença entre concorrência e paralelismo;
* A diferença entre tarefas I/O-bound e CPU-bound;
* O uso de `asyncio.gather()`;
* O uso de `asyncio.create_task()`;
* Como `async/await` funciona no FastAPI;
* A importância de evitar operações bloqueantes em endpoints assíncronos;
* A relação entre `async/await`, FastAPI e SQLAlchemy;
* A importância de utilizar bibliotecas compatíveis com programação assíncrona.

---

# 📌 Resumo

O principal conceito aprendido hoje foi:

```text
async def
    ↓
cria uma função assíncrona

await
    ↓
aguarda uma operação assíncrona

event loop
    ↓
coordena as tarefas

I/O-bound
    ↓
principal cenário onde async é útil

FastAPI
    ↓
possui suporte nativo a async/await
```

O aprendizado de `async/await` é importante para continuar evoluindo no desenvolvimento de APIs com **FastAPI**, principalmente quando começar a trabalhar com acesso assíncrono ao banco de dados, chamadas para APIs externas e aplicações com múltiplas requisições simultâneas.

---

## 📈 Próximos estudos

Como próximo passo, aprofundar:

1. `AsyncSession` do SQLAlchemy;
2. Banco de dados assíncrono com FastAPI;
3. `async`/`await` em repositories e services;
4. Tratamento de erros em código assíncrono;
5. Tasks e background tasks;
6. Testes de endpoints assíncronos com `pytest`.
