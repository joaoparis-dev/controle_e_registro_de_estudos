# Diário de Estudos — 08/08/2026

**Tempo de estudo:** 2 horas

## Estudei:

* APIs REST
* HTTP
* Métodos HTTP
* Endpoints e recursos
* Request e Response
* Status Codes
* JSON
* Headers
* Path Parameters
* Query Parameters
* CRUD
* Autenticação e autorização
* JWT
* HTTPS
* CORS
* Stateless
* Idempotência
* Paginação
* Versionamento de APIs
* Validação
* OpenAPI
* Rate Limiting
* Webhooks

## Aprendi:

Hoje estudei APIs REST e construí uma visão completa de como uma API funciona.

Aprendi que uma API é uma interface que permite a comunicação entre diferentes sistemas e que REST é um estilo arquitetural utilizado para construir APIs, normalmente utilizando HTTP.

Entendi o conceito de **recursos**, como `/users`, `/products` e `/orders`, e como os métodos HTTP representam as operações realizadas sobre esses recursos.

Também revisei os principais métodos:

* `GET` para buscar dados
* `POST` para criar recursos
* `PUT` para substituir recursos
* `PATCH` para alterações parciais
* `DELETE` para remover recursos

Estudei CRUD e sua relação com os métodos HTTP.

Também aprendi a diferença entre **path parameters** e **query parameters**, além da função dos headers, body e JSON nas requisições e respostas HTTP.

Estudei os principais status codes, principalmente:

* `200 OK`
* `201 Created`
* `204 No Content`
* `400 Bad Request`
* `401 Unauthorized`
* `403 Forbidden`
* `404 Not Found`
* `409 Conflict`
* `422 Unprocessable Content`
* `500 Internal Server Error`
* `503 Service Unavailable`

Também entendi melhor a diferença entre **autenticação** e **autorização**, além do funcionamento geral de tokens Bearer e JWT.

Aprendi o conceito de **stateless**, uma das características importantes do REST, e também conceitos como idempotência, paginação, versionamento, CORS, rate limiting e webhooks.

Por fim, entendi como esses conceitos se conectam com o que vou estudar na próxima etapa:

```text
FastAPI
   ↓
Pydantic
   ↓
SQLAlchemy
   ↓
PostgreSQL
   ↓
Autenticação
   ↓
JWT
   ↓
API REST
```

## Dificuldade:

Nenhuma dificuldade significativa.

O conteúdo foi principalmente conceitual e serviu como preparação para começar a desenvolver APIs com FastAPI.

## Próximo passo:

Começar o estudo de **FastAPI**, colocando em prática os conceitos de APIs REST, HTTP, rotas, requests, responses, parâmetros e validação.

## Observação:

Hoje finalizei a base conceitual necessária para começar a segunda fase do meu plano de estudos de backend.
