from sqlalchemy.orm import Session

from . import models, schemas
import datetime

'''CRUD CLIENTE'''


def get_cliente_by_id(db: Session, cliente_id: int):
    return db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()


def get_cliente_by_cpf(db: Session, cliente_cpf: str):
    return db.query(models.Cliente).filter(models.Cliente.cpf == cliente_cpf).first()


def get_cliente(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cliente).offset(skip).limit(limit).all()


def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    db_cliente = models.Cliente(cpf=cliente.cpf,
                                nome=cliente.nome,
                                telefone=cliente.telefone,
                                fgts=cliente.fgts)
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente


'''________________________________________________________________________________________'''
'''CRUD CONTATOS'''


def get_contato_by_id(db: Session, contato_id: int):
    return db.query(models.Contato).filter(models.Contato.id == contato_id).first()


def get_contato_by_cpf(db: Session, contato_cpf: int):
    '''retorna todos contatos do cliente'''
    return db.query(models.Contato).filter(models.Contato.cpf == contato_cpf).all()


def get_active_contato(db: Session, cpf: str = None):
    '''retorna contatos ativos'''
    if cpf:
        return db.query(models.Contato).filter(models.Contato.cpf == cpf and models.Contato.status == 0).all()
    else:
        return db.query(models.Contato).filter(models.Contato.status == 0).all()


def get_contato(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_contato(db: Session, contato: schemas.ContatoCreate):
    db_contato = models.Contato(cpf=contato.cpf,
                                telefone=contato.telefone,
                                interesse=contato.interesse,
                                date=datetime.now(),
                                status=contato.status)
    db.add(db_contato)
    db.commit()
    db.refresh(db_contato)
    return db_contato
