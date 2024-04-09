from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import crud, models, schemas
from database.database import SessionLocal


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/lista_clientes", response_model=schemas.Cliente)
async def read_cliente(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_cliente = crud.get_cliente(db, skip=skip, limit=limit)
    if db_cliente is None:
        HTTPException(status_code=404, detail="Nenhum Cliente Cadastrado")
        return 0
    return db_cliente


@router.put("/")
async def modify_cliente():
    '''Modifica informaçao de um cliente'''
    pass


@router.post('/create', response_model=schemas.Cliente)
async def create_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    '''cria novo cliente'''
    db_cliente = crud.get_cliente_by_cpf(db, cliente_cpf=cliente.cpf)
    if db_cliente:
        raise HTTPException(status_code=400, detail="CPF already registered")
    return crud.create_cliente(db=db, cliente=cliente)
