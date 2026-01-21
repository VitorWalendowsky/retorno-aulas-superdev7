from sqlalchemy.orm import Session
from src.database.models import Teclado


def cadastrar(db: Session, nome: str, modelo: str, tipo_conexao: str, cor: str, preco: float):
    teclado = Teclado(nome=nome, modelo=modelo, tipo_conexao=tipo_conexao, cor=cor, preco=preco)

    db.add(teclado)
    db.commit()
    db.refresh(teclado)

    return teclado


def editar(db: Session, id: int, nome: str, modelo: str, tipo_conexao: str, cor: str, preco: float) -> int:
    teclado = db.query(Teclado).filter(Teclado.id == id).first()

    if not teclado:
        return 0
    
    teclado.nome = nome
    teclado.modelo = modelo
    teclado.tipo_conexao = tipo_conexao
    teclado.cor = cor
    teclado.preco = preco

    db.commit()

    return 1


def apagar(db: Session, id: int) -> int:
    teclado = db.query(Teclado).filter(Teclado.id == id).first()

    if not teclado:
        return 0
    
    db.delete(teclado)
    db.commit()

    return 1


def obter_todos(db: Session):
    teclados = db.query(Teclado).all()

    return teclados


def obter_por_id(db: Session, id: int):
    teclado = db.query(Teclado).filter(Teclado.id == id).first()

    return teclado