# APIs REST

## O que é uma API?

API significa **Application Programming Interface**. É uma interface que permite que diferentes sistemas se comuniquem.

Uma API pode ser implementada utilizando diferentes estilos e tecnologias, como REST, GraphQL, SOAP e gRPC.

## O que é REST?

REST significa **Representational State Transfer**.

É um **estilo arquitetural** para construção de APIs, normalmente utilizando HTTP para comunicação entre cliente e servidor.

Os principais conceitos são:

* Recursos
* URLs
* Métodos HTTP
* Status codes
* HTTP Headers
* Request e Response
* JSON
* Stateless
* Cache
* Interface uniforme

---

## Recursos

REST trabalha com **recursos**.

Exemplos:

```text
/users
/products
/orders
/posts
```

Um recurso específico pode ser identificado:

```text
/users/10
/products/25
/orders/100
```

A URL representa o recurso e o método HTTP representa a operação.

---

## Métodos HTTP

### GET

Utilizado para buscar recursos.

```http
GET /users
GET /users/10
```

### POST

Utilizado normalmente para criar recursos.

```http
POST /users
```

### PUT

Utilizado normalmente para substituir completamente um recurso.

```http
PUT /users/10
```

### PATCH

Utilizado para realizar alterações parciais.

```http
PATCH /users/10
```

### DELETE

Utilizado para remover recursos.

```http
DELETE /users/10
```

---

## CRUD

CRUD representa as quatro operações básicas sobre dados:

| CRUD   | HTTP      |
| ------ | --------- |
| Create | POST      |
| Read   | GET       |
| Update | PUT/PATCH |
| Delete | DELETE    |

Exemplo:

```http
POST   /users
GET    /users
GET    /users/10
PUT    /users/10
PATCH  /users/10
DELETE /users/10
```

---

## Request

Uma requisição HTTP pode possuir:

* Método
* URL
* Headers
* Body

Exemplo:

```http
POST /users HTTP/1.1
Content-Type: application/json

{
    "nome": "João",
    "email": "joao@email.com"
}
```

---

## Response

Uma resposta HTTP normalmente possui:

* Status code
* Headers
* Body

Exemplo:

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
    "id": 1,
    "nome": "João",
    "email": "joao@email.com"
}
```

---

## Path Parameters

São parâmetros presentes no caminho da URL.

```http
GET /users/10
```

Nesse caso:

```text
10
```

é o `user_id`.

No FastAPI:

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id}
```

---

## Query Parameters

São parâmetros enviados depois de `?`.

```http
GET /users?idade=20
```

Também podem existir vários:

```http
GET /users?idade=20&cidade=sp
```

São muito utilizados para:

* filtros
* buscas
* paginação
* ordenação

Exemplos:

```http
GET /products?category=games
GET /products?min_price=100&max_price=500
GET /users?page=1&limit=20
```

---

## JSON

JSON é um dos formatos mais utilizados para troca de dados em APIs REST.

Exemplo:

```json
{
    "id": 1,
    "nome": "João",
    "idade": 20,
    "ativo": true
}
```

Pode representar:

* strings
* números
* booleanos
* null
* arrays
* objetos

---

## Headers

Headers carregam informações adicionais sobre a requisição ou resposta.

Alguns importantes:

```http
Content-Type: application/json
Accept: application/json
Authorization: Bearer TOKEN
```

### Content-Type

Indica o formato dos dados enviados.

```http
Content-Type: application/json
```

### Accept

Indica o formato que o cliente aceita receber.

```http
Accept: application/json
```

### Authorization

Utilizado para enviar informações de autenticação.

```http
Authorization: Bearer TOKEN
```

---

# Status Codes

Os status codes são divididos em categorias:

```text
1xx → informação
2xx → sucesso
3xx → redirecionamento
4xx → erro do cliente
5xx → erro do servidor
```

## Principais 2xx

### 200 OK

Requisição realizada com sucesso.

### 201 Created

Recurso criado com sucesso.

Muito utilizado após:

```http
POST /users
```

### 202 Accepted

Requisição aceita para processamento.

### 204 No Content

Operação realizada com sucesso, mas sem conteúdo para retornar.

Muito comum em:

```http
DELETE /users/10
```

---

## Principais 4xx

### 400 Bad Request

A requisição é inválida.

### 401 Unauthorized

O cliente não possui autenticação válida.

```text
Quem é você?
```

### 403 Forbidden

O cliente está autenticado, mas não possui permissão.

```text
Sei quem você é, mas você não pode fazer isso.
```

### 404 Not Found

Recurso não encontrado.

### 405 Method Not Allowed

O método HTTP não é permitido naquele endpoint.

### 409 Conflict

Existe um conflito com o estado atual do recurso.

### 422 Unprocessable Content

Os dados enviados não passaram pela validação.

FastAPI utiliza bastante esse status para erros de validação.

---

## Principais 5xx

### 500 Internal Server Error

Erro inesperado no servidor.

### 502 Bad Gateway

Um servidor intermediário recebeu uma resposta inválida de outro servidor.

### 503 Service Unavailable

O serviço está temporariamente indisponível.

---

# Stateless

REST possui o princípio de ser **stateless**.

Isso significa que cada requisição deve carregar as informações necessárias para o servidor processá-la.

Exemplo:

```http
GET /profile
Authorization: Bearer TOKEN
```

Outra requisição:

```http
GET /orders
Authorization: Bearer TOKEN
```

Cada requisição contém sua autenticação.

---

# Autenticação e Autorização

## Autenticação

Responde:

```text
Quem é você?
```

Exemplos:

* API Key
* Basic Auth
* Cookies
* JWT
* OAuth 2.0

## Autorização

Responde:

```text
O que você pode fazer?
```

Exemplo:

```text
Usuário autenticado
        ↓
Não é administrador
        ↓
DELETE /users/10
        ↓
403 Forbidden
```

---

# JWT

JWT significa **JSON Web Token**.

Um JWT possui normalmente:

```text
header.payload.signature
```

Pode carregar informações como:

```json
{
    "sub": "123",
    "role": "admin",
    "exp": 1780000000
}
```

É importante lembrar que JWT não significa que o payload esteja criptografado.

Não devemos colocar informações secretas no payload.

Um uso comum é:

```http
Authorization: Bearer TOKEN
```

---

# HTTPS

APIs em produção devem utilizar HTTPS.

HTTPS protege os dados durante a comunicação entre cliente e servidor.

Especialmente importante para:

* senhas
* tokens
* dados pessoais
* informações financeiras

---

# CORS

CORS significa **Cross-Origin Resource Sharing**.

É uma política relacionada ao navegador que controla requisições entre diferentes origens.

Exemplo:

```text
Frontend
http://localhost:3000

API
http://localhost:8000
```

Como são origens diferentes, o navegador pode aplicar regras de CORS.

---

# Idempotência

Uma operação idempotente pode ser repetida sem alterar o resultado final depois da primeira execução.

Geralmente:

| Método | Idempotente         |
| ------ | ------------------- |
| GET    | Sim                 |
| PUT    | Sim                 |
| DELETE | Sim                 |
| POST   | Não necessariamente |
| PATCH  | Depende             |

Isso é especialmente importante em operações como pagamentos.

Uma API pode utilizar:

```http
Idempotency-Key: abc123
```

para evitar operações duplicadas.

---

# Paginação

Quando existem muitos registros, não devemos retornar tudo de uma vez.

Exemplo:

```http
GET /users?page=1&limit=20
```

Ou:

```http
GET /users?offset=0&limit=20
```

Uma resposta pode ser:

```json
{
    "items": [],
    "page": 1,
    "limit": 20,
    "total": 5000
}
```

---

# Versionamento

Uma API pode possuir versões:

```text
/api/v1/users
/api/v2/users
```

Isso permite evoluir a API sem quebrar imediatamente clientes que utilizam uma versão anterior.

---

# Validação

A API deve validar os dados recebidos antes de processá-los ou armazená-los.

Exemplo:

```json
{
    "nome": "",
    "idade": -500,
    "email": "abc"
}
```

Esses dados provavelmente devem ser rejeitados.

No FastAPI, o Pydantic é utilizado para facilitar essa validação.

---

# Request Schemas

Define os dados que o cliente pode enviar.

```python
class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    idade: int
```

---

# Response Schemas

Define os dados que a API pode devolver.

```python
class UserResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr
```

Isso evita expor informações que não deveriam sair da API, como:

```text
password_hash
```

---

# Documentação

APIs devem possuir documentação clara.

É importante documentar:

* endpoints
* métodos HTTP
* parâmetros
* body
* respostas
* status codes
* autenticação
* erros

O padrão **OpenAPI** é muito utilizado para descrever APIs.

O FastAPI gera documentação automaticamente através de ferramentas como Swagger UI e ReDoc.

---

# Rate Limiting

Rate limiting limita a quantidade de requisições que um cliente pode realizar.

Exemplo:

```text
100 requisições por minuto
```

Se o limite for ultrapassado:

```text
429 Too Many Requests
```

Isso ajuda a evitar abuso e sobrecarga.

---

# Webhooks

Webhook permite que um sistema envie uma notificação para outro sistema quando um evento acontece.

Exemplo:

```text
Pagamento aprovado
        ↓
Gateway
        ↓
POST /webhooks/payment
        ↓
Seu backend
```

---

# Princípios REST

Os principais constraints do REST são:

1. Client-Server
2. Stateless
3. Cacheable
4. Uniform Interface
5. Layered System
6. Code-on-Demand (opcional)

HATEOAS também faz parte da concepção completa de REST.

---

# Arquitetura de uma API

Uma aplicação pode seguir uma estrutura como:

```text
Cliente
   ↓
Router
   ↓
Controller
   ↓
Service
   ↓
Repository
   ↓
SQLAlchemy
   ↓
PostgreSQL
```

Por exemplo:

```text
POST /users
      ↓
users_router
      ↓
user_service
      ↓
user_repository
      ↓
SQLAlchemy
      ↓
PostgreSQL
```

---

# Exemplo de API REST com FastAPI

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/users")
def get_users():
    return [
        {"id": 1, "nome": "João"},
        {"id": 2, "nome": "Maria"}
    ]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "id": user_id,
        "nome": "João"
    }


@app.post("/users", status_code=201)
def create_user():
    return {
        "id": 3,
        "nome": "Carlos"
    }
```

Esse exemplo já demonstra:

* endpoint
* recurso
* GET
* POST
* path parameter
* status code
* JSON
* FastAPI

---

# Checklist

Uma API REST profissional deve considerar:

### Design

* [ ] Recursos bem definidos
* [ ] URLs claras
* [ ] Métodos HTTP apropriados
* [ ] Status codes corretos
* [ ] Versionamento

### Dados

* [ ] JSON consistente
* [ ] Validação
* [ ] Request schemas
* [ ] Response schemas
* [ ] Paginação

### Segurança

* [ ] HTTPS
* [ ] Autenticação
* [ ] Autorização
* [ ] Hash de senhas
* [ ] Validação de entrada
* [ ] Rate limiting
* [ ] Segredos fora do código

### Qualidade

* [ ] Tratamento de erros
* [ ] Logs
* [ ] Testes
* [ ] Documentação
* [ ] OpenAPI

---

# Resumo

```text
API
→ interface para comunicação entre sistemas

REST
→ estilo arquitetural para APIs

Resource
→ objeto/recurso disponibilizado pela API

Endpoint
→ ponto de acesso

GET
→ buscar

POST
→ criar

PUT
→ substituir

PATCH
→ atualizar parcialmente

DELETE
→ remover

2xx
→ sucesso

4xx
→ erro do cliente

5xx
→ erro do servidor

Path Parameter
→ identifica um recurso

Query Parameter
→ filtra/modifica uma consulta

Headers
→ metadados da requisição/resposta

Body
→ dados enviados

JSON
→ formato de dados muito utilizado

Authentication
→ quem é você?

Authorization
→ o que você pode fazer?

JWT
→ formato de token utilizado em autenticação

Stateless
→ cada requisição contém as informações necessárias

CRUD
→ Create, Read, Update, Delete

OpenAPI
→ especificação para descrição de APIs
```
