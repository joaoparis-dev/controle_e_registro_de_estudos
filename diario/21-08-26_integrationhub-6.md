Diário de Estudos — 20/08/2026
📖 Conteúdo estudado
Continuação do projeto de integração ERP
OrderItem e regras de negócio
Controle de estoque
Criação, atualização e exclusão de itens de pedido
Validação de estoque disponível
Ajuste automático do estoque ao alterar a quantidade
Devolução do estoque ao excluir um item
Separação entre routers e services
Refatoração da lógica de negócio
🧠 O que aprendi

Hoje continuei o desenvolvimento da API de integração ERP, focando principalmente nas regras de negócio relacionadas aos OrderItems.

Implementei o controle de estoque durante a criação de um item de pedido. A API verifica se o produto existe, se existe estoque suficiente e utiliza automaticamente o preço cadastrado no produto como unit_price.

Também trabalhei na atualização dos itens de pedido. Ao alterar a quantidade, a API calcula a diferença entre a quantidade antiga e a nova para ajustar corretamente o estoque.

Por exemplo:

Quantidade antiga: 2
Quantidade nova: 5

5 - 2 = 3

Estoque diminui em 3

Da mesma forma, quando a quantidade é reduzida, a diferença é devolvida ao estoque.

Também implementei a devolução do estoque ao excluir um OrderItem.

🔄 Fluxo do estoque

O funcionamento ficou:

POST OrderItem
       ↓
Diminui estoque

PUT OrderItem
       ↓
Compara quantidade antiga e nova
       ↓
Ajusta estoque

DELETE OrderItem
       ↓
Devolve quantidade ao estoque
🏗️ Organização do projeto

Também comecei a refatorar a aplicação para separar as responsabilidades entre routers e services.

Antes, o router concentrava tanto a parte HTTP quanto as regras de negócio.

Agora estamos buscando uma estrutura como:

Router
   ↓
Service
   ↓
Database

O router ficará responsável principalmente por receber as requisições, trabalhar com os schemas e chamar os services.

Os services ficarão responsáveis pelas regras de negócio da aplicação.

📁 Estrutura

A organização está caminhando para:

app/
├── models/
├── schemas/
├── routers/
│   ├── customers.py
│   ├── products.py
│   ├── orders.py
│   └── order_items.py
│
├── services/
│   ├── order_service.py
│   └── order_item_service.py
│
├── database.py
└── main.py
🧠 Principal aprendizado

Hoje entendi melhor a diferença entre CRUD e regra de negócio.

Criar, buscar, atualizar e excluir registros é apenas uma parte da API. Em uma aplicação real, existem regras que precisam ser respeitadas, como:

Não permitir estoque negativo.
Usar o preço cadastrado do produto.
Ajustar o estoque quando a quantidade do pedido muda.
Devolver o estoque quando um item é excluído.
Impedir a exclusão de clientes que possuem pedidos.

Também entendi que essas regras não precisam ficar diretamente nos endpoints. Podemos colocá-las em services, deixando o código mais organizado, reutilizável e fácil de manter.

🚀 Próximos passos
Finalizar a refatoração de OrderItem para services
Testar todos os endpoints após a refatoração
Refatorar Orders
Refatorar Products
Refatorar Customers
Melhorar validações dos schemas
Trabalhar com transações de forma mais robusta
Implementar autenticação com JWT
Criar integrações externas
Adicionar testes automatizados
Preparar a API para produção