import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import engine
from database import models
from routes import clientes, contatos

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(clientes.router, prefix="/cliente")
app.include_router(contatos.router, prefix="/contato")


@app.get("/")
async def main():
    return {'message': "Pagina inicial ainda em construção"}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
