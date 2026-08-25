# Diário de Estudos — 24/08/2026

## 📖 Conteúdo estudado

* Refatoração dos schemas da API
* Organização dos schemas em arquivos separados
* Validação de dados com Pydantic
* Separação de responsabilidades entre Router, Schema, Service e Model
* Revisão das regras de negócio da ERP Integration API
* Testes das validações no Swagger

## 🧠 O que aprendi

Hoje finalizei uma etapa importante da estrutura da **ERP Integration API**.

Os schemas, que anteriormente estavam concentrados em um único arquivo, foram organizados em uma pasta própria, separando cada recurso em seu respectivo arquivo:

* `customer.py`
* `product.py`
* `order.py`
* `order_item.py`

Também implementei validações utilizando recursos do **Pydantic**, garantindo que dados inválidos sejam rejeitados antes de chegarem às regras de negócio.

Entre as validações implementadas estão:

* Preços maiores que zero.
* Estoque maior ou igual a zero.
* Quantidades de produtos maiores que zero.
* IDs válidos.
* Tamanho mínimo e máximo para determinados campos.
* Validação de e-mail.

Após as alterações, testei as validações através do Swagger e confirmei que estão funcionando corretamente.

## 🏗️ Arquitetura atual

A aplicação está organizada seguindo uma separação clara de responsabilidades:

```text
Request
   ↓
Router
   ↓
Schema / Pydantic
   ↓
Service
   ↓
SQLAlchemy Model
   ↓
PostgreSQL
```

Os **schemas** ficam responsáveis pela validação dos dados recebidos, enquanto os **services** continuam responsáveis pelas regras de negócio.

## 📦 Regras de negócio revisadas

Também revisei as regras implementadas anteriormente:

* Controle de estoque.
* Verificação de produtos ativos.
* Criação e atualização de OrderItems.
* Devolução de estoque ao excluir itens.
* Devolução de estoque ao excluir pedidos.
* Cálculo do total dos pedidos.
* Soft delete de produtos.
* Validação da existência de clientes, produtos e pedidos.

## 🎯 Resultado

Com as validações funcionando, a estrutura básica da API está praticamente finalizada.

A ERP Integration API agora possui uma base organizada e com uma separação clara entre:

* HTTP
* Validação
* Regras de negócio
* Persistência
* Banco de dados

## 🚀 Próximo passo

A próxima etapa será iniciar a **autenticação da API**.

Pretendo implementar:

* Modelo de usuário.
* Cadastro de usuários.
* Hash de senhas.
* Login.
* JWT.
* Proteção das rotas.
* Autorização e permissões.
