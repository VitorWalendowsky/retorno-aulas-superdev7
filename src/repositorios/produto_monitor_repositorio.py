from sqlalchemy.orm import Session
from src.database.models import Monitor



def cadastrar (db: Session, nome: str, polegadas: float, frequenaica: int, preco: float):
    monitor = Monitor(
        nome=nome,
        polegadas=polegadas,
        frequencia=frequenaica,
        preco=preco
    )
    db.add(monitor)
    db.commit()
    db.refresh(monitor)
    return monitor


def obter_todos(db: Session):
    monitores = db.query(Monitor).all()
    return monitores


def obter_por_id(db: Session, monitor_id: int):
    monitor = db.query(Monitor).filter(Monitor.id == monitor_id).first()
    return Monitor


def apagar(db: Session, id:int):
    monitor = db.query(Monitor).filter(Monitor.id == id).first()
    if not monitor:
        return None
    
    db.delete(monitor)
    db.commit()
    return monitor


def editar(db: Session, monitor_id: int, nome: str, polegadas: float, frequencia: int, preco: float):
        monitor = db.query(Monitor).filter(Monitor.id == monitor_id).first()
        if not monitor:
            return None
        
        monitor.nome = nome
        monitor.polegadas = polegadas
        monitor.frequencia = frequencia
        monitor.preco = preco

        db.commit()
        db.refresh(monitor)
        return monitor