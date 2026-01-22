from sqlalchemy.orm import Session
from src.database.models import Notebook



def cadastrar(db: Session, nome: str, polegadas: float, quantidade_ram: int, processador: str, placa_video: str, rgb: bool, peso: float, ssd: bool, preco: float):
    notebook = Notebook(
    nome = nome,
    polegadas = polegadas,
    quantidade_ram = quantidade_ram,
    processador = processador,
    placa_video = placa_video,
    rgb = rgb,
    peso = peso,
    ssd = ssd,
    preco = preco
    )
    db.add(notebook)
    db.commit()
    db.refresh(notebook)
    return notebook


def obter_todos(db: Session):
    notebooks = db.query(Notebook).all()
    return notebooks


def obter_por_id(db: Session, notebook_id: int):
    notebook = db.query(Notebook).filter(Notebook.id == notebook_id).first()
    return notebook

def apagar(db: Session, id:int):
    notebook = db.query(Notebook).filter(Notebook.id == id).first()
    if not notebook:
        return None
    
    db.delete(notebook)
    db.commit()
    return notebook


def editar(db: Session, notebook_id: int, nome: str, polegadas: float, quantidade_ram: int, processador: str, placa_video: str, rgb: bool, peso: float, ssd: bool, preco: float):
        notebook = db.query(Notebook).filter(Notebook.id == notebook_id).first()
        if not notebook:
            return None
        
        notebook.nome = nome
        notebook.polegadas = polegadas
        notebook.quantidade_ram = quantidade_ram
        notebook.processador = processador
        notebook.placa_video = placa_video
        notebook.rgb = rgb
        notebook.peso = peso
        notebook.ssd = ssd
        notebook.preco = preco

        db.commit()
        db.refresh(notebook)
        return notebook
