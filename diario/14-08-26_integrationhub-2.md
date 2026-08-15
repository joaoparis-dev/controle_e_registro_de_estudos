Diário de Estudos — 14/08/2026
📖 Conteúdo estudado
Continuação do projeto de integração entre ERP e APIs
CRUD de clientes com FastAPI
Integração entre FastAPI, SQLAlchemy e PostgreSQL
Tratamento de erros HTTP
Schemas Pydantic
Estrutura e relacionamento entre Customer, Product, Order e OrderItem
🧠 O que aprendi

Hoje continuei o projeto de integração entre ERP e APIs, avançando na construção da API utilizando FastAPI.

Completei o CRUD de clientes, implementando operações para criar, listar, buscar, atualizar e excluir clientes.

Também aprendi a utilizar HTTPException para retornar respostas HTTP apropriadas quando um recurso não existe, utilizando o status 404 Not Found.

Além disso, comecei a estruturar a parte de produtos da aplicação, criando os schemas necessários para trabalhar com produtos através da API.

Também entendi melhor a dependência entre as entidades do sistema e a ordem em que elas devem ser implementadas.

A estrutura lógica do projeto ficou:

Customer
   ↓
Order
   ↓
OrderItem ← Product

Para criar pedidos corretamente, precisamos ter clientes e produtos previamente cadastrados.

💻 O que foi implementado
CRUD de Customers

Foram implementados os seguintes endpoints:

POST   /customers
GET    /customers
GET    /customers/{id}
PUT    /customers/{id}
DELETE /customers/{id}
Tratamento de erros

Foi utilizado:

HTTPException

para retornar:

404 Not Found

quando um cliente não é encontrado.

Schemas de Product

Foram criados os schemas:

ProductCreate
ProductUpdate
ProductResponse

Esses schemas serão utilizados para validar os dados dos produtos na API.

🔗 Estrutura das entidades

O projeto possui atualmente:

Customer
   │
   ▼
Order
   │
   ▼
OrderItem ← Product

O OrderItem funciona como uma entidade intermediária entre pedidos e produtos, permitindo que um pedido possua vários produtos e que um produto apareça em vários pedidos.

📌 Próximo passo

Amanhã continuarei a implementação de Products, criando os endpoints da API e conectando-os ao PostgreSQL.

Depois disso, será implementado o fluxo de:

Products
   ↓
Orders
   ↓
OrderItems
   ↓
Integração com ERP externo

Hoje finalizei a parte de clientes e deixei a estrutura de produtos preparada para continuar o projeto amanhã.