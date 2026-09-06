Diário de Estudos — 05/09/2026

📖 Conteúdo estudado

Middleware

Middleware no FastAPI

Ciclo de requisição e resposta

Request e Response

call_next

Middleware HTTP

Middleware global

Ordem de execução dos middlewares

Tratamento de requisições e respostas

Logging com middleware

Medição de tempo de resposta

Headers HTTP

CORS

Diferença entre middleware, dependency e endpoint

Boas práticas e cuidados com middleware

🧠 O que aprendi

Hoje estudei o conceito de middleware e como ele funciona dentro de uma aplicação web, especialmente utilizando o FastAPI.

Aprendi que middleware é uma camada que fica no caminho entre a requisição do cliente e o processamento da aplicação. Ele pode executar código antes da requisição chegar ao endpoint e também depois que o endpoint termina e uma resposta está sendo produzida.

O middleware é útil para implementar comportamentos que precisam ser aplicados a várias ou todas as rotas da aplicação, como:

Logging;

Medição do tempo de resposta;

Adição ou leitura de headers;

Tratamento de determinadas requisições;

CORS;

Monitoramento;

Algumas tarefas relacionadas à autenticação e segurança.

Também aprendi que o middleware não substitui o endpoint. Ele funciona como uma camada intermediária que pode observar, modificar ou interromper o fluxo de uma requisição.

🔄 Ciclo básico

O fluxo estudado foi:

Cliente
   ↓
Requisição HTTP
   ↓
Middleware
   ↓
Endpoint / Router
   ↓
Service / Regras de negócio
   ↓
Banco de dados
   ↓
Resposta
   ↓
Middleware
   ↓
Cliente

O middleware pode atuar tanto na entrada quanto na saída.

🧩 Middleware no FastAPI

No FastAPI, uma forma simples de criar middleware HTTP é utilizando:

from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def meu_middleware(request: Request, call_next):
    response = await call_next(request)

    return response

O request representa a requisição recebida.

O call_next permite encaminhar a requisição para a próxima etapa do processamento, normalmente outro middleware ou o endpoint.

O response representa a resposta produzida pela aplicação.

⏱️ Medindo o tempo de resposta

Um dos exemplos estudados foi medir quanto tempo uma requisição demora para ser processada:

import time

from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def medir_tempo(request: Request, call_next):
    inicio = time.perf_counter()

    response = await call_next(request)

    fim = time.perf_counter()

    tempo = fim - inicio

    response.headers["X-Process-Time"] = str(tempo)

    return response

Esse exemplo mostra como o middleware pode executar uma ação antes do endpoint, esperar o processamento terminar e depois modificar a resposta.

📝 Logging

Também estudei como middleware pode ser utilizado para registrar informações sobre as requisições:

import time

from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    inicio = time.perf_counter()

    response = await call_next(request)

    tempo = time.perf_counter() - inicio

    print(
        f"{request.method} {request.url.path} "
        f"-> {response.status_code} "
        f"({tempo:.4f}s)"
    )

    return response

Esse tipo de middleware pode ajudar a identificar:

Qual endpoint foi chamado;

Qual método HTTP foi utilizado;

Qual foi o status da resposta;

Quanto tempo a requisição demorou.

🛡️ Middleware e autenticação

Também compreendi que middleware pode participar de mecanismos relacionados à segurança, mas não significa que toda autenticação deva ser feita nele.

No projeto da API, a autenticação baseada em JWT pode continuar sendo tratada de forma mais específica por meio de dependencies, enquanto um middleware pode ser utilizado para tarefas gerais, como logging ou monitoramento.

🔀 Middleware x Dependency x Endpoint

Uma diferença importante estudada:

Middleware

Atua em uma camada mais global da aplicação.

Exemplos:

Logging;

CORS;

Tempo de resposta;

Headers;

Monitoramento.

Dependency

É utilizada para fornecer lógica ou dados necessários a determinados endpoints.

Exemplos:

Obter o usuário autenticado;

Obter uma sessão do banco;

Validar um token;

Reutilizar regras de acesso.

Endpoint

É responsável por receber uma requisição específica e executar a operação correspondente.

Exemplo:

@app.get("/products")
def list_products():
    return {"products": []}

⚠️ Cuidados

Middleware deve ser utilizado com responsabilidade.

Não é uma boa prática colocar toda a lógica da aplicação dentro dele.

Regras específicas de negócio devem continuar nos lugares apropriados, como:

Router
   ↓
Service
   ↓
Repository / Database

O middleware deve ficar focado em responsabilidades transversais que fazem sentido para várias partes da aplicação.

📚 Resumo

Hoje aprendi que middleware é uma camada intermediária entre o cliente e a aplicação.

Ele permite executar lógica:

Antes do endpoint;

Durante o encaminhamento da requisição;

Depois que o endpoint produz a resposta.

No FastAPI, o middleware HTTP pode ser criado com:

@app.middleware("http")

E o fluxo normalmente utiliza:

response = await call_next(request)

Os principais usos estudados foram logging, medição de desempenho, headers, CORS, monitoramento e outras responsabilidades que atravessam várias rotas da aplicação.

🎯 Próximos passos

Implementar um middleware de logging na API;

Testar middleware com pytest;

Entender melhor CORS;

Estudar tratamento global de exceções;

Integrar logging estruturado à API.