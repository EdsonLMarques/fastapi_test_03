from pydantic import BaseModel
from datetime import datetime
# Não deveria ser necessario importar desde o python 3.9.. ficar de olho!
from typing import List


class ClienteBase(BaseModel):
    cpf: str
    nome: str
    telefone: str
    fgts: float


class ClienteCreate(ClienteBase):
    pass


class Cliente(ClienteBase):
    id: int
    contatos: List["Contato"] = []

    class Config:
        orm_mode = True

'''______________________________________________CONTATOS________________________________________________'''
class ContatoBase(BaseModel):
    cpf: str
    interesse: bool
    status:int


class ContatoCreate(ContatoBase):
    pass


class Contato(ContatoBase):
    id: int
    date: datetime
    cliente_id: int

    class Config:
        orm_mode = True
