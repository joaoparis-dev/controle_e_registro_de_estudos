# Diário de Estudos — 09/09/2026

## 📖 Conteúdo estudado

Hoje estudei **Cookies e Tokens**, aprofundando os conceitos relacionados à autenticação e segurança de aplicações web e APIs.

Foram estudados:

* Cookies
* Sessões
* Tokens
* Bearer Token
* JWT (JSON Web Token)
* Header, Payload e Signature
* Access Token
* Refresh Token
* Expiração de tokens
* Stateless e Stateful
* Cookies `HttpOnly`
* Cookies `Secure`
* `SameSite`
* `localStorage`
* CSRF
* XSS
* Logout e revogação de tokens
* HTTPS
* Segurança no armazenamento e transporte de credenciais
* Diferença entre autenticação e autorização
* Utilização de JWT com APIs e FastAPI

## 🧠 O que aprendi

Aprendi que Cookies e Tokens são conceitos diferentes.

O **cookie** é um mecanismo utilizado principalmente pelo navegador para armazenar e enviar informações, enquanto o **token** pode funcionar como uma credencial utilizada para autenticar requisições.

Também aprendi como funciona o JWT, que possui três partes:

```text
Header.Payload.Signature
```

Entendi que a assinatura permite verificar a integridade do token, mas que um JWT assinado não significa que seu conteúdo seja secreto.

Estudei também a diferença entre **Access Token** e **Refresh Token**, entendendo que o Access Token é utilizado para acessar recursos protegidos, enquanto o Refresh Token pode ser utilizado para obter novos Access Tokens.

Aprendi sobre cookies `HttpOnly`, `Secure` e `SameSite`, além dos riscos relacionados a XSS e CSRF.

Também entendi melhor a diferença entre autenticação e autorização e como esses conceitos se relacionam com APIs protegidas.

## 💻 Áreas estudadas

### Cookies

* Armazenamento no navegador
* `HttpOnly`
* `Secure`
* `SameSite`
* Cookies de sessão

### Tokens

* Bearer Token
* Access Token
* Refresh Token
* Expiração
* Revogação

### JWT

* Header
* Payload
* Signature
* Claims
* Chave secreta
* Validação
* Expiração

### Segurança

* HTTPS
* XSS
* CSRF
* Armazenamento de tokens
* Proteção de credenciais

### FastAPI

* Autenticação baseada em tokens
* `Authorization: Bearer`
* Integração com JWT
* Relação entre autenticação e endpoints protegidos

## ⚠️ Dificuldades

Nenhuma dificuldade relevante registrada.

## 🎯 Próximo passo

Continuar aprofundando autenticação e segurança de APIs, estudando conceitos como **OAuth2, CORS, CSRF e Refresh Tokens**, e posteriormente aplicar esses conhecimentos na API ERP Integration.
