# Diário de Estudos — 25/08/2026

## 📖 Conteúdo estudado

* Autenticação em APIs
* Criação e gerenciamento de usuários
* Hash de senhas
* Login
* JWT (JSON Web Token)
* Geração e validação de tokens
* Proteção de endpoints
* Autorização de usuários

## 🧠 O que aprendi

Hoje finalizei a implementação da **autenticação da API** do projeto de integração com ERP.

Implementei o fluxo de autenticação utilizando usuários, senhas protegidas por hash e **JWT**, permitindo que a API identifique usuários autenticados e controle o acesso aos endpoints protegidos.

Também consolidei a diferença entre **autenticação**, que verifica quem é o usuário, e **autorização**, que determina quais recursos esse usuário pode acessar.

## 🔐 Autenticação

Durante a implementação, trabalhei com:

* Criação do modelo de usuário.
* Armazenamento seguro das senhas utilizando hash.
* Validação das credenciais durante o login.
* Geração de tokens JWT.
* Validação dos tokens recebidos pela API.
* Utilização do usuário autenticado nos endpoints protegidos.

## 🎫 JWT

Aprendi como o JWT é utilizado para manter a autenticação entre as requisições.

O fluxo implementado ficou basicamente:

```text
Usuário
   ↓
Login
   ↓
Validação de email e senha
   ↓
Geração do JWT
   ↓
Cliente recebe o token
   ↓
Envia o token nas próximas requisições
   ↓
API valida o JWT
   ↓
Acesso ao endpoint protegido
```

## 💻 Tecnologias utilizadas

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* JWT
* Hash de senhas
* Alembic

## 🎯 Resultado

Com a autenticação finalizada, a API agora possui uma camada de segurança que permite controlar o acesso aos seus recursos através de usuários autenticados e tokens JWT.

Essa etapa representa a conclusão da parte de **autenticação do backend**, avançando o projeto para uma estrutura mais próxima de uma API real de produção.

## 🚀 Próximo passo

O próximo foco será iniciar os **testes automatizados da API**, começando pelos testes de criação de usuários e posteriormente expandindo para autenticação, produtos, clientes, pedidos e demais regras de negócio.
