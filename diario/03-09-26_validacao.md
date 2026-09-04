# Diário de Estudos — 03/09/2026

## 📖 Conteúdo estudado

* Validação de dados no FastAPI
* Pydantic
* Schemas de entrada e saída
* `Field`
* `EmailStr`
* Validação de strings e números
* `Enum`
* `field_validator`
* `model_validator`
* Validação de parâmetros de rota
* Validação de query parameters
* Códigos de erro `422`
* Validação de respostas
* Testes automatizados de validação

## 🧠 O que aprendi

Hoje estudei validação de dados no FastAPI, entendendo como o Pydantic é utilizado para verificar e controlar os dados recebidos pela API.

Aprendi a definir campos obrigatórios e opcionais, limitar tamanho de strings, validar e-mails, números e valores permitidos, além de criar validações personalizadas.

Também entendi a diferença entre **validação dos dados** e **regras de negócio**. A validação deve verificar se os dados possuem o formato esperado, enquanto as regras de negócio ficam na camada de serviços.

## 💻 Principais conceitos

### Pydantic

Aprendi que o Pydantic é responsável por validar os dados recebidos pela API através dos schemas.

### `Field`

Utilizei `Field` para definir restrições como:

* `min_length`
* `max_length`
* `gt`
* `ge`
* `lt`
* `le`
* `pattern`

### `EmailStr`

Aprendi a utilizar `EmailStr` para validar se um campo possui um formato de e-mail válido.

### Validadores personalizados

Estudei `field_validator` para validações específicas de um campo e `model_validator` para situações em que é necessário validar múltiplos campos em conjunto.

### Validação de parâmetros

Também aprendi que o FastAPI permite validar diferentes partes de uma requisição:

* Path parameters
* Query parameters
* Body
* Headers

## 🧪 Testes automatizados

Como estou avançando na etapa de testes automatizados da API, também estudei como testar cenários de validação.

Alguns exemplos:

* Usuário com dados válidos
* E-mail inválido
* Senha muito curta
* Username muito curto
* Campo obrigatório ausente
* Valores numéricos inválidos
* Tipos de dados incorretos

Aprendi que erros de validação normalmente resultam em **HTTP 422 — Unprocessable Entity**.

## 🎯 Próximo passo

Continuar os testes automatizados da API, aplicando as validações estudadas aos schemas existentes e criando testes para verificar tanto os casos válidos quanto os casos inválidos.
