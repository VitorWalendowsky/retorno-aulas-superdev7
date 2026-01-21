from sqlalchemy.orm import Session
from src.database.models import Mouse


def cadastrar(db: Session, nome: str, dpi: int, modelo: str, rgb: bool, quantidade_botao: int, preco: float):
    mouse = Mouse(nome=nome, dpi=dpi, modelo=modelo, rgb=rgb, quantidade_botao=quantidade_botao, preco=preco)
    db.add(mouse)
    db.commit()
    db.refresh(mouse)
    return mouse


def editar(db: Session, id: int, nome: str, dpi: int, modelo: str, rgb: bool, quantidade_botao: int, preco: float) -> int:
    mouse = db.query(Mouse).filter(Mouse.id == id).first()

    if not mouse:
        return 0
    
    mouse.nome = nome
    mouse.dpi = dpi
    mouse.modelo = modelo
    mouse.rgb = rgb
    mouse.quantidade_botao = quantidade_botao
    mouse.preco = preco

    db.commit()

    return 1


def apagar(db: Session, id: int) -> int:
    mouse = db.query(Mouse).filter(Mouse.id == id).first()

    if not mouse:
        return 0
    
    db.delete(mouse)
    db.commit()

    return 1


def obter_todos(db:Session):
    mouses = db.query(Mouse).all()

    return mouses


def obter_por_id(db: Session, id: int):
    mouse = db.query(Mouse).filter(Mouse.id == id).first()

    return mouse