Diário de Estudos — 20/08/2026
📖 Conteúdo estudado
Integração entre Product, Order e OrderItem
Regras de negócio no backend
Criação de itens de pedido
Preço do produto aplicado automaticamente ao OrderItem
Controle de estoque
Validação de estoque disponível
Organização da lógica no services
🧠 O que aprendi

Hoje continuei o desenvolvimento do projeto de integração ERP com FastAPI, PostgreSQL e SQLAlchemy.

Trabalhei principalmente na lógica de negócio dos itens de pedido (OrderItem), entendendo que o preço não deve ser informado livremente pelo cliente. Ao criar um item, a API deve buscar o produto e utilizar o preço cadastrado nele como unit_price.

Também comecei a implementar o controle de estoque. Antes de criar um OrderItem, a API deve verificar se o produto existe e se possui estoque suficiente para atender à quantidade solicitada. Quando o item é criado, a quantidade correspondente é descontada do estoque.

💻 Implementação
OrderItem

O fluxo ficou:

Cliente envia order_id, product_id e quantity
                ↓
          Busca o Order
                ↓
          Busca o Product
                ↓
      Verifica estoque disponível
                ↓
       Pega o preço do Product
                ↓
        Cria o OrderItem
                ↓
       Diminui o estoque
Controle de estoque

Também foi implementada a validação para impedir que um pedido seja criado com uma quantidade maior que o estoque disponível.

Exemplo:

Estoque: 5
Quantidade solicitada: 2


5 - 2 = 3

Caso a quantidade solicitada seja maior que o estoque, a API retorna:

400 Bad Request
Insufficient stock
🔗 Relação entre as entidades

O fluxo atual do projeto está ficando mais próximo de um sistema ERP real:

Customer
   ↓
Order
   ↓
OrderItem
   ↓
Product
   ↓
Stock

O OrderItem funciona como a ligação entre o pedido e o produto, armazenando também o preço praticado no momento da venda.

🚀 Próximos passos
Ajustar o estoque ao editar um OrderItem
Devolver o estoque ao excluir um OrderItem
Melhorar o uso de transações
Organizar as regras de negócio nos services
Implementar autenticação com JWT
Criar integrações externas
Adicionar testes automatizados
Melhorar a documentação da API
Preparar o projeto para produção
📌 Resumo

Hoje avancei do CRUD básico para regras de negócio mais próximas de uma aplicação real. A API agora começa a controlar relações entre pedidos, produtos, itens de pedido, preços e estoque, tornando o projeto mais próximo de uma integração ERP de verdade.