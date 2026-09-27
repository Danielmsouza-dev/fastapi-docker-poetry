# FastAPI com Docker, Compose e Poetry

Exemplo mínimo para executar uma API FastAPI em um container. O Poetry instala as dependências durante o build, e o volume do Compose sincroniza os arquivos locais para que o Uvicorn recarregue a aplicação durante o desenvolvimento.

## Pré-requisitos

- Docker Engine/Desktop iniciado
- Docker Compose (plugin `docker compose` ou comando legado `docker-compose`)

Não é necessário instalar Python ou Poetry na máquina host.

## Executar

Clone o repositório e entre na pasta que contém o `Dockerfile` e o `docker-compose.yml`. Construa a imagem e inicie o serviço em segundo plano:

```bash
docker-compose up --build -d
```

Se sua instalação usa o plugin Compose, o comando equivalente é:

```bash
docker compose up --build -d
```

A API ficará disponível em <http://localhost:8000>. A documentação interativa fica em <http://localhost:8000/docs> e a verificação de saúde em <http://localhost:8000/health>.

Para acompanhar os logs:

```bash
docker-compose logs -f api
```

Para parar e remover o container:

```bash
docker-compose down
```

Use `docker compose` em vez de `docker-compose` se estiver usando o plugin Compose.

## Desenvolvimento

O Compose monta a pasta do projeto em `/app` e inicia o Uvicorn com `--reload`. Salvar alterações em `main.py` atualiza a aplicação automaticamente. A porta `8000` do host é encaminhada à porta `8000` do container.

O `Dockerfile` instala uma versão fixada do Poetry, desativa ambientes virtuais dentro do container e usa `poetry install --only main --no-root` para instalar as dependências descritas no `pyproject.toml`. Caso queira fixar também as versões transitivas, gere e versione um `poetry.lock` com `poetry lock`; nesse exemplo introdutório ele é omitido para que não seja preciso instalar Poetry no host.

## Estrutura

```text
.
├── Dockerfile
├── docker-compose.yml
├── main.py
└── pyproject.toml
```