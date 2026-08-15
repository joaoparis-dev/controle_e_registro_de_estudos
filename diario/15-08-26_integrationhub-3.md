Diário de Estudos — 15/08/2026

Conteúdo estudado
Continuação do projeto de integração entre ERP e APIs
Organização da API com APIRouter
CRUD de produtos
Endpoints de pedidos (Order)
Relacionamento entre Customer e Order
Validação da existência do cliente antes de criar um pedido
Valores padrão no SQLAlchemy
Testes dos endpoints através do Swagger
O que aprendi

Hoje continuei o desenvolvimento da API de integração entre ERP e APIs.

Primeiro, avancei na organização do projeto, separando os endpoints em routers utilizando APIRouter, deixando o main.py mais organizado.

Também implementei os endpoints de produtos, seguindo a mesma lógica que já havia utilizado anteriormente para clientes:

Criar produto
Listar produtos
Buscar produto por ID
Atualizar produto
Excluir produto

Depois comecei a implementação dos pedidos (Order).

Aprendi que um pedido depende de um cliente existente. Antes de criar um pedido, a API verifica se o customer_id informado realmente existe no banco de dados.

Também corrigi um pequeno erro relacionado à utilização do método .first() do SQLAlchemy. É necessário utilizar os parênteses para executar o método:

.first()

em vez de:

.first
Criação de pedidos

O endpoint criado permite receber um customer_id e criar um novo pedido associado ao cliente.

Exemplo:

{
    "customer_id": 2
}

A API verifica se o cliente existe e, caso exista, cria o pedido.

Valores padrão no SQLAlchemy

Também entendi melhor como funcionam os valores default definidos nos modelos.

No modelo Order, foi definido:

status: Mapped[str] = mapped_column(
    String(30),
    default="pending"
)

Por isso, quando o endpoint cria um pedido sem informar o status:

new_order = Order(
    customer_id=order_data.customer_id
)

o SQLAlchemy automaticamente utiliza:

status = "pending"

O mesmo conceito é utilizado para created_at:

created_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
    default=lambda: datetime.now(timezone.utc)
)

Assim, alguns valores são preenchidos automaticamente pelo ORM.

Estrutura atual

A estrutura das entidades está começando a ficar mais completa:

Customer
   │
   └── Order
          │
          └── OrderItem
                 │
                 └── Product

Um cliente pode possuir vários pedidos, e cada pedido poderá possuir vários itens. Cada item estará associado a um produto.

Testes

Utilizei o Swagger para testar os endpoints da API.

A criação de pedidos foi testada com sucesso e a API retornou um pedido contendo:

{
    "id": 5,
    "customer_id": 2,
    "status": "pending",
    "created_at": "2026-08-15T15:07:33.232233-03:00"
}
Próximo passo

Continuar a implementação dos pedidos, principalmente a parte de OrderItem, permitindo adicionar produtos e quantidades dentro de um pedido.

Depois disso, continuar evoluindo a API e melhorar a organização do projeto.