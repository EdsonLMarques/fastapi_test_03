from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from database.database import Base


class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    cpf = Column(String)
    nome = Column(String)
    telefone = Column(String)
    fgts = Column(Float)

    #contatos = relationship("Contato", back_populates="cliente")


class Contato(Base):
    __tablename__ = "contatos"
    id = Column(Integer, primary_key=True)
    cpf = Column(String, ForeignKey('clientes.cpf'))
    interesse = Column(Boolean)
    date = Column(DateTime)
    status = Column(Integer, default=0)

    #cliente = relationship("Cliente", back_populates="contato")
