mande escrito
Diário de Estudos — 17/08/2026
📖 Conteúdo estudado
Continuação do projeto de integração entre ERP e APIs
Estruturação de OrderItem
Relacionamento entre Order, OrderItem e Product
Schemas Pydantic para itens de pedidos
Preparação dos endpoints de OrderItem
🧠 O que aprendi

Hoje dei continuidade ao projeto de integração entre ERP e APIs, avançando para a implementação dos itens dos pedidos (OrderItem).

Depois de finalizar o CRUD de clientes, produtos e pedidos, comecei a trabalhar na estrutura que permitirá que um pedido possua vários produtos.

Também revisei a relação entre as entidades do sistema:

Customer
   ↓
Order
   ↓
OrderItem
   ↓
Product

O OrderItem será responsável por representar cada produto presente em um pedido, permitindo trabalhar posteriormente com informações como produto, quantidade e preço.

Essa etapa é importante para transformar o sistema de pedidos em uma estrutura mais próxima de um ERP real.

💻 Próximos passos
Criar os schemas de OrderItem
Criar os endpoints de OrderItem
Validar se o Order existe
Validar se o Product existe
Testar os endpoints através do Swagger
Revisar os relacionamentos entre as entidades
🚀 Projeto

O projeto já possui:

CRUD de Customer
CRUD de Product
CRUD de Order
PostgreSQL
SQLAlchemy
FastAPI
Pydantic
Alembic
Documentação automática com Swagger

O próximo objetivo é finalizar OrderItem e deixar o fluxo de pedidos completo.