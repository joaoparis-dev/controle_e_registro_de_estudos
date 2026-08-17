Diário de Estudos — 16/08/2026
📖 Conteúdo estudado
Continuação do projeto de integração entre ERP e APIs
Finalização dos endpoints de Order
Criação e gerenciamento de pedidos
Relacionamento entre Customer, Order, OrderItem e Product
Validação de clientes na criação de pedidos
Utilização de APIRouter
Integração entre FastAPI, SQLAlchemy e PostgreSQL
Testes dos endpoints através do Swagger
🧠 O que aprendi

Hoje continuei o desenvolvimento do projeto de integração entre ERP e APIs, com foco na entidade Order.

O objetivo principal foi completar a implementação dos pedidos, utilizando o que já havia aprendido durante a criação dos endpoints de clientes e produtos.

Também aprofundei o entendimento sobre os relacionamentos entre as entidades do sistema e como um pedido se relaciona com um cliente e posteriormente com seus itens e produtos.

📦 Orders

A entidade Order representa um pedido realizado por um cliente.

Cada pedido possui informações como:

id
customer_id
status
created_at

O customer_id funciona como uma chave estrangeira que relaciona o pedido ao cliente.

Customer
   │
   └── Order
🔗 Relacionamento com OrderItem

Um pedido pode possuir vários itens.

Order
   │
   ├── OrderItem
   ├── OrderItem
   └── OrderItem

Cada OrderItem representa um produto dentro daquele pedido, armazenando informações como:

Produto
Quantidade
Preço unitário

Dessa forma:

Customer
   │
   └── Order
          │
          ├── OrderItem → Product
          ├── OrderItem → Product
          └── OrderItem → Product
⚙️ Status do pedido

O modelo Order possui um valor padrão para o status:

status: Mapped[str] = mapped_column(
    String(30),
    default="pending"
)

Assim, quando um pedido é criado sem informar um status, ele começa automaticamente como:

pending

Posteriormente será possível implementar a alteração do status, por exemplo:

pending
   ↓
processing
   ↓
completed

ou:

pending
   ↓
cancelled
🧪 Testes

Os endpoints foram testados utilizando o Swagger, permitindo verificar na prática a comunicação entre:

FastAPI
   ↓
SQLAlchemy
   ↓
PostgreSQL

Também foi validada a criação de pedidos associados a clientes existentes.

📌 Estado atual do projeto

A API já possui uma estrutura funcional para:

Customers
   ├── Create
   ├── Read
   ├── Update
   └── Delete


Products
   ├── Create
   ├── Read
   ├── Update
   └── Delete


Orders
   ├── Create
   ├── Read
   ├── Update
   └── Delete

O próximo ponto importante é trabalhar com os OrderItems, permitindo adicionar produtos aos pedidos e calcular corretamente os valores de cada pedido.

🚀 Próximo passo

Continuar a implementação de OrderItem e integrar os produtos aos pedidos.

Depois disso, será possível começar a trabalhar com regras mais completas de negócio, como:

Adicionar produtos a um pedido
Definir quantidades
Calcular subtotal
Calcular valor total do pedido
Validar estoque
Atualizar estoque após uma compra
Controlar o status do pedido