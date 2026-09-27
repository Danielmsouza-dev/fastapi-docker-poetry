from fastapi import FastAPI

app = FastAPI(title="FastAPI com Docker e Poetry", version="1.0.0")


@app.get("/", tags=["health"])
def read_root() -> dict[str, str]:
    return {"message": "Olá! A aplicação FastAPI está rodando no Docker."}


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}
