'''As rotas de contato sao para receber e tratar os dados provenientes do robo de marketing.
A rota POST é responsavel por criar novos registros de contato.
Ja a rota PUT é responsavel por alterar status dos contatos
CADA CONTATO REGISTRADO SERÁ TRATADO COMO UM 'CARD'
'''

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_contato():
    '''busca por todos os contatos'''
    pass


@router.put("/")
async def modify_contato():
    '''modifica atributos de um contato'''
    pass


@router.post("/")
async def create_contato():
    '''cria um novo registro de contato'''
    pass
