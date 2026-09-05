Diário de Estudos — 04/09/2026

📖 Conteúdo estudado

Dependency Injection (Injeção de Dependências) no FastAPI

Depends()

Funções de dependência

Injeção de dependências em rotas

Dependências com banco de dados

Dependências com autenticação

Dependências encadeadas

yield para criação e encerramento de recursos

Organização de dependências em projetos FastAPI

Boas práticas de arquitetura e testes

🧠 O que aprendi

Hoje estudei Dependency Injection (DI) no FastAPI, um recurso importante para organizar aplicações e evitar que cada rota precise criar ou conhecer diretamente todos os recursos de que depende.

A ideia principal é separar a responsabilidade de fornecer um recurso da responsabilidade de utilizá-lo. Em vez de uma rota criar diretamente uma sessão do banco, por exemplo, uma dependência pode fornecer essa sessão automaticamente.

No FastAPI, o principal recurso utilizado para isso é o Depends().

🔌 Dependency Injection

Dependency Injection significa Injeção de Dependências.

Uma dependência é qualquer recurso ou serviço que uma determinada função precisa para executar seu trabalho.

Exemplo conceitual:

def criar_pedido(cliente, db):
    ...

Nesse caso, a função depende de cliente e db.

Em vez de criar esses objetos dentro da própria função, podemos recebê-los de fora. Isso torna o código mais organizado, reutilizável e fácil de testar.

⚙️ Depends()

No FastAPI, usamos Depends() para declarar uma dependência.

from fastapi import Depends

def minha_dependencia():
    return "valor"

@app.get("/")
def rota(valor = Depends(minha_dependencia)):
    return {"valor": valor}

O FastAPI identifica que valor depende de minha_dependencia, executa a dependência e passa o resultado para a rota.

A rota não precisa chamar manualmente:

minha_dependencia()

O próprio FastAPI administra esse processo.

🗄️ Dependency Injection com banco de dados

Um dos usos mais importantes é fornecer uma sessão do SQLAlchemy para as rotas.

Exemplo:

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

A rota pode receber a sessão assim:

@app.get("/products")
def listar_produtos(db: Session = Depends(get_db)):
    produtos = db.query(Product).all()
    return produtos

Nesse cenário:

O cliente faz uma requisição.

O FastAPI identifica Depends(get_db).

get_db() cria uma sessão.

A sessão é entregue para a rota.

A rota utiliza o banco.

Depois da execução, o finally fecha a sessão.

Isso evita repetir a criação e o fechamento da conexão em todas as rotas.

🧹 yield nas dependências

O yield é especialmente útil quando precisamos executar alguma ação antes e depois da requisição.

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

Antes do yield, o recurso é preparado.

O valor depois do yield é disponibilizado para a rota.

Depois que a rota termina, o código do finally é executado.

Esse padrão é muito útil para recursos que precisam ser liberados corretamente.

🔐 Dependency Injection e autenticação

Dependency Injection também pode ser usada para autenticação.

Por exemplo:

def get_current_user(token: str = Depends(oauth2_scheme)):
    # validar token
    # buscar usuário
    return user

Uma rota protegida pode então fazer:

@app.get("/users/me")
def get_me(current_user = Depends(get_current_user)):
    return current_user

A rota não precisa repetir toda a lógica de:

receber o token;

validar o JWT;

verificar o usuário;

buscar o usuário no banco.

Tudo isso fica concentrado na dependência.

🔗 Dependências encadeadas

Uma dependência também pode depender de outra.

Exemplo:

def get_db():
    ...

def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    ...

Nesse caso, temos uma cadeia:

Rota
  ↓
get_current_user
  ↓
get_db

O FastAPI resolve essas dependências automaticamente.

🧩 Por que isso é importante?

Sem Dependency Injection, uma aplicação pode acabar com muita lógica repetida:

def rota():
    db = SessionLocal()

    token = ...
    user = ...

    # lógica da rota

Com DI:

def rota(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    ...

A rota fica focada na sua responsabilidade principal.

🏗️ Organização no projeto

Uma organização possível para uma API FastAPI é:

app/
├── main.py
├── database.py
├── models/
├── schemas/
├── routers/
├── services/
├── dependencies/
└── tests/

As dependências podem ficar em um arquivo separado:

app/
└── dependencies/
    └── auth.py

Por exemplo:

def get_current_user(...):
    ...

Isso evita colocar toda a lógica de autenticação dentro dos routers.

🧪 Dependency Injection e testes

DI também facilita muito os testes.

Uma dependência pode ser substituída por outra durante o teste.

O FastAPI possui mecanismos para sobrescrever dependências, permitindo utilizar, por exemplo, um banco de testes em vez do banco real.

A ideia é:

Aplicação
   ↓
get_db
   ↓
Banco real

Durante o teste:

Teste
   ↓
get_db_test
   ↓
Banco de testes

Isso permite testar as rotas de forma mais isolada.

🧠 Principais vantagens

Reutilização

A mesma dependência pode ser utilizada em várias rotas.

Organização

A lógica compartilhada fica fora das rotas.

Manutenção

Alterações em uma dependência podem ser feitas em um único lugar.

Testabilidade

Dependências podem ser substituídas durante os testes.

Separação de responsabilidades

Cada parte da aplicação possui uma responsabilidade mais clara.

Segurança

Lógicas como autenticação podem ser centralizadas em dependências.

⚠️ O que evitar

Não é recomendado transformar qualquer pequena função em uma dependência apenas por usar Depends().

Também é importante evitar colocar regras de negócio complexas diretamente nas dependências.

Uma boa separação pode ser:

Router
  ↓
Dependency
  ↓
Service
  ↓
Repository/Database

Cada camada possui uma responsabilidade.

🎯 Aplicação no projeto

No projeto da ERP Integration API, Dependency Injection é especialmente importante porque já existem componentes como:

banco PostgreSQL;

sessões SQLAlchemy;

autenticação JWT;

usuário autenticado;

routers;

services;

testes automatizados.

Um fluxo possível é:

Requisição
    ↓
Router
    ↓
Depends(get_current_user)
    ↓
Validação do JWT
    ↓
Usuário autenticado
    ↓
Service
    ↓
Banco de dados

Dessa forma, as rotas ficam mais limpas e a arquitetura da API fica mais organizada.

📌 Resumo

Hoje aprendi que Dependency Injection é uma técnica para fornecer às funções os recursos de que elas precisam sem que elas precisem criar esses recursos diretamente.

No FastAPI, o principal mecanismo para isso é o Depends().

Os principais conceitos estudados foram:

Dependency Injection;

Depends();

funções de dependência;

yield;

sessão do banco;

autenticação;

dependências encadeadas;

organização do projeto;

substituição de dependências em testes.

A principal ideia que ficou foi:

A rota deve se preocupar com o que precisa fazer, enquanto as dependências se preocupam em fornecer os recursos necessários para que ela faça isso.